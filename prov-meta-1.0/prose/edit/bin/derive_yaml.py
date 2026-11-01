"""Derive the YAML serialization of the JSON schema (yaml/data-provenance.yaml).

Usage:
    python bin/derive_yaml.py            # rewrite ../../yaml/data-provenance.yaml
    python bin/derive_yaml.py --check    # report drift as a diff; exit 1 when the file is not derived
"""

import argparse
import difflib
import json
import sys
from pathlib import Path

import yaml

ENCODING = 'utf-8'
EDIT = Path(__file__).resolve().parent.parent
SCHEMA = EDIT.parent.parent / 'json' / 'data-provenance.json'
TARGET = EDIT.parent.parent / 'yaml' / 'data-provenance.yaml'
HEADER = """\
# YAML serialization of data-provenance.json
# This file is generated from json/data-provenance.json; its content is identical, the JSON schema is normative.
# OASIS Data Provenance Standard (DPS) prov-meta v1.0
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--check', action='store_true', help='report drift and exit 1 instead of rewriting')
    args = parser.parse_args(argv)
    schema = json.loads(SCHEMA.read_text(encoding=ENCODING))
    derived = HEADER + yaml.safe_dump(schema, sort_keys=False, allow_unicode=True)
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
