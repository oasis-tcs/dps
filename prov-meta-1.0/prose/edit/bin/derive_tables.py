"""Derive the property tables of the Provenance Schema sections from the JADN information model.

Each table is found by its caption (Table: Type `Name` (Kind){#tab:...}) in src/schema-*.md and regenerated from
the JADN type of that name, with the `\\columns=` width line before it; all prose between the tables stays.
Every JADN type except the format aliases (URI, UUID, DateTime, Date: written inline as `String /format`) needs
exactly one table, and every table a type: a type without a table, or a table without a type, is an error.

Column widths are one set per table shape (members, enumeration items, simple types), so that all tables of a
shape share one grid: each identifier column is as wide as the longest identifier of that shape in any table (they
must not wrap: a hyphen inside a code value would read as part of it), the description takes the rest of the line.

Usage:
    python bin/derive_tables.py            # rewrite the tables under src/ in place
    python bin/derive_tables.py --check    # report drift as a diff; exit 1 when any table is not derived
"""

import argparse
import difflib
import json
import re
import sys
from pathlib import Path
from typing import Any

ENCODING = 'utf-8'
EDIT = Path(__file__).resolve().parent.parent
JADN = EDIT.parent.parent / 'jadn' / 'data-provenance.jadn'
INLINE = {'URI': 'String /uri', 'UUID': 'String /uuid', 'DateTime': 'String /date-time', 'Date': 'String /date'}
SUFFIX = {'Record': 'record', 'Map': 'map', 'Enumerated': 'enum', 'ArrayOf': 'array', 'String': 'string'}
LINE = 100  # characters of table text across the text width (measured in the PDF: about 103)
PAD = 2  # characters of cell padding on top of an identifier
HEADERS = {
    'fields': ['ID', 'Name', 'Type', '\\#', 'Description'],
    'items': ['ID', 'Item', 'Description'],
    'simple': ['Type Name', 'Type Definition', 'Description'],
}
LETTERS = {'fields': 'inthd', 'items': 'ind', 'simple': 'ntd'}  # only the lengths count; never '#'
TABLE = re.compile(
    r'(?P<columns>^\\columns=[^\n]*\n\n)?(?P<table>(?:^\|[^\n]*\n)+)\nTable: Type `(?P<name>\w+)` \((?P<kind>[^\n]*?)\)\{#tab:[^}]*\}$',
    re.M,
)


def kebab(name: str) -> str:
    return re.sub(r'(?<=[a-z0-9])(?=[A-Z])', '-', name).lower()


def cardinality(opts: list[str]) -> str:
    low = '0' if '[0' in opts else '1'
    return f'{low}..\\*' if ']0' in opts else ('0..1' if low == '0' else '1')


def grid(header: list[str], align: list[str], rows: list[list[str]]) -> str:
    """A pipe table with every column padded to its widest cell; `align` is 'r' or 'l' per column."""
    width = [max(len(c) for c in col) for col in zip(header, *rows)]

    def fmt(cells: list[str]) -> str:
        return '| ' + ' | '.join(c.rjust(w) if a == 'r' else c.ljust(w) for c, w, a in zip(cells, width, align)) + ' |'

    rule = (
        '|' + '|'.join(('-' * (w + 1) + ':') if a == 'r' else (':' + '-' * (w + 1)) for w, a in zip(width, align)) + '|'
    )
    return '\n'.join([fmt(header), rule] + [fmt(r) for r in rows]) + '\n'


def kind_of(t: list[Any]) -> str:
    return f'ArrayOf({t[2][0][1:]})' if t[1] == 'ArrayOf' else t[1]


def shape_rows(t: list[Any]) -> tuple[str, list[list[str]]]:
    """(shape, rows) of the table of a JADN type."""
    fields = t[4] if len(t) > 4 else []
    if t[1] in ('Record', 'Map') and fields:
        return 'fields', [[str(f[0]), f[1], INLINE.get(f[2], f[2]), cardinality(f[3]), f[4]] for f in fields]
    if t[1] == 'Enumerated':
        return 'items', [[str(f[0]), f[1], f[2]] for f in fields]
    return 'simple', [[t[0], kind_of(t), t[3]]]


def columns(types: list[list[Any]]) -> dict[str, str]:
    """One `\\columns=` line per table shape: identifier columns fit their longest cell, the description the rest."""
    widest: dict[str, list[int]] = {}
    for t in types:
        shape, rows = shape_rows(t)
        cells = [HEADERS[shape]] + rows
        width = [max(len(r[i].replace('\\', '')) for r in cells) + PAD for i in range(len(HEADERS[shape]) - 1)]
        widest[shape] = [max(a, b) for a, b in zip(widest.get(shape, width), width)]
    lines = {}
    for shape, width in widest.items():
        letters = LETTERS[shape]
        rest = LINE - sum(width)
        lines[shape] = '\\columns=' + ','.join(c * w for c, w in zip(letters, width + [rest]))
    return lines


def table(t: list[Any], widths: dict[str, str]) -> tuple[str, str, str]:
    """(columns line, table, caption) of a JADN type."""
    name, base = t[0], t[1]
    shape, rows = shape_rows(t)
    body = grid(HEADERS[shape], list('rllll' if shape == 'fields' else 'rll' if shape == 'items' else 'lll'), rows)
    caption = f'Table: Type `{name}` ({kind_of(t)}){{#tab:{kebab(name)}-{SUFFIX[base]}}}'
    return widths[shape], body, caption


def derive(text: str, types: dict[str, list[Any]], seen: set[str]) -> str:
    widths = columns(list(types.values()))

    def replace(m: re.Match[str]) -> str:
        name = m['name']
        if name not in types:
            raise LookupError(f'table of type {name!r}: no such type in {JADN.name}')
        seen.add(name)
        width, body, caption = table(types[name], widths)
        return f'{width}\n\n{body}\n{caption}'

    return TABLE.sub(replace, text)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--check', action='store_true', help='report drift and exit 1 instead of rewriting')
    args = parser.parse_args(argv)
    types = {t[0]: t for t in json.loads(JADN.read_text(encoding=ENCODING))['types'] if t[0] not in INLINE}
    seen: set[str] = set()
    drifted = 0
    for path in sorted((EDIT / 'src').glob('schema-*.md')):
        text = path.read_text(encoding=ENCODING)
        derived = derive(text, types, seen)
        if derived == text:
            continue
        drifted += 1
        if args.check:
            sys.stdout.writelines(
                difflib.unified_diff(text.splitlines(True), derived.splitlines(True), str(path), 'derived')
            )
        else:
            path.write_text(derived, encoding=ENCODING)
    if missing := sorted(set(types) - seen):
        print(f'types without a table (add a caption line where each belongs): {", ".join(missing)}', file=sys.stderr)
        return 1
    verb = 'differ from' if args.check else 'rewritten from'
    print(f'{len(seen)} table(s); {drifted} file(s) {verb} {JADN.name}', file=sys.stderr)
    return 1 if args.check and drifted else 0


if __name__ == '__main__':
    sys.exit(main())
