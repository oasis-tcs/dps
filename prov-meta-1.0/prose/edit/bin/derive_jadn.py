"""Derive the JADN information model from the JSON schema.

The JSON schema is the source. Each schema node that is a JADN type carries its type name as the annotation
`x-jadn-type`, each enumeration the descriptions of its values as `x-jadn-enum`; the members' `description`s
become the field descriptions. The string formats map to the primitive aliases URI, UUID, DateTime and Date.

Type order: the root, then the types of each top-level member (segment) depth first in member order,
then the types used by more than one segment (shared), then the string aliases.

Usage:
    python bin/derive_jadn.py            # rewrite ../../jadn/data-provenance.jadn
    python bin/derive_jadn.py --check    # report drift as a diff; exit 1 when the file is not derived
"""

import argparse
import difflib
import json
import sys
from pathlib import Path
from typing import Any

ENCODING = 'utf-8'
EDIT = Path(__file__).resolve().parent.parent
SCHEMA = EDIT.parent.parent / 'json' / 'data-provenance.json'
TARGET = EDIT.parent.parent / 'jadn' / 'data-provenance.jadn'
INFO = {
    'title': 'Data Provenance Metadata',
    'package': 'https://docs.oasis-open.org/dps/prov-meta/v1.0/schema/',
    'version': '1.0',
    'description': 'JADN information model for OASIS Data Provenance Standard (DPS) prov-meta v1.0.',
    'license': 'https://www.oasis-open.org/policies-guidelines/ipr/',
    'exports': ['DataProvenance'],
}
FORMATS = {  # JSON schema string format -> (JADN alias, description)
    'uri': ('URI', 'A Uniform Resource Identifier (RFC 3986).'),
    'uuid': ('UUID', 'A Universally Unique Identifier (RFC 4122).'),
    'date-time': ('DateTime', 'An RFC 3339 date-time string.'),
    'date': ('Date', 'An RFC 3339 full-date string (YYYY-MM-DD).'),
}
ALIASES = {alias for alias, _ in FORMATS.values()}
PRIMITIVES = {'string': 'String', 'boolean': 'Boolean', 'integer': 'Integer', 'number': 'Number'}

Type = list[Any]


class Deriver:
    def __init__(self, schema: dict[str, Any]) -> None:
        self.schema = schema
        self.types: dict[str, Type] = {}
        self.segments: dict[str, set[str]] = {}  # type name -> top-level members whose subtree uses it
        self.order: dict[str, list[str]] = {}  # segment -> types in depth-first order of first use

    def deref(self, node: dict[str, Any]) -> dict[str, Any]:
        ref = node.get('$ref')
        return self.schema['$defs'][ref.rsplit('/', 1)[-1]] if ref else node

    def type_node(self, name: str) -> dict[str, Any]:
        """The schema node annotated as JADN type `name` (an empty dict for primitives and aliases)."""
        if not hasattr(self, '_nodes'):
            self._nodes: dict[str, dict[str, Any]] = {}
            stack: list[Any] = [self.schema]
            while stack:
                node = stack.pop()
                if isinstance(node, dict):
                    self._nodes.setdefault(node.get('x-jadn-type', ''), node)
                    stack += node.values()
                elif isinstance(node, list):
                    stack += node
        return self._nodes.get(name, {})

    def field_type(self, node: dict[str, Any]) -> str:
        """The JADN type name of a (dereferenced) schema node used as a field or element type."""
        if name := node.get('x-jadn-type'):
            return str(name)
        if fmt := node.get('format'):
            return FORMATS[fmt][0]
        kind = node.get('type') or ('string' if isinstance(node.get('const'), str) else '')
        return PRIMITIVES[str(kind)]

    def element(self, member: dict[str, Any], optional: bool) -> tuple[dict[str, Any], list[str]]:
        """(type node, JADN field options) of a member: arrays become a multiplicity, not a type."""
        node = self.deref(member)
        opts = ['[0'] if optional else []
        if node.get('type') == 'array' and 'x-jadn-type' not in node:
            opts = ['[0' if optional else '[1', ']0']
            node = self.deref(node['items'])
        return node, opts

    def visit(self, node: dict[str, Any], segment: str) -> None:
        name = node.get('x-jadn-type')
        if not name or name in ALIASES:
            return
        if segment in self.segments.setdefault(name, set()):
            return
        self.segments[name].add(segment)
        if name in self.types:  # met again from another segment: its own subtypes are used there too
            for field in self.types[name][4] if len(self.types[name]) > 4 else []:
                self.visit(self.type_node(field[2]), segment)
            return
        self.order.setdefault(segment, []).append(name)
        description = node.get('description', '')
        if 'enum' in node:
            values = node.get('x-jadn-enum', {})
            self.types[name] = [
                name,
                'Enumerated',
                [],
                description,
                [[i, v, values.get(v, '')] for i, v in enumerate(node['enum'], 1)],
            ]
        elif node.get('type') == 'array':
            item = self.deref(node['items'])
            opts = [f'*{self.field_type(item)}'] + ([f'[{node["minItems"]}'] if 'minItems' in node else [])
            self.types[name] = [name, 'ArrayOf', opts, description]
        elif node.get('type') == 'object' or 'properties' in node:
            required = node.get('required', [])
            least = node.get('minProperties')
            base = 'Map' if (least and not required) or not node.get('properties') else 'Record'
            fields: list[list[Any]] = []
            children: list[dict[str, Any]] = []
            for i, (key, member) in enumerate(node.get('properties', {}).items(), 1):
                target, opts = self.element(member, key not in required)
                fields.append([i, key, self.field_type(target), opts, member.get('description', '')])
                children.append(target)
            self.types[name] = [name, base, [f'{{{least}'] if least and not required else [], description, fields]
            for child in children:
                self.visit(child, segment)
        else:
            self.types[name] = [name, PRIMITIVES[node.get('type', 'string')], [], description]

    def derive(self) -> dict[str, Any]:
        root = self.schema
        self.types[root['x-jadn-type']] = []  # placeholder keeps the root first
        self.visit_root(root)
        shared = [n for seg in self.order.values() for n in seg if len(self.segments[n]) > 1 and n not in ALIASES]
        strings = [n for seg in self.order.values() for n in seg if self.types[n][1] == 'String' and n not in shared]
        names = [root['x-jadn-type']]
        names += [n for seg in self.order.values() for n in seg if n not in shared and n not in strings]
        names += [n for n in shared if self.types[n][1] != 'String'] + [
            n for n in shared if self.types[n][1] == 'String'
        ]
        names += strings
        used = {f[2] for t in self.types.values() if len(t) > 4 for f in t[4]} | {
            o[1:] for t in self.types.values() for o in t[2]
        }
        aliases = [[alias, 'String', [f'/{fmt}'], text] for fmt, (alias, text) in FORMATS.items() if alias in used]
        return {'info': INFO, 'types': [self.types[n] for n in names] + aliases}

    def visit_root(self, root: dict[str, Any]) -> None:
        name = root['x-jadn-type']
        required = root.get('required', [])
        fields = []
        for i, (key, member) in enumerate(root['properties'].items(), 1):
            target, opts = self.element(member, key not in required)
            fields.append([i, key, self.field_type(target), opts, member.get('description', '')])
            self.visit(target, key)
        self.types[name] = [name, 'Record', [], root.get('description', ''), fields]


def dump(model: dict[str, Any]) -> str:
    """The JADN file in its reviewed layout: one type per block, field columns aligned within a type."""
    enc = lambda value: json.dumps(value, ensure_ascii=False)  # noqa: E731
    out = ['{', '  "info": {']
    info = [f'    {enc(k)}: {enc(v)}' for k, v in model['info'].items()]
    out += [line + ',' for line in info[:-1]] + [info[-1], '  },', '  "types": [', '']
    blocks = []
    simple: list[Type] = []

    def flush() -> None:
        if simple:
            cols = [max(len(enc(t[i])) + 1 for t in simple) for i in range(3)]
            rows = [
                f'    [{"".join((enc(t[i]) + ",").ljust(cols[i] + 1) for i in range(3))}{enc(t[3])}]' for t in simple
            ]
            blocks.append(',\n'.join(rows))
            simple.clear()

    for t in model['types']:
        if len(t) == 4:
            simple.append(t)
            continue
        flush()
        head = f'    [{enc(t[0])}, {enc(t[1])}, {enc(t[2])}, {enc(t[3])}, ['
        rows = [[enc(c) + ',' for c in f[:-1]] for f in t[4]]
        width = [max(len(r[i]) for r in rows) for i in range(len(rows[0]))] if rows else []
        lines = [
            f'      [{" ".join(c.ljust(width[i]) for i, c in enumerate(r))} {enc(f[-1])}]' for r, f in zip(rows, t[4])
        ]
        blocks.append(head + ('\n' + ',\n'.join(lines) if lines else '') + '\n    ]]')
    flush()
    out.append(',\n\n'.join(blocks))
    out += ['', '  ]', '}']
    return '\n'.join(out) + '\n'


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--check', action='store_true', help='report drift and exit 1 instead of rewriting')
    args = parser.parse_args(argv)
    derived = dump(Deriver(json.loads(SCHEMA.read_text(encoding=ENCODING))).derive())
    current = TARGET.read_text(encoding=ENCODING) if TARGET.exists() else ''
    if derived == current:
        print(f'{TARGET.name}: derived from the schema', file=sys.stderr)
        return 0
    if args.check:
        sys.stdout.writelines(
            difflib.unified_diff(current.splitlines(True), derived.splitlines(True), str(TARGET), 'derived')
        )
        print(f'{TARGET.name}: differs from the schema', file=sys.stderr)
        return 1
    TARGET.write_text(derived, encoding=ENCODING)
    print(f'{TARGET.name}: rewritten from the schema', file=sys.stderr)
    return 0


if __name__ == '__main__':
    sys.exit(main())
