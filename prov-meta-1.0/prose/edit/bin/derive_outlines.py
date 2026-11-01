"""Derive the YAML outlines of the prose from the JSON schema, one per annotated fence.

The JSON schema is the source: every fence opened by ```{.yaml json-path="..."} gets its body generated from the
schema node that its JSON path addresses. The outline shows that node in its place in a document, from the root
member DataProvenance down (other members of each level elided as `# ...`), in kaava's type vocabulary
(String.URI, Sequence, $defs.version-type, ...), so `nide quality` cross-checks the result with the same words.

What a fence shows depends on where its path ends:

  ...properties          the members of that object, one line each
  any other schema node  the member it belongs to, expanded: inline objects and arrays in full, a reference to a
                         definition followed once (references further down stay as $defs.x words); facet keywords
                         (pattern, format, type, const, enum, $ref, required, minProperties, items, ...) select the
                         member they constrain

Members are listed required first, then optional ones marked `# optional`, both in schema order.

Usage:
    python bin/derive_outlines.py            # rewrite the fence bodies under src/ in place
    python bin/derive_outlines.py --check    # report drift as a diff; exit 1 when any fence is not derived
"""

import argparse
import difflib
import json
import re
import sys
from pathlib import Path
from typing import Any

import jsonpath
from kaava import classify
from ruamel.yaml import YAML

ENCODING = 'utf-8'
EDIT = Path(__file__).resolve().parent.parent
ROOT_NAME = 'DataProvenance'
ELIDED = '# ...'
FENCE = re.compile(r'^```\{\.yaml json-path="(?P<path>[^"]*)"\}\n(?P<body>.*?)^```$', re.M | re.S)
FACETS = frozenset({'$ref', 'const', 'enum', 'format', 'items', 'maxItems', 'minItems', 'minLength', 'minProperties'})
FACETS |= {'pattern', 'required', 'type', 'uniqueItems', 'default', 'additionalProperties'}

Step = tuple[str, str]  # ('member', name) or ('item', '')
Line = tuple[int, str, str]  # (indent, text, comment)


def load_schema() -> dict[str, Any]:
    """The schema that etc/nide.yaml names for the json-path check: one source for both."""
    config = YAML(typ='safe').load((EDIT / 'etc' / 'nide.yaml').read_text(encoding=ENCODING))
    return json.loads((EDIT / config['pi']['json-schema']).read_text(encoding=ENCODING))


class Outliner:
    """Render outlines of one schema; knows where each schema node sits in an instance document."""

    def __init__(self, schema: dict[str, Any]) -> None:
        self.schema = schema
        self.places: dict[tuple[str, ...], tuple[Step, ...]] = {}
        self._visit(schema, (), (), frozenset())

    def _visit(self, node: Any, loc: tuple[str, ...], place: tuple[Step, ...], seen: frozenset[str]) -> None:
        """Record the first instance place of every schema location, in schema order (refs followed once)."""
        if not isinstance(node, dict):
            return
        self.places.setdefault(loc, place)
        if ref := node.get('$ref'):
            name = ref.rsplit('/', 1)[-1]
            if name not in seen:
                self._visit(self.schema['$defs'][name], ('$defs', name), place, seen | {name})
        for key, member in node.get('properties', {}).items():
            self._visit(member, (*loc, 'properties', key), (*place, ('member', key)), seen)
        if 'items' in node:
            self._visit(node['items'], (*loc, 'items'), (*place, ('item', '')), seen)

    def deref(self, node: dict[str, Any]) -> dict[str, Any]:
        ref = node.get('$ref')
        return self.schema['$defs'][ref.rsplit('/', 1)[-1]] if ref else node

    def subject(self, expr: str) -> tuple[str, tuple[Step, ...]]:
        """('members' | 'member', instance place) of the schema node that a JSON path addresses."""
        matches = list(jsonpath.finditer(expr, self.schema))
        if not matches:
            raise LookupError(f'json-path {expr!r} does not resolve against the schema')
        loc = tuple(str(part) for part in matches[0].parts)
        while loc and (loc[-1] in FACETS or loc[-1].isdigit()) and loc[-2:-1] != ('properties',):  # format: a member
            loc = loc[:-1]
        kind = 'members' if loc and loc[-1] == 'properties' else 'member'
        loc = loc[:-1] if kind == 'members' else loc
        if loc not in self.places:
            raise LookupError(f'json-path {expr!r} addresses {"/".join(loc)!r}, which no document can reach')
        place = self.places[loc]
        return ('members' if not place else kind), place

    def outline(self, expr: str) -> str:
        kind, place = self.subject(expr)
        lines: list[Line] = [(0, f'{ROOT_NAME}:', '')]
        lines += self._context(self.schema, place, 2, kind)
        return render(lines)

    # -- members ----------------------------------------------------------------------------------------------------

    @staticmethod
    def ordered(node: dict[str, Any]) -> list[tuple[str, Any, bool]]:
        """(name, schema, optional) of an object's members: required first, then optional, each in schema order."""
        required = node.get('required', [])
        members = node.get('properties', {})
        listed = [(k, members[k], False) for k in members if k in required]
        return listed + [(k, v, 'minProperties' not in node) for k, v in members.items() if k not in required]

    def _context(self, node: dict[str, Any], steps: tuple[Step, ...], indent: int, kind: str) -> list[Line]:
        """Lines from an object level down to the subject; `node` is the (dereferenced) schema of the level."""
        if not steps:
            return self._flat(node, indent)
        (step, name), rest = steps[0], steps[1:]
        if step == 'item':
            return as_item(self._context(self.deref(node['items']), rest, indent + 2, kind), indent)
        members = self.ordered(node)
        index = next(i for i, (key, _, _) in enumerate(members) if key == name)
        _, member, optional = members[index]
        lines: list[Line] = [(indent, ELIDED, '')] if index > 0 else []
        if rest:
            lines.append((indent, f'{name}:', comment(optional)))
            lines += self._context(self.deref(member), rest, indent + 2, kind)
        elif kind == 'members':
            lines.append((indent, f'{name}:', comment(optional, self.deref(member))))
            target = self.deref(member)
            if target.get('type') == 'array':
                lines += as_item(self._flat(self.deref(target['items']), indent + 4), indent + 2)
            else:
                lines += self._flat(target, indent + 2)
        else:
            lines += self._expand(name, member, indent, optional, follow=True)
        if index < len(members) - 1:
            lines.append((indent, ELIDED, ''))
        return lines

    def _flat(self, node: dict[str, Any], indent: int) -> list[Line]:
        """One line per member, its type as a word."""
        return [
            (indent, f'{key}: {classify(member)}', comment(optional)) for key, member, optional in self.ordered(node)
        ]

    def _expand(self, name: str, node: dict[str, Any], indent: int, optional: bool, follow: bool) -> list[Line]:
        """A member in full: inline structure recursively, its own reference (and its items' one) followed once."""
        target = self.deref(node) if follow and self._structured(self.deref(node)) else node
        if target.get('properties'):
            head = (indent, f'{name}:', comment(optional, target))
            return [head] + self._members(target, indent + 2)
        if target.get('type') == 'array' and 'items' in target:
            items = target['items']
            items = self.deref(items) if follow and self._structured(self.deref(items)) else items
            head = (indent, f'{name}:', comment(optional, items))
            if items.get('properties'):
                return [head] + as_item(self._members(items, indent + 4), indent + 2)
            return [head, (indent + 2, f'- {classify(items)}', comment(False, values=items if follow else None))]
        return [(indent, f'{name}: {classify(node)}', comment(optional, values=target if follow else None))]

    def _members(self, node: dict[str, Any], indent: int) -> list[Line]:
        lines: list[Line] = []
        for key, member, optional in self.ordered(node):
            lines += self._expand(key, member, indent, optional, follow=False)
        return lines

    def _structured(self, node: dict[str, Any]) -> bool:
        return bool(node.get('properties')) or node.get('type') == 'array'


def comment(optional: bool, node: dict[str, Any] | None = None, values: dict[str, Any] | None = None) -> str:
    notes = ['optional'] if optional else []
    if node is not None and (least := node.get('minProperties')) and not node.get('required'):
        notes.append('at least one of these members' if least == 1 else f'at least {least} of these members')
    if values is not None and 'enum' in values:
        notes.append(' | '.join(str(v) for v in values['enum']))
    return '; '.join(notes)


def as_item(lines: list[Line], indent: int) -> list[Line]:
    """Make lines (rendered two deeper than `indent`) the one example item of a sequence at `indent`."""
    if not lines:
        return lines
    first_indent, text, note = lines[0]
    return [(indent, f'- {text}', note)] + lines[1:] if first_indent == indent + 2 else lines


def render(lines: list[Line]) -> str:
    """Join lines, aligning the comments of each run of sibling leaf lines (same key column) on one column.

    A header line (`name:` with members below it) keeps its comment close and ends the run around it.
    """
    texts = [' ' * indent + text for indent, text, _ in lines]
    columns = [-1 if t.endswith(':') else len(t) - len(t.lstrip(' -')) for t in texts]
    out = []
    for i, (text, (_, _, note)) in enumerate(zip(texts, lines)):
        if not note or columns[i] < 0:
            out.append(f'{text}  # {note}' if note else text)
            continue
        group = [j for j in _run(texts, columns, i) if lines[j][2]]
        width = max(len(texts[j]) for j in group)
        out.append(f'{text.ljust(width)}  # {note}')
    return '\n'.join(out) + '\n'


def _run(texts: list[str], columns: list[int], i: int) -> range:
    """The contiguous run of lines around i at the same key column (elision lines do not interrupt a run)."""
    same = lambda j: columns[j] == columns[i] or texts[j].strip() == ELIDED  # noqa: E731
    start, end = i, i
    while start > 0 and same(start - 1):
        start -= 1
    while end < len(texts) - 1 and same(end + 1):
        end += 1
    return range(start, end + 1)


def derive(text: str, outliner: Outliner) -> str:
    return FENCE.sub(lambda m: f'```{{.yaml json-path="{m["path"]}"}}\n{outliner.outline(m["path"])}```', text)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--check', action='store_true', help='report drift and exit 1 instead of rewriting')
    parser.add_argument('sources', nargs='*', type=Path, help='markdown sources (default: src/*.md)')
    args = parser.parse_args(argv)
    outliner = Outliner(load_schema())
    drifted = fences = 0
    for path in args.sources or sorted((EDIT / 'src').glob('*.md')):
        text = path.read_text(encoding=ENCODING)
        fences += len(FENCE.findall(text))
        derived = derive(text, outliner)
        if derived == text:
            continue
        drifted += 1
        if args.check:
            sys.stdout.writelines(
                difflib.unified_diff(text.splitlines(True), derived.splitlines(True), str(path), 'derived')
            )
        else:
            path.write_text(derived, encoding=ENCODING)
    verb = 'differ from' if args.check else 'rewritten from'
    print(f'{fences} outline fence(s); {drifted} file(s) {verb} the schema', file=sys.stderr)
    return 1 if args.check and drifted else 0


if __name__ == '__main__':
    sys.exit(main())
