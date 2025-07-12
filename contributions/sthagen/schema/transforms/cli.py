"""Command line interface for transforms helper tool."""

import argparse
import pathlib
import sys

from transforms.api import transform
from transforms import (
    APP_ALIAS,
    APP_ENV,
    APP_NAME,
    DEBUG,
    JSON_FORMAT,
    VERSION,
    YAML_FORMAT,
)


JSON_SUFFIXES = set(['.json'])
YAML_SUFFIXES = set(['.yaml', '.yml'])
KNOWN_SUFFIXES = JSON_SUFFIXES | YAML_SUFFIXES


def parser_configured() -> argparse.ArgumentParser:
    """Return the configured argument parser."""
    parser = argparse.ArgumentParser(
        prog=APP_ALIAS,
        description=APP_NAME,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        'source_pos',
        nargs='?',
        metavar='SOURCE_FILE',
        help='JSON or YAML source as positional argument',
    )
    parser.add_argument(
        'target_pos',
        nargs='?',
        metavar='TARGET_FILE',
        help='JSON or YAML target as positional argument',
    )
    parser.add_argument(
        '--source',
        '-s',
        dest='source',
        metavar='FILE',
        help='JSON or YAML source',
    )
    parser.add_argument(
        '--target',
        '-t',
        dest='target',
        metavar='FILE',
        help='JSON or YAML target',
    )
    parser.add_argument(
        '--debug',
        '-d',
        dest='debug',
        default=None,
        action='store_true',
        help=f'work in debug mode (default: False), overwrites any environment variable {APP_ENV}_DEBUG value',
    )
    parser.add_argument(
        '--quiet',
        '-q',
        dest='quiet',
        default=None,
        action='store_true',
        help='work in quiet mode (default: False)',
    )
    parser.add_argument(
        '--version',
        '-V',
        dest='version',
        default=None,
        action='store_true',
        help='display version and exit',
    )

    return parser


def validate_source(
    options: argparse.Namespace, engine: argparse.ArgumentParser
) -> str:
    """Validate the source given."""
    if not (options.source_pos or options.source):
        engine.error(
            'source path must be given - either as first positional argument or as value to the --source option'
        )

    if options.source_pos and options.source:
        engine.error(
            'source path given both as first positional argument and as value to the --source option - pick one'
        )

    if not options.source:
        options.source = options.source_pos

    if not pathlib.Path(options.source).is_file():
        engine.error(f'requested source ({options.source}) is not a file')

    source_suffix = pathlib.Path(options.source).suffix.lower()
    if source_suffix not in KNOWN_SUFFIXES:
        engine.error(
            f'requested source suffix ({source_suffix}) is not in known suffixes ({", ".join(KNOWN_SUFFIXES)})'
        )

    return source_suffix


def validate_target(
    options: argparse.Namespace, engine: argparse.ArgumentParser
) -> str:
    """Validate the target given."""
    if not (options.target_pos or options.target):
        engine.error(
            'target path must be given - either as second positional argument or as value to the --target option'
        )

    if options.target_pos and options.target:
        engine.error(
            'target path given both as second positional argument and as value to the --target option - pick one'
        )

    if not options.target:
        options.target = options.target_pos

    if pathlib.Path(options.target).exists():
        engine.error(
            f'requested target ({options.target}) already exist - remove or request other target'
        )

    target_suffix = pathlib.Path(options.target).suffix.lower()
    if target_suffix not in KNOWN_SUFFIXES:
        engine.error(
            f'requested target suffix ({target_suffix}) is not in known suffixes ({", ".join(KNOWN_SUFFIXES)})'
        )

    return target_suffix


def parse_request(argv: list[str]) -> int | argparse.Namespace:
    """Parse the request vector into validated options."""
    parser = parser_configured()
    if not argv:
        parser.print_help()
        return 0

    options = parser.parse_args(argv)

    if options.version:
        print(VERSION)
        return 0

    # Ensure consistent request for verbosity
    if options.debug and options.quiet:
        parser.error('Cannot be quiet and debug - pick one')

    # Ensure hierarchical setting of debug: command line overwrites environment variable value
    if options.debug is None:
        options.debug = DEBUG

    # Quiet overwrites any debug requests
    if options.quiet:
        options.debug = False

    # Validate and derive the DSL values for source and target formats
    options.source_format = (
        JSON_FORMAT
        if validate_source(options, engine=parser) in JSON_SUFFIXES
        else YAML_FORMAT
    )
    options.target_format = (
        JSON_FORMAT
        if validate_target(options, engine=parser) in JSON_SUFFIXES
        else YAML_FORMAT
    )

    return options


def main(argv: list[str] | None = None) -> int:
    """Delegate processing to functional module."""
    argv = sys.argv[1:] if argv is None else argv
    options = parse_request(argv)
    if isinstance(options, int):
        return 0
    return transform(request=options)
