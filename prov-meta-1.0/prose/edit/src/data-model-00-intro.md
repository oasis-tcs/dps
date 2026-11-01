# Provenance Data Model Encoding {#provenance-data-model-encoding}

The information model defines which metadata elements a Data Provenance Metadata record contains and how they relate,
independent of any particular serialization.
JSON is the single normative encoding of the information model:
a Data Provenance Metadata record is a JSON document that is valid against the Data Provenance Metadata JSON schema.
The JADN and YAML encodings of section [sec](#provenance-information-model-encoding) are generated from that schema
and are informative.

## JSON Encoding {#json-encoding}

The technical encoding of the data provenance metadata data model
is specified in the following schema artifacts for JSON data:

- Data Provenance Metadata JSON schema
- Data Provenance Metadata Configuration JSON schema

The Data Provenance Metadata Configuration JSON schema configures validators
to enforce all type and subtype constraints.

The Data Provenance Metadata JSON schema provides definitions and the structure
for any data provenance metadata JSON instance.

The required top-level members are:

```{.yaml json-path="$.properties"}
DataProvenance:
  $schema: String.Const
  set: Mapping
  source: $defs.source-type
  provenance: $defs.provenance-type
  use: $defs.use-type
  proof: Mapping  # optional
```
