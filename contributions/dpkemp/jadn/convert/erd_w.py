import re
from jadn import JADNCore
from jadn.definitions import (PRIMITIVE_TYPES, TypeName, CoreType, TypeOptions, Fields,
                              FieldID, FieldName, FieldType, FieldOptions)
from jadn.utils import jadn2typestr, jadn2fielddef, multiplicity_str


# =========================================================
# Convert JADN schema to Entity Relationship Diagram
# =========================================================
class ERD(JADNCore):

    def style(self) -> dict:
        # Return diagram appearance options
        return {
            'graph': 'plantuml',        # diagram language: graphviz, plantuml
            'detail': 'conceptual',     # Level of detail: conceptual, logical, information
            'links': True,              # Show link edges (dashed)
            'link_horizontal': True,    # Use e-w links vs. n-s containers
            'edge_label': True,         # Show field name on edges
            'edge_mult': True,          # Show multiplicity on edges
            'attributes': False,        # Show node attributes connected to entities (ellipse)
            'attr_color': 'palegreen',  # Attribute ellipse fill color
            'enums': 10,                # Show Enumerated items with max count (0: none)
            'header': {
                'plantuml': [
                    '\' !theme spacelab',
                    'hide empty members',
                    'hide circle'
                ],
                'graphviz': [
                    'graph [fontname=Arial, fontsize=12];',
                    'node [fontname=Arial, fontsize=8, shape=plain, style=filled, fillcolor=lightskyblue1];',
                    'edge [fontname=Arial, fontsize=7, arrowsize=0.5, labelangle=45.0, labeldistance=0.9];',
                    'bgcolor="transparent";'
                ]
            }
        }

    def schema_dumps(self, pkg, style: dict = {}) -> str:
        """
        Convert JADN schema to Entity Relationship Diagram source file
        """
        def node_leaf(td, bt) -> str:
            """
            Return Leaf Type Definition in selected diagram language
            """
            # nodes and s are available in caller scope
            tn = td[TypeName]
            return {
                'graphviz': f'n{nodes[tn]} [label=<<b>{tn}{bt}</b>>, '
                            f'shape=ellipse, style=filled, fillcolor={s["attr_color"]}]\n\n',
                'plantuml': f'class "{tn}{bt}" as n{nodes[tn]}\n'
            }[s['graph']]

        def node_start(td, bt) -> str:
            """
            Return start of Compound Type Definition in selected diagram language
            """
            # nodes and s are available in caller scope
            tn = td[TypeName]
            color = f'fillcolor={s["attr_color"]}, ' if td[CoreType] == 'Enumerated' else ''
            hr = '<hr/>' if s['detail'] in {'logical', 'information'} and td[Fields] else ''
            return {
                'plantuml': f'class "{tn}{bt}" as n{nodes[tn]}\n',
                'graphviz': f'n{nodes[tn]} [{color}label=<<table cellborder="0" cellpadding="1" cellspacing="0">\n'
                            f'<tr><td cellpadding="4"><b>  {tn}{bt}  </b></td></tr>{hr}\n'
            }[s['graph']]

        def node_field(td, fd) -> str:
            """
            Return Field Definition in selected diagram language
            """
            # nodes and s are available in caller scope
            if s['detail'] == 'conceptual':
                return ''
            elif s['detail'] == 'logical':
                fval = fd[FieldName]
            elif s['detail'] == 'information':
                fl = '{field} ' if s['language'] == 'plantuml' else ''    # override PlantUML parsing parens as methods
                fname, fdef, fmult, fdesc = jadn2fielddef(fd, td)
                fdef += '' if fmult == '1' else ' [' + fmult + ']'
                fval = f'{fd[FieldID]} {fname}' + ('' if td[CoreType] == 'Enumerated' else f' : {fl}{fdef}')
            return {
                'plantuml': f'  n{nodes[td[TypeName]]} : {fval}\n',
                'graphviz': f'  <tr><td align="left">  {fval}  </td></tr>\n'
            }[s['graph']]

        def node_end() -> str:
            """
            Return end of Compound Type Definition
            """
            # nodes and s are available in caller scope
            return {
                'plantuml': '\n',
                'graphviz': '</table>>]\n\n'
            }[s['graph']]

        def edge_type(td) -> str:
            """
            Return graph edges from type options in selected diagram language
            """
            topts = td[TypeOptions]
            k, v = topts.get('ktype', None), topts.get('vtype', None)
            edge = edge_field(td, [0, 'key', k, {}, '']) if k else ''
            edge += edge_field(td, [0, 'value', v, {}, '']) if v else ''
            return edge

        def edge_field(td, fd) -> str:
            """
            Return graph edges from fields in selected diagram language
            """
            # Normalize edge label for diagram language
            def ename(edge_label: str) -> str:
                return edge_label.replace('-', '_')

            # nodes and s are available in caller scope
            if td[CoreType] == 'Enumerated':
                return ''
            fopts = fd[FieldOptions]
            fieldtype = fopts['vtype'] if fd[FieldType] in {'ArrayOf', 'MapOf'} else fd[FieldType]
            if fieldtype in nodes:      # TODO: include ktype
                mult_f = multiplicity_str(fopts)
                mult_r = '1'
                if s['graph'] == 'plantuml':
                    rel = ('.' if 'link_horizontal' in s else '..') if 'link' in fopts else '--'
                    elabel = ' : ' + fd[FieldName] if s['edge_label'] else ''
                    mult = f'"{mult_r}" {rel}> "{mult_f}"' if s['edge_mult'] else f'{rel}>'
                    return f'  n{nodes[td[TypeName]]} {mult} n{nodes[fieldtype]}{elabel}\n'
                elif s['graph'] == 'graphviz':
                    edge = [f'label={ename(fd[FieldName])}'] if s['edge_label'] else []
                    edge += ['style="dashed"'] if 'link' in fopts else []
                    edge += [f'headlabel="{mult_f}", taillabel="{mult_r}"'] if s['edge_mult'] else []
                    edge_label = f' [{", ".join(edge)}]' if edge else ''
                    return f'  n{nodes[td[TypeName]]} -> n{nodes[fieldtype]}{edge_label}\n'
            return ''

        self.SCHEMA = pkg.SCHEMA
        self.SOURCE = pkg.SOURCE

        s = self.style()
        s.update(style)
        assert s['graph'] in {'plantuml', 'graphviz'}, f'Invalid graph language: {s["graph"]}'
        assert s['detail'] in {'conceptual', 'logical', 'information'}, f'Invalid detail: {s["detail"]}'
        fmt = {
            'plantuml': {
                'comment': "'",
                'start': '@startuml',
                'end': '@enduml',
                'header': s['header']['plantuml']
            },
            'graphviz': {
                'comment': '#',
                'start': 'digraph G {',
                'end': '}',
                'header': s['header']['graphviz']
            }
        }[s['graph']]

        text = ''
        for k, v in self.SCHEMA.get('meta', {}).items():
            text += f"{fmt['comment']} {k}: {v}\n"
        text += f"\n{fmt['start']}\n  " + '\n  '.join(fmt['header']) + '\n\n'

        hide_types = [] if s['attributes'] else (*PRIMITIVE_TYPES, 'Enumerated')
        nodes = {tdef[TypeName]: k for k, tdef in enumerate(self.SCHEMA['types']) if tdef[CoreType] not in hide_types}
        edges = ''
        for td in self.SCHEMA['types']:
            if (td[TypeName]) in nodes:
                bt = f' : {jadn2typestr(td[CoreType], td[TypeOptions])}' if s['detail'] == 'information' else ''
                if td[CoreType] in PRIMITIVE_TYPES:
                    text += node_leaf(td, bt)
                else:
                    text += node_start(td, bt)
                    edges += edge_type(td)
                    for fd in td[Fields]:
                        text += node_field(td, fd)
                        edges += edge_field(td, fd)
                    text += node_end()
        return text + edges + fmt['end']


# ========================================================
# Support functions
# ========================================================

# Wrap typenames at word boundaries to minimize node width, using a max of "lines" lines.
def wrapstr(ss: str, lines: int = 3) -> str:
    p = 0
    bp = len(ss)/lines
    wrapped = ''
    for m in re.findall(r'([A-Z][a-z0-9]+)|([A-Z]+)|([a-z]+)', ss):  # TODO: update regex to support more word formats
        w = ''.join(m)
        if p > 0 and p + len(w)/2 > bp:
            wrapped += '\\n'
            bp += len(ss)/lines
        wrapped += w
        p += len(w)
    return wrapped
