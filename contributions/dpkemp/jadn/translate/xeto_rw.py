from jadn import JADNCore

"""
Translate JADN abstract schema to/from Haystack Extensible Explicitly Typed Objects (Xeto) schema language
"""

class XETO(JADNCore):
    def style(self) -> dict:
        return {}

    def schema_loads(self, doc: str) -> None:
        print('XETO schema load not implemented')
        exit(1)

    def schema_dumps(self, pkg, style: dict = {}) -> str:
        self.SCHEMA = pkg.SCHEMA
        self.SOURCE = pkg.SOURCE
        print('XETO schema dump not implemented')
        exit(1)
