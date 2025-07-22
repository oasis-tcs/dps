"""
 JADN Definitions

A JSON Abstract Data Notation (JADN) file contains a list of datatype definitions.  Each type definition
has a specified format - a list of four or five columns depending on whether the type is primitive or
structure: (name, base type, type options, type description [, fields]).

For the enumerated type each field definition is a list of three items: (tag, name, description).

For other structure types (array, choice, map, record) each field definition is a list of five items:
(tag, name, type, field options, field description).
"""

# Datatype Definition columns
TypeName = 0            # Name of the type being defined
CoreType = 1            # Core type of the type being defined
TypeOptions = 2         # An array of zero or more TYPE_OPTIONS
TypeDesc = 3            # A non-normative description of the type
Fields = 4              # List of one or more items or fields

# Enumerated Item Definition columns
ItemID = 0              # Integer item identifier
ItemValue = 1           # String value of the item
ItemDesc = 2            # A non-normative description of the Enumerated item

# Field Definition columns
FieldID = 0             # Integer field identifier
FieldName = 1           # Name or label of the field
FieldType = 2           # Type of the field
FieldOptions = 3        # An array of zero or more FIELD_OPTIONS (and TYPE_OPTIONS if extended)
FieldDesc = 4           # A non-normative description of the field


# Core datatypes
PRIMITIVE_TYPES = (
    'Binary',
    'Boolean',
    'Integer',
    'Number',
    'String',
)

PYTHON_TYPES = {            # Programming language types used to hold instances of Primitive types
    'Binary': bytes,
    'Boolean': bool,
    'Integer': int,
    'Number': float,
    'String': str,
}

COMPOUND_TYPES = (
    'Array',
    'ArrayOf',          # (value_type): instance is a container but definition has no fields
    'Map',
    'MapOf',            # (key_type, value_type): instance is a container but definition has no fields
    'Record',
)

UNION_TYPES = (
    'Enumerated',       # enum option specifies fields derived from a defined type
    'Choice',
)

CORE_TYPES = PRIMITIVE_TYPES + COMPOUND_TYPES + UNION_TYPES

FIELD_LENGTH = {
    'Binary': 0,
    'Boolean': 0,
    'Integer': 0,
    'Number': 0,
    'String': 0,
    'Enumerated': 3,    # 0 if Enumerated type definition contains enum or pointer option
    'Choice': 5,
    'Array': 5,
    'ArrayOf': 0,
    'Map': 5,
    'MapOf': 0,
    'Record': 5,
}


def is_builtin(t: str) -> bool:      # Is a core type
    return t in CORE_TYPES


def has_fields(t: str) -> bool:      # Is a type with fields listed in definition
    return FIELD_LENGTH[t] == 5 if is_builtin(t) else False


# Option "tagged-string" serialization:
#   JADN type definitions have TypeOptions and FieldOptions, each of which is a Map of key:value pairs
#   In JSON serialization, options are represented as a List of ID-value strings where the first character
#   of the string is the Unicode codepoint (ID) of its key; the remaining characters are its value.
#   Option tables list the ID: (key name, value type, canonical sort order) of each option:

TYPE_OPTIONS = {
    0x3d: ('id', 'Boolean', 1),             # '=', Enumerated type and Choice/Map/Record keys are ID not Name
    0x2a: ('vtype', 'String', 2),           # '*', Value type for ArrayOf and MapOf
    0x2b: ('ktype', 'String', 3),           # '+', Key type for MapOf
    0x23: ('enum', 'String', 4),            # '#', enumeration derived from Array/Choice/Map/Record type
    0x3e: ('pointer', 'String', 5),         # '>', enumeration of pointers derived from Array/Choice/Map/Record type
    0x25: ('pattern', 'String', 6),         # '%', regular expression that a string must match
    0x77: ('minExclusive', None, 7),        # 'w', minimum numeric/string value, excluding bound
    0x78: ('maxExclusive', None, 8),        # 'x', maximum numeric/string value, excluding bound
    0x79: ('minInclusive', None, 9),        # 'y', minimum numeric/string value
    0x7a: ('maxInclusive', None, 10),       # 'z', maximum numeric/string value
    0x75: ('default', None, 11),            # 'u', Default value
    0x76: ('const', None, 12),              # 'v', Constant value
    0x7b: ('minLength', 'Integer', 13),     # '{', minimum byte or text string length, collection item count
    0x7d: ('maxLength', 'Integer', 14),     # '}', maximum byte or text string length, collection item count
    0x71: ('unique', 'Boolean', 15),        # 'q', ArrayOf instance must not contain duplicates
    0x73: ('set', 'Boolean', 16),           # 's', ArrayOf instance is unordered and unique (set)
    0x62: ('unordered', 'Boolean', 17),     # 'b', ArrayOf instance is unordered and not unique (bag)
    0x6f: ('sequence', 'Boolean', 18),      # 'o', Map, MapOr or Record instance is ordered and unique (ordered set)
    0x30: ('nillable', 'Boolean', 19),      # '0', Instance may have no value, represented by nil, null, None, etc.
    0x43: ('combine', 'String', 20),        # 'C', Choice instance is a logical combination (anyOf, allOf, oneOf)
    0x2f: ('format', 'String', 21),         # '/', semantic validation keyword, may affect serialization
    0x61: ('abstract', 'Boolean', 22),      # 'a', Inheritance: abstract, non-instantiatable
    0x72: ('restricts', 'String', 23),      # 'r', Inheritance: restriction - subset of referenced type
    0x65: ('extends', 'String', 24),        # 'e', Inheritance: extension - superset of referenced type
    0x66: ('final', 'Boolean', 25),         # 'f', Inheritance: final - cannot have subtype
    0x41: ('attr', 'Boolean', 26)           # 'A', field may be serialized as an attribute of an element
}

FIELD_OPTIONS = {
    0x5b: ('minOccurs', 'Integer', 27),     # '[', min cardinality, default = 1, 0 = field is optional
    0x5d: ('maxOccurs', 'Integer', 28),     # ']', max cardinality, default = 1, <0 = inherited or none, not 1 = array
    0x26: ('tagid', 'Integer', 29),         # '&', field that specifies the type of this field
    0x3c: ('dir', 'String', 30),            # '<', pointer enumeration treats field as a collection
    0x4b: ('key', 'Boolean', 31),           # 'K', field is the primary key for TypeName
    0x4c: ('link', 'Boolean', 32),          # 'L', field is a link (foreign key) to an instance of FieldType
    0x4e: ('not', 'Boolean', 33),           # 'N', field is not an instance of FieldType
}

BOOL_OPTS = {'/', }     # Full-key Boolean options, present=True (e.g., /format)
MAX_DEFAULT = -1            # maxOccurs sentinel value: Upper size limit defaults to JADN or package limit
MAX_UNLIMITED = -2          # maxOccurs sentinel value: Upper size limit does not exist

REQUIRED_TYPE_OPTIONS = {
    'Binary': [],
    'Boolean': [],
    'Integer': [],
    'Number': [],
    'String': [],
    'Enumerated': [],
    'Choice': [],
    'Array': [],
    'ArrayOf': ['vtype'],
    'Map': [],
    'MapOf': ['ktype', 'vtype'],
    'Record': [],
}

ALLOWED_TYPE_OPTIONS_ALL = ['nillable', 'abstract', 'extends', 'restricts', 'final']

ALLOWED_TYPE_OPTIONS = {
    'Binary': ['format', 'minLength', 'maxLength', 'default', 'const', 'attr'],
    'Boolean': ['default', 'const', 'attr'],
    'Integer': ['format', 'minInclusive', 'maxInclusive', 'minExclusive', 'maxExclusive', 'default', 'const', 'attr'],
    'Number': ['format', 'minInclusive', 'maxInclusive', 'minExclusive', 'maxExclusive', 'default', 'const', 'attr'],
    'String': ['format', 'pattern', 'minLength', 'maxLength',
               'minInclusive', 'maxInclusive', 'minExclusive', 'maxExclusive', 'default', 'const', 'attr'],
    'Enumerated': ['id', 'enum', 'pointer', 'attr'],
    'Choice': ['id', 'combine'],
    'Array': ['format', 'minLength', 'maxLength'],
    'ArrayOf': ['vtype', 'minLength', 'maxLength', 'unique', 'set', 'unordered'],
    'Map': ['id', 'minLength', 'maxLength', 'sequence'],
    'MapOf': ['ktype', 'vtype', 'minLength', 'maxLength', 'sequence'],
    'Record': ['minLength', 'maxLength', 'sequence'],
}

# Ensure jsonschema prerequisite packages are installed, e.g., rfc3987 for uri/iri validation
FORMAT_JS_VALIDATE = {      # Semantic validation formats defined by JSON Schema 2019-09 Sec 7.3
    'date-time': 'String',
    'date': 'String',
    'time': 'String',
    'duration': 'String',
    # 'email': 'String',        # jsonschema package has deliberately buggy email - won't be fixed
    'idn-email': 'String',
    # 'hostname': 'String',     # jsonschema package needs bug fix
    'idn-hostname': 'String',
    'ipv4': 'String',           # doesn't allow netmask prefix length
    'ipv6': 'String',           # doesn't allow netmask prefix length
    'uri': 'String',
    'uri-reference': 'String',
    'iri': 'String',
    'iri-reference': 'String',
    # 'uuid': 'String',
    'uri-template': 'String',
    'json-pointer': 'String',
    'relative-json-pointer': 'String',
    'regex': 'String'
}

FORMAT_VALIDATE = {         # Semantic validation formats for information instances
    'email': 'String',          # Use this instead of jsonschema
    'hostname': 'String',       # Use this instead of jsonschema
    'eui': 'Binary',            # IEEE Extended Unique Identifier, 48 bits or 64 bits
    'uuid': 'Binary',           # Use this instead of jsonschema
    'tag-uuid': 'Array',        # Prefixed UUID, e.g., "action-b254a45e-d0d3-4e17-b65a-3002f86ee836"
    'ipv4-addr': 'Binary',      # IPv4 address as specified in RFC 791 Section 3.1
    'ipv6-addr': 'Binary',      # IPv6 address as specified in RFC 8200 Section 3
    'ipv4-net': 'Array',        # Binary IPv4 address and Integer prefix length, RFC 4632 Section 3.1
    'ipv6-net': 'Array',        # Binary IPv6 address and Integer prefix length, RFC 4291 Section 2.3
    'i#': 'Integer',            # #-bit signed integer, range [-2^(#-1) .. 2^(#-1)-1]
    'u#': 'Integer',            # #-bit field or unsigned integer, range = [0 .. 2^#-1]
    'f#': 'Number',             # #-bit float, significand and exponent ranges as defined in IEEE 754
}

FORMAT_SERIALIZE = {        # Data representation formats for one or more serializations
    'eui': 'Binary',            # IEEE EUI, 'hex-byte-colon' text representation, (e.g., 00:1B:44:11:3A:B7)
    'uuid': 'Binary',           # RFC 4122 UUID text representation, (e.g., e81415a7-4c8d-45cd-a658-6b51b7a8f45d)
    'tag-uuid': 'Array',        # UUID with prefixed tag, (e.g., action-e81415a7-4c8d-45cd-a658-6b51b7a8f45d)
    'ipv4-addr': 'Binary',      # IPv4 'dotted-quad' text representation, RFC 2673 Section 3.2
    'ipv6-addr': 'Binary',      # IPv6 text representation, RFC 4291 Section 2.2
    'ipv4-net': 'Array',        # IPv4 Network Address CIDR text string, RFC 4632 Section 3.1
    'ipv6-net': 'Array',        # IPv6 Network Address CIDR text string, RFC 4291 Section 2.3
    'b64': 'Binary',            # Base64url - RFC 4648 Section 5 (default text representation of Binary type)
    'x': 'Binary',              # Hex - base16 - lowercase out, case-folding in
    'X': 'Binary',              # Hex - RFC 4648 Section 8 - uppercase only
    'i#': 'Integer',            # n-bit signed integer, n should be 8*2^N (8, 16, 32, 64, ...)
    'u#': 'Integer',            # n-bit field or unsigned integer
    'd#': 'Integer',            # n-digit fixed precision integer scale = 10^n (1=deci, 2=centi, 3=milli, ...)
    'f#': 'Number',             # n-bit IEEE 754 Float (16=half precision, 32=single, 64=double, 128=quad, ...)
}

VALID_FORMATS = {**FORMAT_JS_VALIDATE, **FORMAT_VALIDATE, **FORMAT_SERIALIZE}

DEFAULT_CONFIG = {          # Configuration values to use if not specified in schema
    '$MaxBinary': 255,          # Maximum number of octets for Binary types
    '$MaxString': 255,          # Maximum number of characters for String types
    '$MaxElements': 255,        # Maximum number of items/properties for container types
    '$Sys': '.',                # System reserved character for TypeName
    '$TypeName': '^[A-Z][-.A-Za-z0-9]{0,63}$',     # Type Name regex, must include $Sys
    '$FieldName': '^[a-z][_A-Za-z0-9]{0,63}$',     # Field Name regex, must exclude $Sys
    '$NSID': '^([A-Za-z][A-Za-z0-9]{0,7})?$',      # Namespace ID regex
    '$TypeRef': '^$'            # Placeholder for derived pattern ($NSID ':')? $TypeName
}

EXTENSIONS = {
    'AnonymousType',            # TYPE_OPTIONS included in FieldOptions
    'Multiplicity',             # maxOccurs other than 1, or minLength other than 0 (optional) or 1 (required)
    'DerivedEnum',              # enum and pointer/dir options, create Enumerated type of fields or JSON Pointers
    'MapOfEnum',                # ktype option specifies an Enumerated type
    'Link',                     # key and link options
}

META_ORDER = ('title', 'package', 'version', 'jadn_version', 'description', 'comments',
              'copyright', 'license', 'namespaces', 'roots', 'config')    # Display order

# Precomputed constants
OPTS = (TYPE_OPTIONS | FIELD_OPTIONS)  # Defined Option table: {id: (name, type, sort_order)}
OPTX = {v[0]: k for k, v in OPTS.items()}  # Generated Option reverse index: {name: id}
OPTO = {v[0]: v[2] for k, v in OPTS.items()}  # Generated canonical option sort order {name: order}
