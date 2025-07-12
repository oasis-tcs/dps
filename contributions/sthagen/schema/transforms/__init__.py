"""Transforms helper tool."""

import os
import pathlib

__version__ = '2025.7.12'
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0]
    for part in __version__.split('+')
    for e in part.split('.')
    if e != 'parent'
)
__all__: list[str] = [
    'APP_ALIAS',
    'APP_NAME',
    'DEBUG',
    'ENCODING',
    'ENC_ERRS',
    'JSON_FORMAT',
    'PathLike',
    'VERSION',
    'VERSION_INFO',
    'YAML_FORMAT',
]

APP_ALIAS = str(pathlib.Path(__file__).parent.name)
APP_ENV = APP_ALIAS.upper()
APP_NAME = locals()['__doc__']

DEBUG = bool(os.getenv(f'{APP_ENV}_DEBUG', ''))

ENCODING = 'utf-8'
ENC_ERRS = 'ignore'

JSON_FORMAT = 'json'
YAML_FORMAT = 'yaml'

PathLike = pathlib.Path | str
VERSION = __version__
VERSION_INFO = __version_info__
