from jadn import JADNCore

"""
Translate JADN abstract schema to Protocol Buffers
"""

class PROTO(JADNCore):
    def style(self) -> dict:
        return {}

    def schema_loads(self, doc: str) -> None:
        print('Protobuf schema load not implemented')
        exit(1)

    def schema_dumps(self, pkg, style: dict = {}) -> str:
        self.SCHEMA = pkg.SCHEMA
        self.SOURCE = pkg.SOURCE
        print('Protobuf schema dump not implemented')
        exit(1)
