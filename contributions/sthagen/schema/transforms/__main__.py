"""Magi main module to allow python -m transforms calls."""

import sys

from transforms.cli import main

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))  # pragma: no cover
