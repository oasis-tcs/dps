# JADN Install Package

## Organization

* **definitions.py:** Constants that define the JADN language.
* **core.py:** The base JADNCore class. This is inherited by others but not instantiated directly.
* **utils.py:** Miscellaneous utility functions, including translating type definition strings
to/from JADN values.
* **config.py:** Functions for managing command-line configuration options.
* **data/:** The JSON schema and JADN metaschema used to validate all JADN schemas.
* **convert/:** Classes that translate the logical (internal) value of a JADN schema to and from a
literal value of that schema in an external data format. All formats are equivalent,
meaning that conversions among them are lossless.
    * **jadn:** JSON data, the authoritative data format for JADN schemas
    * **jidl:** JADN Information Definition Language, a declarative text specification analogous to source code
    * **xasd:** XML Abstract Schema Definition language, an XML data format for JADN schemas
    * **md:** Markdown tables, a property table format for including JADN schemas in specification documents
    * **atree:** ASCII tree diagram showing dependency relationships between types
    * **erd:** Entity Relationship Diagram, text source for a graphical representation of a JADN schema.
    Two ERD formats are currently supported: Graphviz (.dot) and PlantUML (.puml)
* **translate/:** Classes that translate a JADN schema into a different abstract or concrete schema language.
Translations are lossy to the extent that different languages have different capabilities and concrete schemas
are less flexible than information models, but mechanical translation provides a starting point for refinement.  
Schema languages are:
    * **json:** JSON Schema
    * **xsd:** XML Schema Definition
    * **cddl:** Concise Data Definition Language, the schema specification for IETF CBOR
    * **proto:** Google Protocol Buffers
    * **xeto:** Extensible Explicitly Typed Objects, a schema language developed for the smart buildings industry
* **transform/:** Convert a JADN schema into different JADN schema for various purposes such as:
    * simplifying shortcuts (syntactic sugar) into core definitions 
    * resolving external references between schema packages
