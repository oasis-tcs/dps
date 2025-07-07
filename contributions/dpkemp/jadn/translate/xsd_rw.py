from collections import defaultdict
from io import BytesIO
from lxml import etree
from jadn import JADNCore

"""
Translate JADN abstract schema to XML schema definition (XSD)
"""

class XSD(JADNCore):

    def style(self) -> dict:
        return {}

    def schema_loads(self, xml_str: str) -> None:
        tree = etree.parse(BytesIO(xml_str.encode('utf8')))
        root = tree.getroot()
        tag = etree.QName(root.tag).localname
        attrs = {k: v for k, v in root.items()}

        meta = {}
        meta['package'] = attrs['targetNamespace']
        meta['version'] = attrs['version']
        meta['roots'] = [tag.capitalize()]
        meta['namespaces'] = [(k, v) for k, v in root.nsmap.items()]

        types = make_jadn(root)
        self.SCHEMA = {'meta': meta, 'types': types}

    def schema_dumps(self, pkg, style: dict = {}) -> str:
        self.SCHEMA = pkg.SCHEMA
        self.SOURCE = pkg.SOURCE
        print('XSD dump not implemented')
        exit(1)

# ========================================================
# Support functions
# ========================================================

def make_jadn(root: etree.Element) -> dict:

    def walk(path: list, ctx: dict, n: int) -> None:
        e = path[-1]
        ctx['e_count']['.'.join([etree.QName(v).localname for v in path])] += 1
        s = {
            'tag': etree.QName(e.tag),
            'attrs': {k: v for k, v in e.items()},
            'val': f'{e.text.strip() if e.text else ""}',
            'documentation': [],
            'fields': [],
        }
        print(f'{n:>{2*len(path)}} {len(e)} {s["tag"]} {s["attrs"]} {s["val"]}')
        for n, child in enumerate(path[-1], start=1):
            walk(path + [child], ctx, n)
        process(ctx, s)

    ctx = {
        'meta': {},
        'types': [],
        'e_count': defaultdict(int),
    }
    walk([root], ctx, 1)
    for n, (k, v) in enumerate(ctx['e_count'].items(), start=1):
        print(f'{n:=4} {k} = {v}')
    return {k: ctx[k] for k in ('meta', 'types')}


def process(ctx, s):
    def p_schema(ctx, s):
        print('## Schema')

    def p_annotation(ctx, s):
        print('## Annotation')

    def p_list(ctx, s):
        print('## List')

    def p_documentation(ctx, s):
        print('## Documentation')

    def p_localterm(ctx, s):
        print('## LocalTerm')

    def p_appinfo(ctx, s):
        print('## Appinfo')

    def p_import(ctx, s):
        print('## Import')

    def p_attribute(ctx, s):
        print('## Attribute')

    def p_element(ctx, s):
        print('## Element')

    def p_simpleType(ctx, s):
        print('## SimpleType')

    def p_simpleContent(ctx, s):
        print('## SimpleContent')

    def p_complexType(ctx, s):
        print('## ComplexType')

    def p_complexContent(ctx, s):
        print('## ComplexContent')

    def p_extension(ctx, s):
        print('## Extension')

    def p_attributeGroup(ctx, s):
        print('## AttributeGroup')

    def p_restriction(ctx, s):
        print('## Restriction')

    def p_enumeration(ctx, s):
        print('## Enumeration')

    def p_sequence(ctx, s):
        print('## Sequence')

    def p_option(ctx, s):
        print('## Option')

    p = {
        'schema': p_schema,
        'annotation': p_annotation,
        'list': p_list,
        'documentation': p_documentation,
        'LocalTerm': p_localterm,
        'appinfo': p_appinfo,
        'import': p_import,
        'attribute': p_attribute,
        'element': p_element,
        'simpleType': p_simpleType,
        'simpleContent': p_simpleContent,
        'complexType': p_complexType,
        'complexContent': p_complexContent,
        'extension': p_extension,
        'attributeGroup': p_attributeGroup,
        'restriction': p_restriction,
        'enumeration': p_enumeration,
        'sequence': p_sequence,
        'minInclusive': p_option,
        'maxInclusive': p_option,
        'minExclusive': p_option,
        'maxExclusive': p_option,
        'pattern': p_option
    }

    p[s['tag'].localname](ctx, s)
