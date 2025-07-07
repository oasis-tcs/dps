{
  "meta": {
    "title": "JADN Metaschema",
    "package": "http://oasis-open.org/openc2/jadn/v2.0/schema",
    "description": "Syntax of a JSON Abstract Data Notation (JADN) package.",
    "license": "CC-BY-4.0",
    "roots": ["Schema"],
    "config": {
      "$FieldName": "^[$A-Za-z][_A-Za-z0-9]{0,63}$"
    }
  },
  "types": [
    ["Schema", "Record", [], "Definition of a JADN package", [
      [1, "meta", "Metadata", ["[0"], "Information about this package"],
      [2, "types", "Type", ["q", "]-1"], "Types defined in this package"]
    ]],
    ["Metadata", "Map", [], "Information about this package", [
      [1, "package", "Namespace", [], "Unique name/version of this package"],
      [2, "version", "String", ["{1", "[0"], "Incrementing version within package"],
      [3, "title", "String", ["{1", "[0"], "Title"],
      [4, "description", "String", ["{1", "[0"], "Description"],
      [5, "comment", "String", ["{1", "[0"], "Comment"],
      [6, "copyright", "String", ["{1", "[0"], "Copyright notice"],
      [7, "license", "String", ["{1", "[0"], "SPDX licenseId of this package"],
      [8, "namespaces", "PrefixNs", ["q", "[0", "]-1"], "Referenced packages"],
      [9, "roots", "TypeName", ["q", "[0", "]-1"], "Roots of the type tree(s) in this package"],
      [10, "config", "Config", ["[0"], "Configuration variables"],
      [11, "jadn_version", "Namespace", ["[0"], "JADN Metaschema package"]
    ]],
    ["PrefixNs", "Array", [], "Prefix corresponding to a namespace IRI", [
      [1, "prefix", "NSID", [], "Namespace prefix string"],
      [2, "namespace", "Namespace", [], "Namespace IRI"]
    ]],
    ["Config", "Map", ["{1"], "Config vars override JADN defaults", [
      [1, "$MaxBinary", "Integer", ["y1", "[0"], "Package max octets, default = 255"],
      [2, "$MaxString", "Integer", ["y1", "[0"], "Package max characters, default = 255"],
      [3, "$MaxElements", "Integer", ["y1", "[0"], "Package max items/properties, default = 255"],
      [4, "$Sys", "String", ["{1", "}1", "[0"], "System character for TypeName, default = '.'"],
      [5, "$TypeName", "String", ["/regex", "[0"], "Default = ^[A-Z][-.A-Za-z0-9]{0,63}$"],
      [6, "$FieldName", "String", ["/regex", "[0"], "Default = ^[a-z][_A-Za-z0-9]{0,63}$"],
      [7, "$NSID", "String", ["/regex", "[0"], "Default = ^([A-Za-z][A-Za-z0-9]{0,7})?$"]
    ]],
    ["Namespace", "String", ["/uri"], "Unique name of a package"],
    ["NSID", "String", ["%$NSID"], "Namespace prefix matching $NSID"],
    ["TypeName", "String", ["%$TypeName"], "Name of a logical type"],
    ["FieldName", "String", ["%$FieldName"], "Name of a field in a structured type"],
    ["TypeRef", "String", [], "Reference to a type, matching ($NSID ':')? $TypeName"],
    ["Type", "Array", [], "", [
      [1, "type_name", "TypeName"],
      [2, "core_type", "Enumerated", ["#JADN-Type"]],
      [3, "type_options", "TypeOptions", ["[0", "&2"]],
      [4, "type_description", "Description", ["[0"]],
      [5, "fields", "JADN-Type", ["[0", "&2"]]
    ]],
    ["JADN-Type", "Choice", [], "", [
      [1, "Binary", "Empty"],
      [2, "Boolean", "Empty"],
      [3, "Integer", "Empty"],
      [4, "Number", "Empty"],
      [5, "String", "Empty"],
      [6, "Enumerated", "Items"],
      [7, "Choice", "Fields"],
      [8, "Array", "Fields"],
      [9, "ArrayOf", "Empty"],
      [10, "Map", "Fields"],
      [11, "MapOf", "Empty"],
      [12, "Record", "Fields"]
    ]],
    ["TypeOptions", "Choice", [], "", [
      [1, "Binary", "BinaryOpts"],
      [2, "Boolean", "BooleanOpts"],
      [3, "Integer", "IntegerOpts"],
      [4, "Number", "NumberOpts"],
      [5, "String", "StringOpts"],
      [6, "Enumerated", "EnumeratedOpts"],
      [7, "Choice", "ChoiceOpts"],
      [8, "Array", "ArrayOpts"],
      [9, "ArrayOf", "ArrayOfOpts"],
      [10, "Map", "MapOpts"],
      [11, "MapOf", "MapOfOpts"],
      [12, "Record", "RecordOpts"]
    ]],
    ["Empty", "Array", ["}0"]],
    ["Items", "ArrayOf", ["*Item"]],
    ["Fields", "ArrayOf", ["*Field"]],
    ["Item", "Array", [], "", [
      [1, "item_id", "FieldID"],
      [2, "item_value", "String", ["[0"]],
      [3, "item_description", "Description", ["[0"]]
    ]],
    ["Field", "Array", [], "", [
      [1, "field_id", "FieldID"],
      [2, "field_name", "FieldName"],
      [3, "field_type", "TypeRef"],
      [4, "field_options", "TypeOptions", ["[0", "&3"]],
      [5, "field_description", "Description", ["[0"]]
    ]],
    ["FieldID", "Integer", ["y0"]],
    ["FieldOptions", "Map", [], "", [
      [91, "minOccurs", "Integer", ["y0", "[0"]],
      [93, "maxOccurs", "Integer", ["y-2", "[0"]],
      [38, "tagId", "Integer", ["[0"]],
      [75, "key", "Boolean", ["[0"]],
      [76, "link", "Boolean", ["[0"]],
      [78, "not", "Boolean", ["[0"]]
    ]],
    ["AllOpts", "Map", [], "", [
      [48, "nillable", "Boolean", ["[0"]],
      [97, "abstract", "Boolean", ["[0"]],
      [101, "extends", "TypeRef", ["[0"]],
      [114, "restricts", "TypeRef", ["[0"]],
      [102, "final", "Boolean", ["[0"]]
    ]],
    ["BinaryOpts", "Map", ["eAllOpts"], "", [
      [47, "format", "ArrayOf", ["*Format", "q", "[0"]],
      [123, "minLength", "Integer", ["[0"]],
      [125, "maxLength", "Integer", ["[0"]],
      [117, "default", "Binary", ["[0"]],
      [118, "const", "Binary", ["[0"]],
      [65, "attr", "Boolean", ["[0"]]
    ]],
    ["BooleanOpts", "Map", ["eAllOpts"], "", [
      [117, "default", "Boolean", ["[0"]],
      [118, "const", "Boolean", ["[0"]],
      [65, "attr", "Boolean", ["[0"]]
    ]],
    ["IntegerOpts", "Map", ["eAllOpts"], "", [
      [47, "format", "ArrayOf", ["*Format", "q", "[0"]],
      [121, "minInclusive", "Integer", ["[0"]],
      [122, "maxInclusive", "Integer", ["[0"]],
      [119, "minExclusive", "Integer", ["[0"]],
      [120, "maxExclusive", "Integer", ["[0"]],
      [117, "default", "Integer", ["[0"]],
      [118, "const", "Integer", ["[0"]],
      [65, "attr", "Boolean", ["[0"]]
    ]],
    ["NumberOpts", "Map", ["eAllOpts"], "", [
      [47, "format", "ArrayOf", ["*Format", "q", "[0"]],
      [121, "minInclusive", "Number", ["[0"]],
      [122, "maxInclusive", "Number", ["[0"]],
      [119, "minExclusive", "Number", ["[0"]],
      [120, "maxExclusive", "Number", ["[0"]],
      [117, "default", "Number", ["[0"]],
      [118, "const", "Number", ["[0"]],
      [65, "attr", "Boolean", ["[0"]]
    ]],
    ["StringOpts", "Map", ["eAllOpts"], "", [
      [47, "format", "ArrayOf", ["*Format", "q", "[0"]],
      [121, "minInclusive", "String", ["[0"]],
      [122, "maxInclusive", "String", ["[0"]],
      [119, "minExclusive", "String", ["[0"]],
      [120, "maxExclusive", "String", ["[0"]],
      [37, "pattern", "String", ["/regex", "[0"]],
      [123, "minLength", "Integer", ["y0", "[0"]],
      [125, "maxLength", "Integer", ["y0", "[0"]],
      [117, "default", "String", ["[0"]],
      [118, "const", "String", ["[0"]],
      [65, "attr", "Boolean", ["[0"]]
    ]],
    ["EnumeratedOpts", "Map", ["eAllOpts"], "", [
      [61, "id", "Boolean", ["[0"]],
      [35, "enum", "TypeRef", ["[0"]],
      [62, "pointer", "TypeRef", ["[0"]],
      [65, "attr", "Boolean", ["[0"]]
    ]],
    ["ChoiceOpts", "Map", ["eAllOpts"], "", [
      [61, "id", "Boolean", ["[0"]],
      [67, "combine", "String", ["{1", "}1", "[0"]]
    ]],
    ["ArrayOpts", "Map", ["eAllOpts"], "", [
      [47, "format", "ArrayOf", ["*Format", "q", "[0"]],
      [123, "minLength", "Integer", ["y0", "[0"]],
      [125, "maxLength", "Integer", ["y0", "[0"]]
    ]],
    ["ArrayOfOpts", "Map", ["eAllOpts"], "", [
      [42, "vtype", "TypeRef"],
      [123, "minLength", "Integer", ["y0", "[0"]],
      [125, "maxLength", "Integer", ["y0", "[0"]],
      [113, "unique", "Boolean", ["[0"]],
      [115, "set", "Boolean", ["[0"]],
      [98, "unordered", "Boolean", ["[0"]]
    ]],
    ["MapOpts", "Map", ["eAllOpts"], "", [
      [61, "id", "Boolean", ["[0"]],
      [123, "minLength", "Integer", ["y0", "[0"]],
      [125, "maxLength", "Integer", ["y0", "[0"]],
      [111, "sequence", "Boolean", ["[0"]]
    ]],
    ["MapOfOpts", "Map", ["eAllOpts"], "", [
      [43, "ktype", "TypeRef"],
      [42, "vtype", "TypeRef"],
      [123, "minLength", "Integer", ["y0", "[0"]],
      [125, "maxLength", "Integer", ["y0", "[0"]],
      [111, "sequence", "Boolean", ["[0"]]
    ]],
    ["RecordOpts", "Map", ["eAllOpts"], "", [
      [123, "minLength", "Integer", ["y0", "[0"]],
      [125, "maxLength", "Integer", ["y0", "[0"]],
      [111, "sequence", "Boolean", ["[0"]]
    ]],
    ["Format", "String", ["%^/[a-zA-Z0-9]{1,16}+$"]],
    ["Description", "String"]
  ]
}
