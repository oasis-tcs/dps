# Provenance Information Model Encoding {#provenance-information-model-encoding}

This specification defines the Data Provenance Metadata format by one normative artifact and views derived from it:

JSON schema
:   The Data Provenance Metadata JSON schema (`json/data-provenance.json`) is the normative definition of the format.
    It decides which documents are valid, and it carries the description of every member.

YAML outlines
:   The outlines in section [sec](#provenance-data-model-encoding) show where each member sits in a document,
    whether it is required, and its type, in a compact notation generated from the JSON schema.

Property tables
:   The tables in section [sec](#provenance-schema) give, for each type, its members with their type, cardinality, and description.
    They are generated from the JADN encoding of the information model (section [sec](#jadn-encoding)), which in turn is generated from the JSON schema.

The information model is also available in the following two informative encodings, both generated from the JSON schema.
The JSON encoding (section [sec](#json-encoding)) is the only normative one.

## JADN Encoding {#jadn-encoding}

The JADN encoding of the data provenance metadata information model is provided in
`jadn/data-provenance.jadn`.

The file is generated from the JSON schema.
Each schema node that defines a type carries the JADN type name in the annotation `x-jadn-type`,
and each enumeration carries the descriptions of its values in the annotation `x-jadn-enum`;
the descriptions of the fields are the `description` annotations of the members.
Neither annotation affects validation.
The exported root type is `DataProvenance`.
The string formats of the JSON schema map to the primitive aliases `URI`, `UUID`, `DateTime`, and `Date`.

## YAML Encoding {#yaml-encoding}

The YAML encoding of the data provenance metadata information model is provided in
`yaml/data-provenance.yaml`.

This file is a YAML serialization of `json/data-provenance.json`, generated from it.
It is provided for tooling that consumes YAML-format schemas natively.
All field names, constraints, type references, and enumeration values are identical
to those in the JSON schema.
