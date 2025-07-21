"""
Translate JADN to XML Abstract Schema Definition (XASD)
"""
from io import BytesIO
from typing import Union
from lxml import etree as ET
from jadn import JADNCore
from jadn.definitions import (TypeName, CoreType, TypeOptions, TypeDesc, Fields, ItemID, ItemValue, ItemDesc,
                              FieldID, FieldName, FieldType, FieldDesc, FieldOptions, PYTHON_TYPES, OPTS, OPTX)


class XASD(JADNCore):
    def style(self) -> dict:
        return {}

    def schema_loads(self, xml_str: str) -> None:
        tree = ET.parse(BytesIO(xml_str.encode('utf8')))
        root = tree.getroot()
        assert root.tag == 'Schema'
        meta = {}
        types = []
        for element in root:
            if element.tag == 'Metadata':
                meta = _get_meta(element)
            elif element.tag == 'Types':
                for el in element:
                    types.append(_get_type(self, el))
        self.SCHEMA = {'meta': meta, 'types': types}

    def schema_dumps(self, pkg, style: dict = None) -> str:
        self.SCHEMA = pkg.SCHEMA
        self.SOURCE = pkg.SOURCE

        def aname(k: str) -> str:   # Mangle "format" attribute names to be valid XML
            return k.replace('/', '_')

        sp = '  '   # Indentation space per level
        xasd = '<?xml version="1.0" encoding="UTF-8"?>\n<Schema>\n'
        if meta := self.SCHEMA['meta']:
            xasd += f'{sp}<Metadata>\n'
            # xasd += '\n'.join([f'{4*" "}{k}="{v}"' for k, v in meta.items() if isinstance(v, str)]) + '>\n'
            for k, v in meta.items():
                if k == 'roots':
                    xasd += f'{2*sp}<{k.capitalize()}>\n'
                    for v in meta[k]:
                        xasd += f'{3*sp}<TypeName>{v}</TypeName>\n'
                    xasd += f'{2*sp}</{k.capitalize()}>\n'
                elif k == 'namespaces':
                    xasd += f'{2*sp}<{k.capitalize()}>\n'
                    for v in meta[k]:
                        xasd += f'{3*sp}<PrefixNs prefix="{v[0]}">{v[1]}</PrefixNs>\n'
                    xasd += f'{2*sp}</{k.capitalize()}>\n'
                elif k == 'config':
                    xasd += f'{2*sp}<{k.capitalize()}>\n'
                    for k2, v in meta[k].items():
                        xasd += f'{3*sp}<{k2.strip("$")}>{v}</{k2.strip("$")}>\n'
                    xasd += f'{2*sp}</{k.capitalize()}>\n'
                else:
                    xasd += f'{2*sp}<{k.capitalize()}>{meta[k]}</{k.capitalize()}>\n'
            xasd += f'{sp}</Metadata>\n'
        xasd += f'{sp}<Types>\n'
        for td in self.SCHEMA['types']:
            (ln, end) = ('\n', 2*sp) if td[Fields] else ('', '')
            to = ''.join([f' {aname(k)}="{v}"' for k, v in td[TypeOptions].items()])
            xasd += f'{2*sp}<Type name="{td[TypeName]}" type="{td[CoreType]}"{to}>{td[TypeDesc]}{ln}'
            for fd in td[Fields]:
                if td[CoreType] == 'Enumerated':
                    xasd += f'{3*sp}<Item id="{fd[ItemID]}" value="{fd[ItemValue]}">{fd[ItemDesc]}</Item>\n'
                else:
                    fo = ''.join([f' {aname(k)}="{v}"' for k, v in fd[FieldOptions].items()])
                    xasd += f'{3*sp}<Field fid="{fd[FieldID]}" name="{fd[FieldName]}" type="{fd[FieldType]}"{fo}>{fd[FieldDesc]}</Field>\n'
            xasd += f'{end}</Type>\n'
        xasd += f'{sp}</Types>\n'
        xasd += '</Schema>\n'
        return xasd

# ========================================================
# Support functions
# ========================================================

def _get_meta(el: ET.Element) -> dict:
    meta = {k: v for k, v in el.items()}
    for e in el:
        if e.tag == 'Roots':
            meta['roots'] = [v.text for v in e]
        elif e.tag == 'Namespaces':
            meta['namespaces'] = [[v.get('prefix'), v.text] for v in e]
        elif e.tag == 'Config':
            meta['config'] = {'$' + v.tag: v.text for v in e}
        else:
            meta[e.tag.lower()] = e.text
    return meta


def _get_type(self, e: ET.Element) -> list:
    def aname(k: str) -> str:   # un-mangle XML attribute name to /format
        return k.replace('_', '/')

    def atype(k: str, v: str, t: str) -> Union[bool, int, float, str]:
        if k not in OPTX:
            return v
        atype = x[1] if (x := OPTS[OPTX[k]]) else t
        return PYTHON_TYPES[atype if atype else t](v)

    def gettext(el: ET.Element) -> str:
        return el.text.strip() if el.text is not None else ''

    assert e.tag == 'Type'
    at = {aname(k): atype(k, v, e.get('type', '')) for k, v in e.items()}
    fields = []
    for f in e:
        fa = {aname(k): atype(k, v, f.get('type', '')) for k, v in f.items()}
        if f.tag == 'Field':
            fields.append([int(fa.pop('fid')), fa.pop('name'), fa.pop('type'), fa, gettext(f)])
        elif f.tag == 'Item':
            fields.append([int(fa.pop('fid')), fa.pop('value'), gettext(f)])

    type = [at.pop('name'), at.pop('type'), at, gettext(e), fields]
    return type


# =========================================================
# Diagnostics
# =========================================================
if __name__ == '__main__':
    pass
