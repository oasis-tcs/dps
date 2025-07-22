"""
Convert JADN to/from JADN Interface Definition Language (JIDL)
"""
import json
import re
from jadn import JADNCore
from jadn.definitions import TypeName, CoreType, TypeOptions, TypeDesc, Fields, ItemID, FieldID, META_ORDER
from jadn.utils import (fielddef2jadn, jadn2fielddef, jadn2typestr, typestr2jadn,
                     cleanup_tagid, raise_error, id_type, etrunc)


# JIDL -> JADN Type regexes
p_tname = r'\s*(\S+)'                   # Type Name
p_assign = r'\s*='                      # Type assignment operator
p_tstr = r'\s*(.*?)\s*\{?'              # Type definition

# JIDL -> JADN Field regexes
p_id = r'\s*(\d+)'  # Field ID
p_fname = r'\s+(\S+)' # Field Name
p_fstr = r'\s*(.*?)'  # Field definition or Enum value
p_range = r'\s*(?:\[([.*\w]+)\]|(optional))?'  # Multiplicity

class JIDL(JADNCore):
    def style(self) -> dict:
        # Return default column positions
        return {
            'meta': 12,     # Width of meta name column
            'id': 4,        # Width of Field Id column
            'name': 16,     # Width of Field Name column
            'type': 35,     # Width of Field Type column
            'desc': 50,     # Fixed-position descriptions - overrides type-dependent default if not None
            'page': None    # Truncate to specified page width if specified
        }

    def schema_loads(self, doc: str | bytes) -> None:
        meta = {}
        types = []
        fields = None
        for line in doc.splitlines():
            if line:
                t, v = _line2jadn(line, types[-1] if types else None)    # Parse a JIDL line
                if t == 'F':
                    fields.append(v)
                elif fields:
                    cleanup_tagid(fields)
                    fields = None
                if t == 'I':
                    meta.update({v[0]: json.loads(v[1])})
                elif t == 'T':
                    types.append(v)
                    fields = types[-1][Fields]
        self.SCHEMA = {'meta': meta, 'types': types}

    def schema_dumps(self, pkg, style: dict = {}) -> str:
        """
        Convert JADN schema to JADN-IDL

        :param dict schema: JADN schema
        :param dict style: Override default column widths if specified
        :return: JADN-IDL text
        :rtype: str
        """
        self.SCHEMA = pkg.SCHEMA
        self.SOURCE = pkg.SOURCE

        w = self.style()
        if style:
            w.update(style)   # Override any specified column widths

        text = ''
        meta = self.SCHEMA.get('meta', {})
        mlist = [k for k in META_ORDER if k in meta]
        for k in mlist + list(set(meta) - set(mlist)):              # Display meta elements in fixed order
            text += f'{k:>{w["meta"]}}: {json.dumps(meta[k])}\n'    # TODO: wrap to page width, continuation-line parser

        wt = w['desc'] if w['desc'] else w['id'] + w['name'] + w['type']
        for td in self.SCHEMA['types']:
            tdef = f'{td[TypeName]} = {jadn2typestr(td[CoreType], td[TypeOptions])}'
            tdesc = ' // ' + td[TypeDesc] if td[TypeDesc] else ''
            text += f'\n{tdef:<{wt}}{tdesc}'[:w['page']].rstrip() + '\n'
            idt = id_type(td)
            for fd in td[Fields] if len(td) > Fields else []:       # TODO: constant-length types
                fname, fdef, fmult, fdesc = jadn2fielddef(fd, td)
                if td[CoreType] == 'Enumerated':
                    fdesc = ' // ' + fdesc if fdesc else ''
                    fs = f'{fd[ItemID]:>{w["id"]}} {fname}'
                    wf = w['id'] + w['name'] + 2
                else:
                    fdef += '' if fmult == '1' \
                        else ' optional' if fmult == '0..1' \
                        else ' [' + fmult + ']'
                    fdesc = ' // ' + fdesc if fdesc else ''
                    wn = 0 if idt else w['name']
                    fs = f'{fd[FieldID]:>{w["id"]}} {fname:<{wn}} {fdef}'
                    wf = w['id'] + w['type'] if idt else wt
                wf = w['desc'] if w['desc'] else wf
                text += etrunc(f'{fs:{wf}}{fdesc}'.rstrip(), w['page']) + '\n'
        return text


# ========================================================
# Support functions
# ========================================================

# Convert JIDL to JADN
def _line2jadn(line: str, tdef: list) -> tuple[str, list]:
    if line.split('//', maxsplit=1)[0].strip():
        p_meta = r'^\s*([-\w]+):\s*(.+?)\s*$'
        if m := re.match(p_meta, line):
            return 'I', [m.group(1), m.group(2)]

        q = re.search(r'"(?:[^"\\]|\\.)+"', line)  # Find quoted string (String pattern option)
        s = q.end() if q else 0
        desc = ''
        if d := re.search(r' //', line[s:]):
            desc = line[s + d.end():].strip()
            line = line[:s + d.start()].strip()

        p_type = fr'^{p_tname}{p_assign}{p_tstr}$'
        if m := re.match(p_type, line):
            btype, topts, fo = typestr2jadn(m.group(2))
            assert fo == {}  # field options MUST not be included in typedefs
            newtype = [m.group(1), btype, topts, desc, []]
            return 'T', newtype

        if tdef:  # looking for fields
            pn = '()' if id_type(tdef) else p_fname
            if tdef[CoreType] == 'Enumerated':  # Parse Enumerated Item
                pattern = fr'^{p_id}{p_fstr}$'
                if m := re.match(pattern, line):
                    return 'F', fielddef2jadn(int(m.group(1)), m.group(2), '', '', desc)
            else:  # Parse Field
                pattern = fr'^{p_id}{pn}{p_fstr}{p_range}$'
                if m := re.match(pattern, line):
                    m_range = '0..1' if m.group(5) else m.group(4)  # Convert 'optional' to range
                    return 'F', fielddef2jadn(int(m.group(1)), m.group(2), m.group(3), m_range if m_range else '',
                                              desc)
        else:
            raise_error(f'JIDL Load - field with no type: {repr(line)}')

    return '', []


# =========================================================
# Diagnostics
# =========================================================
if __name__ == '__main__':
    pass
