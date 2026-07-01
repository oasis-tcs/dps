"""Apply YAML-configured text patches to text files."""

import sys
from pathlib import Path

import yaml

ENCODING = 'utf-8'


def main() -> None:
    """Drive the configuration based transforms."""
    if len(sys.argv) != 2:
        print(f'usage: {Path(sys.argv[0]).name} patches.yaml', file=sys.stderr)
        sys.exit(1)
    config: dict = yaml.safe_load(Path(sys.argv[1]).read_text(encoding=ENCODING))
    for path, pairs in config.items():
        target = Path(path)
        if not target.exists():
            if path != '00-usage-hints':
                print(f'warning: {path} not found, skipping', file=sys.stderr)
            continue
        text = target.read_text(encoding=ENCODING)
        for this, that in pairs:
            text = text.replace(this, that)
        target.write_text(text, encoding=ENCODING)


if __name__ == '__main__':
    main()
