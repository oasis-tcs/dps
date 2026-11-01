"""Derive the overview figure (src/images/metadata.{dot,svg}) from the JSON schema.

The figure shows the root type and the type of each top-level member with all its members, in the words of the
property tables (type names, `String /uri`, multiplicities), so it cannot disagree with them: both come from the
same JADN derivation (bin/derive_jadn.py) of the schema. Graphviz `dot` renders the SVG from the derived source.

Usage:
    python bin/derive_figure.py            # rewrite metadata.dot and render metadata.svg
    python bin/derive_figure.py --check    # report drift of metadata.dot as a diff; exit 1 when not derived
"""

import argparse
import difflib
import html
import json
import shutil
import subprocess  # nosec B404 - runs graphviz dot on the derived source
import sys
from pathlib import Path
from typing import Any

EDIT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(EDIT))  # run as a script: make the bin package importable

from bin.derive_jadn import SCHEMA, Deriver  # noqa: E402
from bin.derive_tables import INLINE, cardinality  # noqa: E402

ENCODING = 'utf-8'
DOT = EDIT / 'src' / 'images' / 'metadata.dot'
SVG = DOT.with_suffix('.svg')
HEAD = '#dde6f2'


def box(t: list[Any]) -> str:
    """An HTML-like Graphviz label: the type name over its members (name : Type [multiplicity])."""
    title = f'<tr><td bgcolor="{HEAD}"><b>{html.escape(t[0])}</b></td></tr>'
    fields = t[4] if len(t) > 4 else []
    lines = [f'{f[1]} : {INLINE.get(f[2], f[2])} [{cardinality(f[3]).replace(chr(92), "")}]' for f in fields] or [
        '(opaque)'
    ]
    body = '<br align="left"/>'.join(html.escape(line) for line in lines) + '<br align="left"/>'
    return f'<<table border="0" cellborder="1" cellspacing="0" cellpadding="5">{title}<tr><td align="left">{body}</td></tr></table>>'


def dot(model: dict[str, Any]) -> str:
    types = {t[0]: t for t in model['types']}
    root = types[model['info']['exports'][0]]
    out = [
        '// Derived from json/data-provenance.json by bin/derive_figure.py - do not edit.',
        'digraph metadata {',
        '  graph [rankdir=TB, nodesep=0.25, ranksep=0.5, fontname="Helvetica"];',
        '  node [shape=plain, fontname="Helvetica", fontsize=10];',
        '  edge [fontname="Helvetica", fontsize=9, dir=back, arrowtail=diamond];',
        f'  "{root[0]}" [label={box(root)}];',
    ]
    segments = [f for f in root[4] if f[2] in types and len(types[f[2]]) > 3 and types[f[2]][1] in ('Record', 'Map')]
    for f in segments:
        out.append(f'  "{f[2]}" [label={box(types[f[2]])}];')
    out.append('  { rank=same; ' + ' '.join(f'"{f[2]}";' for f in segments) + ' }')
    for f in segments:
        out.append(f'  "{root[0]}" -> "{f[2]}" [label=" {f[1]} [{cardinality(f[3]).replace(chr(92), "")}]"];')
    out.append('}')
    return '\n'.join(out) + '\n'


def render() -> None:
    if not shutil.which('dot'):
        raise SystemExit('derive_figure: graphviz dot not found (brew install graphviz)')
    svg = subprocess.run(
        ['dot', '-Tsvg', str(DOT)], capture_output=True, text=True, check=True
    ).stdout  # nosec B603 B607
    SVG.write_text(svg, encoding=ENCODING)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--check', action='store_true', help='report drift and exit 1 instead of rewriting')
    args = parser.parse_args(argv)
    derived = dot(Deriver(json.loads(SCHEMA.read_text(encoding=ENCODING))).derive())
    current = DOT.read_text(encoding=ENCODING) if DOT.exists() else ''
    if derived == current and (args.check or SVG.exists()):
        print(f'{DOT.name}: derived from the schema', file=sys.stderr)
        return 0
    if args.check:
        sys.stdout.writelines(
            difflib.unified_diff(current.splitlines(True), derived.splitlines(True), str(DOT), 'derived')
        )
        print(f'{DOT.name}: differs from the schema', file=sys.stderr)
        return 1
    DOT.write_text(derived, encoding=ENCODING)
    render()
    print(f'{DOT.name}: rewritten from the schema; {SVG.name} rendered', file=sys.stderr)
    return 0


if __name__ == '__main__':
    sys.exit(main())
