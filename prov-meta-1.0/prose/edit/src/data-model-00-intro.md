# Provenance Data Model Encoding {#provenance-data-model-encoding}

> The information model defines the complete set of metadata elements and associated attributes specified by the Data Provenance Standard.
> It establishes a common conceptual framework for representing provenance information, including the structures and relationships necessary to describe the origin, history, and handling of data.
> The information model is intended to provide a consistent semantic basis for provenance across implementations, independent of any particular serialization or storage mechanism.
>
> In order to support interoperability and exchange of provenance information between systems, the information model requires one or more concrete encodings.
> An encoding provides a standardized, machine-readable representation of the information model suitable for electronic transmission, persistence, and processing.
> While the information model defines what information is conveyed, the encoding defines how that information is represented for exchange between conforming implementations.
>
> This section describes a set of possible encodings for the Data Provenance Standard.
> Each encoding maps the constructs defined in the information model to a specific representation format intended for storage or system-to-system exchange.
> The encodings described herein are non-exclusive and are provided to support diverse implementation environments and usage scenarios.
> Implementations MAY support one or more of these encodings, subject to their interoperability, performance, and deployment requirements.

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

```yaml <!--json-path($.*[:])-->
DataProvenance:
  $schema: String.Constant
  set: Mapping
  source: Mapping
  provenance: Mapping
  use: Mapping
```
