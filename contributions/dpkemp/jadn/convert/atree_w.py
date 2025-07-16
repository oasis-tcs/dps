from asciitree import LeftAligned
from asciitree.drawing import BoxStyle, BOX_BLANK, BOX_ASCII, BOX_LIGHT, BOX_HEAVY, BOX_DOUBLE

from jadn import JADNCore
from jadn.definitions import TypeName, CoreType, TypeOptions
from jadn.utils import build_deps, jadn2typestr

"""
Translate JADN abstract schema to a tree diagram
"""

class ATREE(JADNCore):
    def style(self) -> dict:
        # Return default column positions
        return {
            'draw': 'light',            # blank, ascii, light, heavy, double
            'detail': 'conceptual',     # conceptual (name), logical (name+type), information (name+type+options)
        }


    def schema_dumps(self, pkg, style: dict = None) -> str:
        """
        Translate JADN schema to ascii tree diagram
        """
        def line(t: str, tx: dict[str, list], detail: str) -> str:
            if ' ' in t:
                tree_col, name = t.rsplit(' ', maxsplit=1)
                name = name.strip('[]')     # remove 'blank' style decoration
                tree_col = tree_col.strip('[]')
                jtype = (f'{name}' if detail == 'conceptual' else
                         f'{name} = {tx[name][CoreType]}' if detail == 'logical' else
                         f'{name} = {jadn2typestr(tx[name][CoreType], tx[name][TypeOptions])}')
                return ' '.join((tree_col, jtype))
            return ''

        self.SCHEMA = pkg.SCHEMA
        self.SOURCE = pkg.SOURCE

        tr = tree_style(style['draw'])
        defs = build_deps(self.SCHEMA)  # Get all type definitions and their dependencies
        refs = set(d for deps in defs.values() for d in deps)   # All referenced types
        roots = set(defs) - refs        # Unreferenced types
        tree = '\n\n'.join([tr(build_tree(defs, root)) for root in roots])
        tx = {} if style['detail'] == 'conceptual' else {k[TypeName]: k for k in self.SCHEMA['types']}
        return '\n'.join([line(t, tx, style['detail']) for t in tree.split('\n')])

# ========================================================
# Support functions
# ========================================================

def build_tree(dependencies: dict[str, list], root: str) -> dict:
    def bt(deps: dict, this: str, seen: set):
        tree = {}
        if this not in seen:
            seen |= {this, }
            if this in deps:
                for dep in deps[this]:
                    tree[dep] = bt(deps, dep, seen)
        return tree

    seen = set()
    return {' ' + root: bt(dependencies, root, seen)}


def tree_style(style: str) -> LeftAligned:
    smap = {
        'blank': BoxStyle(gfx=BOX_BLANK, label_space=0, label_format='[{}]', indent=0),
        'ascii': BoxStyle(gfx=BOX_ASCII),
        'light': BoxStyle(gfx=BOX_LIGHT),
        'heavy': BoxStyle(gfx=BOX_HEAVY),
        'double': BoxStyle(gfx=BOX_DOUBLE)
    }
    return LeftAligned(draw=smap[style])


# =========================================================
# Diagnostics
# =========================================================
if __name__ == '__main__':

    dependencies = {
        'asciitree': ['sometimes', 'just', 'trees', 'in'],
        'sometimes': ['you'],
             'just': ['want'],
             'want': ['to', 'draw'],
               'in': ['your'],
             'your': ['terminal'],
    }

    ts = tree_style('double')
    tree = build_tree(dependencies, 'asciitree')
    print(ts(tree))
