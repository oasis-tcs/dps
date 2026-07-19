# Provenance Information Model Encoding {#provenance-information-model-encoding}

The technical encoding of the information model is specified in both JADN and YAML in the following subsections.

## JADN Encoding {#jadn-encoding}

The JADN encoding of the data provenance metadata information model is specified in
`jadn/data-provenance.jadn`.

The file contains 43 named types derived directly from the property tables in Section 5.
The exported root type is `DataProvenance`.
Six named primitive aliases (`URI`, `UUID`, `DateTime`, `Date`, `Version`, `Language`)
carry format constraints that apply wherever those types appear as field types,
keeping the field-level definitions free of inline format options.
Eight enumerated types carry the closed code vocabularies introduced in Section 5.

## YAML Encoding {#yaml-encoding}

The YAML encoding of the data provenance metadata information model is specified in
`yaml/data-provenance.yaml`.

This file is a YAML serialization of `json/data-provenance.json` and is normatively
equivalent to it.
It is provided for tooling that consumes YAML-format schemas natively.
All field names, constraints, type references, and enumeration values are identical
to those in the JSON schema.
