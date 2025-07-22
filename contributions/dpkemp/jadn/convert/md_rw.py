import json
import re
from jadn import JADNCore
from jadn.definitions import TypeName, CoreType, TypeOptions, TypeDesc, Fields, ItemID, FieldID, META_ORDER
from jadn.utils import jadn2typestr, typestr2jadn, jadn2fielddef, fielddef2jadn, cleanup_tagid, raise_error


# =========================================================
# Convert JADN type definitions to Markdown tables
# =========================================================
class MD(JADNCore):

    def style(self) -> dict:
        # Return default column positions
        return {
            'pad': True,    # Use one space horizontal padding
            'links': True   # Retain Markdown links: [text](link)
        }

    def schema_loads(self, doc: str) -> None:
        meta = {}       # TODO: parsing state machine for meta followed by types including TypeDesc
        types = []
        fields = None
        for line in doc.splitlines():
            if line:
                t, v = _line2jadn(line, types[-1] if types else None)    # Parse a MARKDOWN line
                if t == 'F':
                    fields.append(v)
                elif fields:
                    cleanup_tagid(fields)
                    fields = None
                elif t == 'M':
                    meta.update({v[0]: json.loads(v[1])})
                elif t == 'T':
                    types.append(v)
                    fields = types[-1][Fields]
                elif t:
                    assert t == 'D', f'Unexpected line {t}: "{v}"'
        self.SCHEMA = {'meta': meta, 'types': types}

    def schema_dumps(self, pkg, style: dict = {}) -> str:
        """
        Convert JADN schema to Markdown Tables
        """
        self.SCHEMA = pkg.SCHEMA
        self.SOURCE = pkg.SOURCE

        text = '```\n'
        meta = self.SCHEMA['meta']
        mlist = [k for k in META_ORDER if k in meta]
        for k in mlist + list(set(meta) - set(mlist)):      # Display meta elements in fixed order
            text += f'{k:>14}: {json.dumps(meta[k])}\n'     # TODO: wrap to width, continuation-line parser
        text += '```\n'

        for td in self.SCHEMA['types']:
            if len(td) > Fields and td[Fields]:
                tdef = f'{td[TypeName]} ({jadn2typestr(td[CoreType], td[TypeOptions])})'
                tdesc = f'\n{td[TypeDesc]}\n' if td[TypeDesc] else ''
                text += f'{tdesc}\n**Type: ' + tdef.replace("*", r"\*") + '**\n'
                idt = td[CoreType] == 'Array' or td[TypeOptions].get('id', False)
                table_type = (0 if td[CoreType] == 'Enumerated' else 2) + (0 if idt else 1)
                table = [
                    [['ID', 'Description']],
                    [['ID', 'Item', 'Description']],
                    [['ID', 'Type', r'\#', 'Description']],
                    [['ID', 'Name', 'Type', r'\#', 'Description']]
                ][table_type]
                for fd in td[Fields]:
                    fname, fdef, fmult, fdesc = jadn2fielddef(fd, td)
                    fdef = fdef.replace('*', r'\*')
                    fmult = fmult.replace('*', r'\*')
                    dsc = fdesc.split('::', maxsplit=2)
                    fdesc = f'**{dsc[0]}** - {dsc[1].strip()}' if len(dsc) == 2 else fdesc
                    if table_type == 0:
                        table.append([str(fd[ItemID]), fdesc])
                    elif table_type == 1:
                        table.append([str(fd[ItemID]), f'**{fname}**', fdesc])
                    elif table_type == 2:
                        table.append([str(fd[FieldID]), fdef, fmult, fdesc])
                    elif table_type == 3:
                        table.append([str(fd[FieldID]), f'**{fname}**', fdef, fmult, fdesc])
            else:
                table = [['Type Name', 'Type Definition', 'Description'],
                         [f'**{td[TypeName]}**', jadn2typestr(td[CoreType], td[TypeOptions]), td[TypeDesc]]]
            text += f'\n{_format_table(table)}\n\n**********\n'
        return text


# ========================================================
# Support functions
# ========================================================
def _format_table(rows: list) -> str:
    cwidth = [len(data.strip()) for data in rows[0]]
    for row in rows[1:]:
        for c in range(len(row)):
            cwidth[c] = max(cwidth[c], len(row[c].strip()))
    hbar = f'|{"|".join(["-" * (c + 2) for c in cwidth])}|'
    cf = f'| {" | ".join(["{:" + str(c) + "}" for c in cwidth])} |'
    return '\n'.join([cf.format(*rows[0])] + [hbar] + [cf.format(*r) for r in rows[1:]])


# MARKDOWN -> JADN Type regexes
p_tname = r'\s*([-$\w]+)'               # Type Name
p_assign = r'\s*='                      # Type assignment operator
p_tstr = r'\s*(.*?)\s*\{?'              # Type definition
p_tdesc = r'(?:\s*\/\/\s*(.*?)\s*)?'    # Optional Type description

# MARKDOWN -> JADN Field regexes
p_id = r'\s*(\d+)'  # Field ID
p_fname = r'\s+([-:$\w]+\/?)?'  # Field Name with dir/ option (colon is deprecated, allow for now)
p_fstr = r'\s*(.*?)'  # Field definition or Enum value
p_range = r'\s*(?:\[([.*\w]+)\]|(optional))?'  # Multiplicity
p_desc = r'\s*(?:\/\/\s*(.*?)\s*)?'  # Field description, including field name if .id option


# Convert MARKDOWN to JADN
def _line2jadn(line: str, tdef: list) -> tuple[str, list]:
    if line.split('//', maxsplit=1)[0].strip("` "): # remove backticks and whitespace
        p_meta = r'^\s*([-\w]+):\s*(.+?)\s*$'
        if m := re.match(p_meta, line):
            return 'M', [m.group(1), m.group(2)]

        p_type = fr'^{p_tname}{p_assign}{p_tstr}{p_tdesc}$'
        if m := re.match(p_type, line):
            btype, topts, fo = typestr2jadn(m.group(2))
            assert fo == []                     # field options MUST not be included in typedefs
            newtype = [m.group(1), btype, topts, m.group(3) if m.group(3) else '', []]
            return 'T', newtype

        if tdef:        # looking for fields
            pn = '()' if (tdef[TypeOptions].get('id', False) or tdef[CoreType] == 'Array') else p_fname
            if tdef[CoreType] == 'Enumerated':      # Parse Enumerated Item
                pattern = fr'^{p_id}{p_fstr}{p_desc}$'
                if m := re.match(pattern, line):
                    return 'F', fielddef2jadn(int(m.group(1)), m.group(2), '', '', m.group(3) if m.group(3) else '')
            else:                                   # Parse Field
                pattern = f'^{p_id}{pn}{p_fstr}{p_range}{p_desc}$'
                if m := re.match(pattern, line):
                    m_range = '0..1' if m.group(5) else m.group(4)        # Convert 'optional' to range
                    fdesc = m.group(6) if m.group(6) else ''
                    return 'F', fielddef2jadn(int(m.group(1)), m.group(2), m.group(3), m_range if m_range else '', fdesc)
        else:
            return 'D', [line]        # Document text (not part of a table)

    return '', []
