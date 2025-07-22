from jadn import JADNCore

"""
Template for creating a new JADNCore class for new schema format <foo>
"""

class FOO(JADNCore):

    def style(self) -> dict:
        # Return all output style options for <foo> with default values
        return {
            'option1': 'sanitize',
            'option2': 42
        }

    def schema_loads(self, doc: str) -> None:
        meta = {}   # Initialize JADN schema
        types = []

        #
        # Convert a text or binary schema in format "foo" to JADN schema
        #  ...

        self.SCHEMA = {'meta': meta, 'types': types}    # Save the schema to input class variable

    def schema_dumps(self, pkg, style: dict = {}) -> str:
        self.SCHEMA = pkg.SCHEMA    # Copy the source JADN schema to output class variable
        self.SOURCE = pkg.SOURCE    # SOURCE filename is populated by schema_load(), copy to output class

        foo = ''    # or foo = b''

        #
        # Convert JADN schema to text or binary format <foo>
        #  ...

        return foo      # Return string or bytes to be saved to file by schema_dump()