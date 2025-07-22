from jadn import JADNCore

"""
Translate JADN abstract schema to/from Concise Data Definition Language (CDDL), a concrete schema for CBOR
"""

class CDDL(JADNCore):
    def style(self) -> dict:
        return {}

    def schema_loads(self, doc: str) -> None:
        print('CDDL load not implemented')
        exit(1)

    def schema_dumps(self, pkg, style: dict = {}) -> str:
        self.SCHEMA = pkg.SCHEMA
        self.SOURCE = pkg.SOURCE
        print('CDDL dump not implemented')
        exit(1)
