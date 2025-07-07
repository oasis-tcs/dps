import json
import os
from jadn import JADNCore
from jadn.definitions import TypeName, is_builtin
from jadn.utils import raise_error

"""
Translate JADN abstract schema to/from JSON schema
"""

class JSCHEMA(JADNCore):
    def style(self) -> dict:
        # Return default column positions
        return {
            'size': 'verbose',      # verbose: Record -> object, property/enum -> name
                                    # compact: Record -> array,  property/enum -> name
                                    # concise: Record -> array,  property/enum -> id
            'enum': 'enum',         # const: generate oneOf keyword with const for each item
                                    #  enum: generate an enum keyword containing all items
                                    # regex: generate a regular expression that matches each item
            'typenames': 'named',   # name: types are named in $defs
                                    # anon: types are nested anonymously and repeated
        }

    def schema_loads(self, doc: str) -> None:
        jss = json.loads(doc)
        # assert jss['type'] == 'object', f'Unsupported JSON Schema format'
        defs = jss.get('definitions', jss.get('$defs', {}))
        jssx = {v.get('$id', k): k for k, v in defs.items()}  # Index from $id to definition
        types = {typedefname(k, jss): v for k, v in defs.items()}  # Index from type name to definition
        assert len(types) == len(set(types)), f'Type name collision'

        p = os.path.splitext(pkg := jss.get('$id', ''))
        meta = {'package': (p[0] + '/' if p[-1] in ('.json', '.xsd', '.html') else pkg)}
        meta.update({'jadn_version': 'http://oasis-open.org/openc2/jadn/v2.0/schema/'})
        meta.update({'title': jss['title']} if 'title' in jss else {})
        meta.update({'description': jss['description']} if 'description' in jss else {})
        meta.update({'$comment': jss['$comment']} if '$comment' in jss else {})
        meta.update({'roots': ['Root']})
        meta.update({'config': {
            '$MaxString': 1000,
            '$TypeName': '^[a-zA-Z][-._A-Za-z0-9]{0,63}$',
            '$FieldName': '^[$a-z][-_$A-Za-z0-9]{0,63}$'}})

        nt = []  # Walk nested type definition tree to build type list
        scandef('Root', jss, nt, jss, jssx)
        for tn, tv in defs.items():
            scandef(tn, tv, nt, jss, jssx)

        ntypes = []  # Prune identical type definitions
        for t in nt:
            if t not in ntypes:  # O(n^2) runtime because type definitions aren't hashable
                ntypes.append(t)  # Convert to immutable types if it becomes an issue

        self.SCHEMA = {'meta': meta, 'types': ntypes}

    def schema_dumps(self, pkg, style: dict = {}) -> str:
        """
        Translate JADN schema to/from jschema
        """
        self.SCHEMA = pkg.SCHEMA
        self.SOURCE = pkg.SOURCE
        print('JSON Schema dump not implemented')
        exit(1)


# ========================================================
# Support functions
# ========================================================

def scandef(tn: str, tv: dict, nt: list, jss: dict, jssx: dict):
    """
    Process anonymous type definitions, generate pathname, add to list nt
    """

    if not (td := define_jadn_type(tn, tv, jss, jssx)):
        return
    nt.append(td)
    if tv.get('type', '') == 'object':
        for k, v in tv.get('properties', {}).items():
            if v.get('$ref', '') or v.get('type', '') in ('string', 'number', 'integer', 'boolean'):     # Not nested
                pass
            elif v.get('type', '') == 'object':
                scandef(maketypename(tn, k, jss), v, nt, jss, jssx)
            elif v.get('type', '') == 'array':
                scandef(maketypename('', k, jss), v, nt, jss, jssx)
                if len(vt := v.get('items', {})) != 1 or vt.get('type', '') not in ('string', 'number', 'integer', 'boolean'):
                    scandef(maketypename('', k, jss) + '-item', v['items'], nt, jss, jssx)
            elif v.get('anyOf', '') or v.get('allOf', ''):
                scandef(maketypename(tn, k, jss), v, nt, jss, jssx)
            elif typerefname(v, jss, jssx):
                print('  nested property type:', f'{td[TypeName]}.{k}', v)

        if not tn:
            print(f'  nested type: "{tv.get("title", "")}"')
    elif (tc := tv.get('anyOf', '')) or (tc := tv.get('allOf', '')):
        for n, v in enumerate(tc, start=1):
            scandef(maketypename(tn, n, jss), v, nt, jss, jssx)
    pass


def define_jadn_type(tn: str, tv: dict, jss: dict, jssx: dict) -> list:
    omap = {'minItems': 'minLength', 'maxItems': 'maxLength'}   # Map JSON Schema options to JADN options
    topts = {}
    tdesc = tv.get('description', '')
    fields = []
    if (jstype := tv.get('type', '')) == 'object':
        coretype = 'Record'
        req = tv.get('required', [])
        for n, (k, v) in enumerate(tv.get('properties', {}).items(), start=1):
            fopts = {'minOccurs': 0} if k not in req else {}
            fdesc = v.get('description', '')
            if v.get('type', '') == 'array':
                ftype = maketypename('', k, jss)
                idesc = jss.get('definitions', {}).get(jssx.get(v['items'].get('$ref', ''), ''), {}).get('description', '')
                fdesc = fdesc if fdesc else v['items'].get('description', idesc)
            elif v.get('type', '') == 'object':
                ftype = maketypename(tn, k, jss)
            elif ref := v.get('$ref', ''):
                if len(r := ref.split('/')) == 3:
                    if r[1] in jss:
                        ftype = r[2]
                elif ref == '#':  # TODO: replace this monkey hack with proper reference logic
                    ftype = tn
            elif t := jssx.get(v.get('$ref', ''), ''):
                rt = jss['definitions'][t].get('$ref', '')
                ftype = typedefname(rt if rt else t, jss)
                ft = jss['definitions'][t]
                fdesc = ft.get('description', '')
            elif v.get('anyOf', '') or v.get('allOf', ''):
                ftype = maketypename(tn, k, jss)
            else:
                ftype = typerefname(v, jss, jssx)
            fdef = [n, k, ftype, fopts, fdesc]
            if not ftype:
                raise ValueError(f'  empty field type {tn}.{k}')
            fields.append(fdef)
    elif (td := tv.get('anyOf', '')) or (td := tv.get('allOf', '')):
        coretype = 'Choice'
        # topts = ['<', '∪'] if 'allOf' in tv else ['<']    # TODO: update Choice in JADN library
        # topts = ['∪'] if 'allOf' in tv else []
        for n, v in enumerate(td, start=1):
            fd = typerefname(v, jss)
            ftype = fd if fd else maketypename(tn, n, jss)
            fdef = [n, f'c{n}', ftype, [], '']
            fields.append(fdef)
    elif td := tv.get('enum', ''):
        coretype = 'Enumerated'
        for n, v in enumerate(td, start=1):
            fields.append([n, v, ''])
    elif jstype == 'array':
        if itype := tv.get('items', {}):
            coretype = 'ArrayOf'
            topts = {omap[k]: v for k, v in tv.items() if k in ('minItems', 'maxItems')}
            ref = jss.get('definitions', {}).get(jssx.get(itype.get('$ref', ''), ''), {})
            tr = typerefname(ref, jss, jssx)
            tr = tr if tr else typerefname(itype, jss, jssx)
            tr = tr if tr else tn + '-item'
            topts |= {'vtype': tr}
        else:
            coretype = 'Array'      # TODO: process individual items
            raise_error(f'Array type not yet supported: {tv}')
    elif jstype in ('string', 'integer', 'number', 'boolean'):
        if p := tv.get('pattern', ''):
            topts.append(f'%{p}')
        coretype = jstype.capitalize()
    else:
        return []

    return [typedefname(tn, jss), coretype, topts, tdesc, fields]


def typedefname(jsdef: str, jss: dict) -> str:
    """
    Infer type name from a JSON Schema definition
    """
    assert isinstance(jsdef, str), f'Not a type definition name: {jsdef}'
    if d := jss.get('definitions', jss.get(jsdef, '')):
        if ':' in jsdef:  # qualified definition name
            return maketypename('', jsdef.split(':', maxsplit=1)[1], jss)
        if ref := d.get('$ref', ''):
            return ref.removeprefix('#/definitions/')
    return jsdef.removeprefix('#/definitions/')     # Exact type name or none


def typerefname(jsref: dict, jss: dict, jssx: dict) -> str:
    """
    Infer a type name from a JSON Schema property reference
    """
    if (t := jsref.get('type', '')) in ('string', 'integer', 'number', 'boolean'):
        return t.capitalize()    # Built-in type
    if ref := jsref.get('$ref', ''):
        td = jssx.get(ref, ref)
        if td.startswith('#/definitions/'):  # Exact type name
            return td.removeprefix('#/definitions/')
        if ':' in td:
            return maketypename('', td.split(':', maxsplit=1)[1], jss)  # Extract type name from $id
        if td2 := jss.get('definitions', {}).get(td, {}):
            return typerefname(td2, jss)
    return ''


def maketypename(tn: str, name: str, jss) -> str:
    """
    Convert a type and property name to type name
    """
    tn = typedefname(tn, jss)
    name = f'{tn}.{name}' if tn else name.capitalize()      # $Sys = "."
    return name + '1' if is_builtin(name) else name
