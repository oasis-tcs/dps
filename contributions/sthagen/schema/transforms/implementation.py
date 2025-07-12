"""Format specific load and dump implementations."""

import json
import pathlib

from ruamel.yaml import YAML

from transforms import ENCODING, ENC_ERRS, PathLike


def json_dump(data: object, path: PathLike, debug: bool = False) -> None:
    """doc"""
    _ = debug and print(f'json_dump(data, path={path}, debug={debug}) called ...')
    with open(path, 'wt', encoding=ENCODING, errors=ENC_ERRS) as target:
        json.dump(data, target, indent=2)


def json_load(path: PathLike, debug: bool = False) -> object:
    """doc"""
    _ = debug and print(f'json_load(path={path}, debug={debug}) called ...')
    with open(path, 'rt', encoding=ENCODING, errors=ENC_ERRS) as source:
        return json.load(source)


def yaml_configured() -> YAML:
    """Return configured YAML processor."""
    yaml = YAML(typ='safe')

    yaml.sort_base_mapping_type_on_output = False  # type: ignore
    yaml.indent(mapping=2, sequence=2, offset=2)
    yaml.width = 150
    yaml.default_flow_style = False

    return yaml


def yaml_dump(data: object, path: PathLike, debug: bool = False) -> None:
    """doc"""
    _ = debug and print(f'yaml_dump(data, path={path}, debug={debug}) called ...')
    yaml = yaml_configured()
    yaml.dump(
        data, pathlib.Path(path)
    )  # upstream requires a target with a write method


def yaml_load(path: PathLike, debug: bool = False) -> object:
    """doc"""
    _ = debug and print(f'yaml_load(path={path}, debug={debug}) called ...')
    yaml = yaml_configured()
    with open(path, 'rt', encoding=ENCODING, errors=ENC_ERRS) as source:
        return yaml.load(source)
