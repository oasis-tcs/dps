import os
import json
from copy import deepcopy
from jadn.definitions import OPTS, OPTX, OPTO, BOOL_OPTS, PYTHON_TYPES, CoreType, Fields, FieldType, TypeOptions, FieldOptions
from typing import TextIO, BinaryIO, Any
from numbers import Number


# =========================================================
# Define JADN schema static function here because it's needed for METASCHEMA
# class variable but using JADN class would be an inheritance loop
# METASCHEMA is not validated on load, it must be correct.
# =========================================================
def jadn_schema_loads(self, jadn_str: str) -> dict:
    """
    Load a logical JADN schema from a JSON string.

    For each type definition, fill in defaults and convert options from list of tagged strings to dict.

    :param self: supplied when calling from a class instance, not used
    :param jadn_str: {meta, types} in serialized format
    :return: {meta, types} in logical format
    """
    schema = json.loads(jadn_str)
    tdef = [None, None, [], '', []]  # [TypeName, CoreType, TypeOptions, TypeDesc, Fields]
    for td in schema['types']:
        td += tdef[len(td):len(tdef)]
        td[TypeOptions] = _load_tagstrings(td[TypeOptions], td[CoreType])
        for fd in td[Fields]:
            fdef = [None, None, ''] if td[CoreType] == 'Enumerated' else [None, None, None, [], '']
            fd += fdef[len(fd):len(fdef)]
            if td[CoreType] != 'Enumerated':
                fd[FieldOptions] = _load_tagstrings(fd[FieldOptions], fd[FieldType])
    return schema


def jadn_schema_dumps(self, style: dict = {}) -> str:
    """
    Return a schema instance as a string containing JADN data in JSON format
    """
    schema_copy = {'meta': self.SCHEMA['meta'], 'types': deepcopy(self.SCHEMA['types'])}

    for td in schema_copy['types']:
        td[TypeOptions] = _dump_tagstrings(td[TypeOptions], td[CoreType])
        for fd in td[Fields]:       # TODO: delete default=1 minOccurs/maxOccurs (until instance validation)
            fd[FieldOptions] = _dump_tagstrings(fd[FieldOptions], fd[FieldType])
            fdef = [None, None, ''] if td[CoreType] == 'Enumerated' else [None, None, None, [], '']
            while fd and fd[-1] == fdef[len(fd) - 1]:
                fd.pop()
        tdef = [None, None, [], '', []]
        while td and td[-1] == tdef[len(td) - 1]:   # Don't pop Fields before checking them
            td.pop()
    return _pprint(schema_copy, strip=style.get('strip', True)) + '\n'


# ========================================================
# Support functions
# ========================================================

def _load_tagstrings(tstrings: list[str], ct: str) -> dict[str, str]:
    """
    Convert JSON-serialized TypeOptions and FieldOptions list of strings to dict
    """
    def opt(s: str, ct: str) -> tuple[str, str]:
        t = OPTS[ord(s[0])]
        f = PYTHON_TYPES[ct if t[1] is None else t[1]]
        return s if s[0] in BOOL_OPTS else t[0], '' if s[0] in BOOL_OPTS else True if f is bool else f(s[1:])
    return dict(opt(s, ct) for s in tstrings)


def _dump_tagstrings(opts: dict[str, str], ct: str) -> list[str]:
    """
    Convert TypeOptions and FieldOptions dict to JSON-serialized list of strings
    """
    def strs(k: str, v: Any) -> str:
        v = '' if isinstance(v, bool) else str(v)
        return k if k[0] in BOOL_OPTS else chr(OPTX[k]) + v
    return [strs(k, v) for k, v in sorted(opts.items(),     # Sort options to a canonical order to ease comparison
            key=lambda k: OPTO[k[0]] if k[0][0] not in BOOL_OPTS else OPTO['format'])]


def _pprint(val: Any, level: int = 0, indent: int = 2, strip: bool = False) -> str:
    """
    Prettyprint a JSON-serialized schema in compact format

    :param val: JSON string to be formatted
    :param level: Indentation level, default = 0 for external calls
    :param indent: Number of spaces per level, default = 2
    :param strip: Remove empty lines between types, boolean default = False
    :return: Formatted JSON string
    """
    if isinstance(val, (Number, type(''))):
        return json.dumps(val, ensure_ascii=False)

    sp = level * indent * ' '
    sp2 = (level + 1) * indent * ' '
    sep2 = ',\n' if strip else ',\n\n'
    if isinstance(val, dict):
        sep = ',\n' if level > 0 else sep2
        lines = sep.join(f'{sp2}"{k}": {_pprint(val[k], level + 1, indent, strip)}' for k in val)
        return f'{{\n{lines}\n{sp}}}'
    if isinstance(val, list):
        sep = ',\n' if level > 1 else sep2
        nest = val and isinstance(val[0], list)  # Not an empty list
        if nest:
            vals = [f"{sp2}{_pprint(v, level, indent, strip)}" for v in val]
            spn = level * indent * ' '
            return f"[\n{sep.join(vals)}\n{spn}]"
        vals = [f"{_pprint(v, level + 1, indent, strip)}" for v in val]
        return f"[{', '.join(vals)}]"
    return '???'


# ========================================================
# JADN schema core class
# ========================================================
class JADNCore:
    DATA_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')
    if 'METASCHEMA' not in dir():
        with open(os.path.join(DATA_DIR, 'jadn_v2.0_schema.jadn'), encoding='utf8') as fp:
            METASCHEMA = jadn_schema_loads(None, fp.read())
    SCHEMA = None
    SOURCE = None

    def __init__(self):
        self.validate()     # METASCHEMA

    def style(self) -> dict:
        return {}

    def schema_loads(self, message: str | bytes) -> None:
        print('Schema load not implemented')
        exit(1)

    def schema_load(self, fp: TextIO | BinaryIO) -> None:
        self.SOURCE = fp.name
        self.schema_loads(fp.read())

    def schema_dumps(self, pkg, style: dict = {}) -> str | bytes:
        print('Schema dump not implemented')
        exit(1)

    def schema_dump(self, fp: TextIO | BinaryIO, pkg, style: dict = {}) -> None:
        fp.write(self.schema_dumps(pkg, style))

    def validate(self) -> None:
        """
        Validate a logical schema instance against JADN metaschema
        """
        pass


# =========================================================
# Diagnostics
# =========================================================
from jadn.definitions import TypeName, Fields, FieldID, FieldName, FieldType, ALLOWED_TYPE_OPTIONS

if __name__ == '__main__':
    # Print class constants generated from definitions.py
    # print('OPTS:', len(JADN.OPTS), JADN.OPTS)   # Option {id: (name, type)}
    # print('OPTX:', len(JADN.OPTX), JADN.OPTX)   # Option {name: id}
    # print('OPTO:', len(JADN.OPTO), JADN.OPTO)   # Option sort order

    # Verify that Metaschema option IDs agree with definitions
    for td in JADNCore.METASCHEMA['types']:
        for fd in td[Fields]:
            if fd[FieldName] in OPTX:
                if (a := fd[FieldID]) != (b := OPTX[fd[FieldName]]):
                    print(f'{td[TypeName]}.{fd[FieldName]}: {a} != {b}')

    # Verify Metaschema's allowed options by type
    tdx = {t[TypeName]: t for t in JADNCore.METASCHEMA['types']}
    for to in tdx['TypeOptions'][Fields]:
        td = tdx[to[FieldType]]
        ato = ALLOWED_TYPE_OPTIONS[to[FieldName]]
        atm = [f[FieldName] for f in td[Fields]]
        if set(ato) != set(atm):
            print(f'Option mismatch: {td[TypeName]}: {ato} != {atm}')
        for f in td[Fields]:
            if (fm := f[FieldName]) != (fd := OPTS[f[FieldID]][0]):
                print(f'Option mismatch: {td[TypeName]}: {fm} != {fd}')

    # Test tagged-string serialization
    opts_s = ['=', '#Pasta', 'y2', 'z3.00', 'u3.14159', 'q', '/ipv4', '/d3', 'A', '[0']
    print(f'\n Loaded opts: {opts_s}')
    opts_d = _load_tagstrings(opts_s, 'Number')
    print(f'Logical opts: {opts_d}')
    opts_s2 = _dump_tagstrings(opts_d, 'Number')
    print(f' Dumped opts: {opts_s2}')
    if opts_s2 != opts_s:
        print(' ** Translation mismatch **')