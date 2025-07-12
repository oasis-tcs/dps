"""Transforms API for opinionated JSON and YAML rewriting."""

import argparse

from transforms.implementation import json_dump, json_load, yaml_dump, yaml_load
from transforms import JSON_FORMAT


def transform(request: argparse.Namespace) -> int:
    """Transform between and within the known formats."""
    debug = request.debug
    _ = debug and print('Debug mode requested.')

    load = json_load if request.source_format == JSON_FORMAT else yaml_load
    dump = json_dump if request.target_format == JSON_FORMAT else yaml_dump

    _ = debug and print(
        f'Requested transform from {request.source_format} to {request.target_format}'
    )
    data = load(request.source, debug)

    dump(data, request.target, debug)

    return 0
