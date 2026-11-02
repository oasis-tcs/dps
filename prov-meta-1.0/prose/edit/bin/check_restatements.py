"""Check the prose sentences that restate schema constraints against the JSON schema they restate.

Derive or check, never neither: the schema is the source, the outlines and tables are derived from it, and every MUST
sentence that repeats a schema fact in words is a hand copy - so each one is checked here against the schema.

The sources keep one sentence per line. A line's subject is, in this order: the field of a bullet (- `date`: ...)
below the section's member (#### Member `set.tracking.revision-history`); a dotted member path that resolves from the
root (The value of `set.tracking.id` ...); a type named in a type table's prose (The `Identity` type ..., by its
x-jadn-type); the fields named as The value of `x` / The `x` member / Both `x` and `y` below the section's member
(searched in depth when not a direct member); otherwise the section's member itself (The sequence ..., Each alias ...).

Claims and what the schema must say for them (on array members, about the items where the claim is about values):
  MUST be one of: `a`, `b` (or a bullet list)   enum equals the listed values
  MUST have / provide / contain `a` and `b`     required equals the listed members
  MUST contain the following members: (bullets) required equals the bulleted members
  MUST be unique                                uniqueItems
  MUST contain at least one                     minItems >= 1
  MUST have at least one of the following       minProperties >= 1, and the listed members are the properties
  At least one ... MUST be provided / present   minProperties >= 1
  valid URI                                     format uri
  date-time ... RFC 3339 / conform to RFC 3339  format date-time
  full-date (YYYY-MM-DD)                        format date
  conform to `$defs.x`                          a reference to $defs/x
  non-empty string                              type string and minLength >= 1
  JSON object                                   type object
  hex-encoded ... at least N hexadecimal digits the pattern accepts N hex digits, rejects N-1 and non-hex
  MUST NOT start or end with whitespace         the pattern rejects leading and trailing whitespace
  MUST be lowercase                             the pattern rejects uppercase
A MUST line with none of these claims is listed as not covered (--list), so the coverage stays visible.

Known differences, each waiting for a decision, are listed with their reason in etc/restatements-known.txt
(member path, claim, reason). They are reported but do not fail the check; a listed difference that no longer
exists fails it, so the list stays true (strict, like an expected failure).

Usage:
    python bin/check_restatements.py           # exit 1 on a new difference or a stale known one
    python bin/check_restatements.py --list    # also list the MUST lines that no claim covers
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Callable

ENCODING = 'utf-8'
EDIT = Path(__file__).resolve().parent.parent
SCHEMA = EDIT.parent.parent / 'json' / 'data-provenance.json'
KNOWN = EDIT / 'etc' / 'restatements-known.txt'
HEADING = re.compile(r'^#+ Member `([^`]+)`', re.M)
FENCE = re.compile(r'^```.*?^```', re.M | re.S)
VALUE_LIST = re.compile(r'([^\n]*MUST be one of)(:[^\n]*|\s+the following:\s*\n(?:\s*- `[^`]+`\s*\n?)+)')
MEMBER_LIST = re.compile(r'MUST contain the following members:\s*$')

Node = dict[str, Any]


class Schema:
    def __init__(self, schema: Node) -> None:
        self.schema = schema
        self.types: dict[str, Node] = {}
        stack: list[Any] = [schema]
        while stack:
            node = stack.pop()
            if isinstance(node, dict):
                if 'x-jadn-type' in node:
                    self.types.setdefault(node['x-jadn-type'], node)
                stack += node.values()
            elif isinstance(node, list):
                stack += node

    def deref(self, node: Node) -> Node:
        while '$ref' in node:
            node = self.schema['$defs'][node['$ref'].rsplit('/', 1)[-1]]
        return node

    def members(self, node: Node) -> dict[str, Node]:
        """The properties of a node, through references and array items."""
        node = self.deref(node)
        while node.get('type') == 'array' and 'items' in node and 'properties' not in node:
            node = self.deref(node['items'])
        return node.get('properties', {})

    def resolve(self, path: str) -> Node | None:
        """The raw schema node (references not followed) of a dotted member path or of `type:Name`."""
        if path.startswith('type:'):
            return self.types.get(path[5:])
        node: Node = self.schema
        for part in path.split('.'):
            members = self.members(node)
            if part not in members:
                return None
            node = members[part]
        return node

    def below(self, path: str, name: str) -> str | None:
        """The dotted path of the one member called `name` below `path` (None when absent or ambiguous)."""
        found: list[str] = []
        seen: set[int] = set()

        def walk(node: Node, at: str) -> None:
            if id(self.deref(node)) in seen:
                return
            seen.add(id(self.deref(node)))
            for key, member in self.members(node).items():
                if key == name:
                    found.append(f'{at}.{key}')
                walk(member, f'{at}.{key}')

        start = self.resolve(path)
        if start is not None:
            walk(start, path)
        return found[0] if len(found) == 1 else None

    def values(self, node: Node) -> Node:
        """The node that constrains the values: the items of an array, through references."""
        node = self.deref(node)
        while node.get('type') == 'array' and 'items' in node:
            node = self.deref(node['items'])
        return node


def _accepts(node: Node, text: str) -> bool:
    if 'minLength' in node and len(text) < node['minLength']:
        return False
    return 'pattern' not in node or re.search(node['pattern'], text) is not None


Claim = Callable[[Schema, Node, list[str]], str | None]


def _required(s: Schema, n: Node, spans: list[str]) -> str | None:
    item = s.values(n)
    listed = {x for x in spans if x in item.get('properties', {})}  # the member names among the code spans
    required = set(item.get('required', []))
    return None if listed == required else f'lists required {sorted(listed)}, the schema requires {sorted(required)}'


def _unique(s: Schema, n: Node, _: list[str]) -> str | None:
    return None if s.deref(n).get('uniqueItems') else 'says unique, the schema has no uniqueItems'


def _at_least_one(s: Schema, n: Node, _: list[str]) -> str | None:
    return None if s.deref(n).get('minItems', 0) >= 1 else 'says at least one, the schema has no minItems >= 1'


def _at_least_one_member(s: Schema, n: Node, listed: list[str]) -> str | None:
    item = s.values(n)
    if item.get('minProperties', 0) < 1:
        return 'says at least one member, the schema has no minProperties >= 1'
    if listed and set(listed) != set(item.get('properties', {})):
        return f'lists members {sorted(listed)}, the schema has {sorted(item.get("properties", {}))}'
    return None


def _format(expected: str) -> Claim:
    def claim(s: Schema, n: Node, _: list[str]) -> str | None:
        found = s.values(n).get('format')
        return None if found == expected else f'says {expected}, the schema has format {found!r}'

    return claim


def _reference(s: Schema, n: Node, names: list[str]) -> str | None:
    found = n.get('$ref', '')
    return (
        None if found.endswith('/' + names[0]) else f'says $defs.{names[0]}, the schema has {found or "no reference"}'
    )


def _non_empty(s: Schema, n: Node, _: list[str]) -> str | None:
    v = s.values(n)
    if v.get('type') != 'string' or v.get('minLength', 0) < 1:
        return f'says non-empty string, the schema has type {v.get("type")!r}, minLength {v.get("minLength")}'
    return None


def _object(s: Schema, n: Node, _: list[str]) -> str | None:
    found = s.deref(n).get('type')
    return None if found == 'object' else f'says JSON object, the schema has type {found!r}'


def _hex(s: Schema, n: Node, digits: list[str]) -> str | None:
    v, count = s.values(n), int(digits[0])
    if _accepts(v, 'a' * count) and not _accepts(v, 'a' * (count - 1)) and not _accepts(v, 'g' * count):
        return None
    return f'says hex with at least {count} digits, the schema pattern {v.get("pattern")!r} does not enforce it'


def _whitespace(s: Schema, n: Node, _: list[str]) -> str | None:
    v = s.values(n)
    if not _accepts(v, ' id') and not _accepts(v, 'id ') and _accepts(v, 'some-id'):
        return None
    return f'says no leading or trailing whitespace, the schema pattern {v.get("pattern")!r} does not enforce it'


def _lowercase(s: Schema, n: Node, _: list[str]) -> str | None:
    v = s.values(n)
    if _accepts(v, 'sha256') and not _accepts(v, 'SHA256'):
        return None
    return f'says lowercase, the schema ({v.get("pattern") or "no pattern"}) accepts uppercase'


_spans = lambda text: re.findall(r'`([^`]+)`', text)  # noqa: E731
CLAIMS: list[tuple[str, re.Pattern[str], Claim, Callable[[re.Match[str]], list[str]]]] = [
    (
        'required',
        re.compile(r'MUST (?:have|provide|contain)(?! at least)(?! the following)(.*)'),
        _required,
        lambda m: _spans(m[1]),
    ),
    ('unique', re.compile(r'MUST(?: \w+)? be unique'), _unique, lambda m: []),
    ('at-least-one', re.compile(r'MUST contain at least one'), _at_least_one, lambda m: []),
    (
        'at-least-one-member',
        re.compile(r'MUST have at least one of the following members: (.*)'),
        _at_least_one_member,
        lambda m: _spans(m[1]),
    ),
    (
        'at-least-one-member',
        re.compile(r'At least one [\w ]+ MUST be (?:provided|present)'),
        _at_least_one_member,
        lambda m: [],
    ),
    ('uri', re.compile(r'valid URI'), _format('uri'), lambda m: []),
    ('date', re.compile(r'full-date'), _format('date'), lambda m: []),
    (
        'date-time',
        re.compile(r'date-time string conforming to|MUST(?: each)? conform to \\?\[RFC 3339\\?\]'),
        _format('date-time'),
        lambda m: [],
    ),
    ('reference', re.compile(r'MUST conform to `\$defs\.([\w-]+)`'), _reference, lambda m: [m[1]]),
    ('non-empty', re.compile(r'MUST be a non-empty string'), _non_empty, lambda m: []),
    ('object', re.compile(r'MUST be a JSON object'), _object, lambda m: []),
    ('hex', re.compile(r'hex-encoded .*at least (\d+) hexadecimal digits'), _hex, lambda m: [m[1]]),
    ('whitespace', re.compile(r'MUST NOT start or end with whitespace'), _whitespace, lambda m: []),
    ('lowercase', re.compile(r'MUST be lowercase'), _lowercase, lambda m: []),
]


def subjects(s: Schema, line: str, section: str | None) -> list[str]:
    """The member paths (or `type:Name`) a line constrains."""
    if bullet := re.match(r'\s*- `([^`]+)`:', line):
        return [f'{section}.{bullet[1]}'] if section else []
    for span in _spans(line):
        if '.' in span and not span.startswith('$') and s.resolve(span) is not None:
            return [span]
    if typed := re.search(r'The `(\w+)` type', line):
        if typed[1] in s.types:
            return [f'type:{typed[1]}']
    named = re.findall(r'(?:The value of|The|Both|and) `([^`]+)`(?= member| and| are| MUST)', line)
    if section and named:
        paths = [f'{section}.{n}' if s.resolve(f'{section}.{n}') is not None else s.below(section, n) for n in named]
        return [p if p else f'{section}.{n}' for p, n in zip(paths, named)]
    return [section] if section else []


Finding = tuple[str, str, str]  # (where, member path, claim name) -> message via dict


def check(text: str, s: Schema, name: str, unchecked: list[str]) -> tuple[int, dict[Finding, str]]:
    findings: dict[Finding, str] = {}
    checked = 0
    masked = FENCE.sub(lambda m: re.sub(r'[^\n]', ' ', m.group()), text)
    headings = [(m.start(), m[1]) for m in HEADING.finditer(masked)]
    section_at = lambda at: next((h for start, h in reversed(headings) if start < at), None)  # noqa: E731
    lines = masked.splitlines()
    # value lists, inline or as a bullet list after "MUST be one of the following:"
    for m in VALUE_LIST.finditer(masked):
        where = f'{name}:{masked.count(chr(10), 0, m.start()) + 1}'
        section = section_at(m.start())
        lead = _spans(m[1])
        paths = [f'{section}.{lead[0]}'] if lead and '.' not in lead[0] and section else subjects(s, m[1], section)
        listed = set(_spans(m[2]))
        for path in paths:
            node = s.resolve(path)
            enum = s.values(node).get('enum') if node is not None else None
            checked += 1
            if enum is None:
                findings[(where, path, 'values')] = 'has a value list, but the schema has no enumeration there'
            elif listed != set(enum):
                findings[(where, path, 'values')] = (
                    f'value list: missing {sorted(set(enum) - listed)}, not in the schema {sorted(listed - set(enum))}'
                )
    # every other MUST line
    offset = 0
    for number, line in enumerate(lines, 1):
        start, offset = offset, offset + len(line) + 1
        if 'MUST' not in line or re.search(r'MUST be one of', line):
            continue
        where = f'{name}:{number}'
        # claims and their subject per MUST sentence: a line may hold more than one sentence (split outside code
        # spans); the field of a bullet is the subject of every sentence in that bullet
        section = section_at(start)
        bullet = re.match(r'\s*- `[^`]+`:', line)
        claims: list[tuple[list[str], str, Claim, list[str]]] = []
        for sentence in (x for x in re.split(r'(?<=\.)\s+(?=[A-Z])', line) if 'MUST' in x):
            paths = subjects(s, line if bullet else sentence, section)
            claims += [(paths, c, f, args(hit)) for c, p, f, args in CLAIMS if (hit := p.search(sentence))]
        if MEMBER_LIST.search(line):  # the bulleted members that follow are the required ones
            following = []
            for later in lines[number:]:
                if b := re.match(r'\s*- `([^`]+)`:', later):
                    following.append(b[1])
                elif later.strip():
                    break
            claims.append((subjects(s, line, section), 'required', _required, following))
        if not claims:
            unchecked.append(f'{where}: {line.strip()}')
            continue
        for paths, claim, function, args in claims:
            for path in paths:
                node = s.resolve(path)
                checked += 1
                if node is None:
                    findings[(where, path, claim)] = 'is not a member of the schema'
                elif message := function(s, node, args):
                    findings[(where, path, claim)] = message
    return checked, findings


def known() -> dict[tuple[str, str], str]:
    """(member path, claim) -> reason, from etc/restatements-known.txt."""
    entries = {}
    if KNOWN.exists():
        for line in KNOWN.read_text(encoding=ENCODING).splitlines():
            if line.strip() and not line.lstrip().startswith('#'):
                path, claim, reason = line.split(None, 2)
                entries[(path, claim)] = reason
    return entries


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--list', action='store_true', help='also list the MUST lines that no claim covers')
    args = parser.parse_args(argv)
    s = Schema(json.loads(SCHEMA.read_text(encoding=ENCODING)))
    findings: dict[Finding, str] = {}
    unchecked: list[str] = []
    checked = 0
    for source in sorted((EDIT / 'src').glob('*.md')):
        count, found = check(source.read_text(encoding=ENCODING), s, f'src/{source.name}', unchecked)
        checked += count
        findings.update(found)
    expected = known()
    seen = {(path, claim) for _, path, claim in findings}
    new = {k: v for k, v in findings.items() if (k[1], k[2]) not in expected}
    stale = sorted(k for k in expected if k not in seen)
    for (where, path, claim), message in sorted(findings.items()):
        tag = 'known' if (path, claim) in expected else 'NEW'
        print(f'{tag}: {where}: {path!r} {message}' + (f'  [{expected[(path, claim)]}]' if tag == 'known' else ''))
    for path, claim in stale:
        print(f'STALE: {KNOWN.name} lists {path} {claim}, which no longer differs - remove the entry')
    if args.list:
        for line in unchecked:
            print(f'not covered: {line}')
    print(
        f'{checked} restated constraint(s) checked: {len(new)} new and {len(findings) - len(new)} known difference(s), '
        f'{len(stale)} stale known entr(ies); {len(unchecked)} MUST line(s) not covered',
        file=sys.stderr,
    )
    return 1 if new or stale else 0


if __name__ == '__main__':
    sys.exit(main())
