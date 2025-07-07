import os
from jadn.core import JADNCore, jadn_schema_loads, jadn_schema_dumps

# =========================================================
# JADN-format methods
# schema_load function is defined in jadn.core in order to initialize METASCHEMA class variable
# =========================================================
class JADN(JADNCore):
    def style(self) -> dict:
        return {
            'strip': True
        }

    def schema_loads(self, jadn_str: str) -> None:
        schema = jadn_schema_loads(self, jadn_str)
        self.SCHEMA = schema

    def schema_dumps(self, pkg, style: dict = {}) -> str:
        self.SCHEMA = pkg.SCHEMA
        self.SOURCE = pkg.SOURCE
        return jadn_schema_dumps(self, style)


# =========================================================
# Diagnostics
# =========================================================
if __name__ == '__main__':
    pkg = JADN()

    with open(os.path.join(pkg.DATA_DIR, 'jadn_v2.0_schema.jadn')) as fp:
        pkg.schema_load(fp)
    print(f'\nSchema package: {pkg.package}')
    print(f'\nIM Schema - Logical value:\n{pkg.schema}')           # Internal (logical) schema value
    print(f'\nIM Schema - JSON value:\n{pkg.schema_dumps()}')       # External (lexical) schema value