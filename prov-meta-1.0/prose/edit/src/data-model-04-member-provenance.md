### Member `provenance` {#member-provenance}

The `provenance` member describes the provenance of the dataset.

The required members are `origin-geography`, `date`, and `generation-method`.
The optional members `source`, `origin`, `previous-date`, `generation-period`, `format`, and `sub-provenance` MAY also be present.

```yaml <!--json-path($['$defs']['provenance-type'].properties)-->
DataProvenance:
  # ...
  provenance:
    origin-geography: Sequence
    date: String.Date
    generation-method: Sequence
    # source: String.URI            (optional)
    # origin: Sequence              (optional)
    # previous-date: String.Date    (optional)
    # generation-period: Mapping    (optional)
    # format: Sequence              (optional)
    # sub-provenance: Mapping       (optional, recursive)
  # ...
# ...
```

The required members of `provenance` are described in subsections 7.1.4.1–7.1.4.3; optional members in 7.1.4.4–7.1.4.9.

#### Member `provenance.origin-geography` {#member-provenance-origin-geography}

The `provenance.origin-geography` member identifies the geographical locations where the data was originally collected, which can be important for compliance with regional laws and understanding the data's context.

The value is a sequence of geographic region objects. Each entry MUST contain a `country`. The optional `state` member MAY also be present. The sequence MUST contain at least one entry and all entries MUST be unique.

```yaml <!--json-path($['$defs']['geographic-regions-type'].items.properties)-->
DataProvenance:
  # ...
  provenance:
    # ...
    origin-geography:
      - country: String
        # state: String  (optional)
    # ...
  # ...
# ...
```

*Example 1:*

```json
[
  {"country": "US"},
  {"country": "DE", "state": "Bavaria"}
]
```

#### Member `provenance.date` {#member-provenance-date}

The `provenance.date` member provides the date when the dataset was compiled or created, providing a temporal context for the data.

```yaml <!--json-path($['$defs']['provenance-type'].properties.date.format)-->
DataProvenance:
  # ...
  provenance:
    # ...
    date: String.Date
    # ...
  # ...
# ...
```

The value of `provenance.date` MUST be a valid date string in full-date format (YYYY-MM-DD).

*Example 1:*

```
2000-01-01
```

#### Member `provenance.generation-method` {#member-provenance-generation-method}

The `provenance.generation-method` member describes the methodology or procedures used to collect, generate, or compile the data, giving insight into its reliability and validity.

The value is a sequence of method objects. Each method MUST contain a `code` drawn from the `GenerationMethodCode` vocabulary. The optional members `system` and `long-description` MAY also be present. The sequence MUST contain at least one method and all entries MUST be unique.

```yaml <!--json-path($['$defs']['provenance-type'].properties['generation-method'].items['$ref'])-->
DataProvenance:
  # ...
  provenance:
    # ...
    generation-method:
      - code: String.Enum  # GenerationMethodCode: data-augmentation | data-mining | feeds | machine-generated-ml-ops | other | primary-user-source | simulations | social-media | syndication | transfer-learning | user-generated-content | web-scraping-crawling
        # system: String           (optional)
        # long-description: String (optional)
    # ...
  # ...
# ...
```

*Example 1:*

```json
[
  {"code": "web-scraping-crawling"},
  {"code": "primary-user-source", "long-description": "Direct survey responses from participants."}
]
```

#### Member `provenance.source` {#member-provenance-source}

The `provenance.source` member identifies where the metadata for the source dataset contributing to the current dataset can be found, establishing lineage.

```yaml <!--json-path($['$defs']['provenance-type'].properties.source.format)-->
DataProvenance:
  # ...
  provenance:
    # ...
    source: String.URI
    # ...
  # ...
# ...
```

The value of `provenance.source` MUST be a valid URI.

*Example 1:*

```
https://example.com/datasets/source-dataset-42/provenance.json
```

#### Member `provenance.origin` {#member-provenance-origin}

The `provenance.origin` member identifies the original source organization when it differs from the issuer of the dataset.
The value is a sequence of organization objects following the same structure as `source.issuer`.

```yaml <!--json-path($['$defs']['provenance-type'].properties.origin['$ref'])-->
DataProvenance:
  # ...
  provenance:
    # ...
    origin:
      - legal-name: String
        # address: Sequence  (optional)
        # url: String.URI    (optional)
    # ...
  # ...
# ...
```

*Example 1:*

```json
[{"legal-name": "Original Data Collector Inc."}]
```

#### Member `provenance.previous-date` {#member-provenance-previous-date}

The `provenance.previous-date` member provides the release date of the previous version of the dataset, to track changes and updates over time.

```yaml <!--json-path($['$defs']['provenance-type'].properties['previous-date'].format)-->
DataProvenance:
  # ...
  provenance:
    # ...
    previous-date: String.Date
    # ...
  # ...
# ...
```

The value of `provenance.previous-date` MUST be a valid date string in full-date format (YYYY-MM-DD).

*Example 1:*

```
1999-06-15
```

#### Member `provenance.generation-period` {#member-provenance-generation-period}

The `provenance.generation-period` member describes the span of time during which the data within the dataset was collected or generated.
Both `start` and `end` are optional but MUST each conform to \[RFC 3339\] when present.

```yaml <!--json-path($['$defs']['provenance-type'].properties['generation-period'])-->
DataProvenance:
  # ...
  provenance:
    # ...
    generation-period:
      # start: String.DateTime  (optional)
      # end: String.DateTime    (optional)
    # ...
  # ...
# ...
```

*Example 1:*

```json
{
  "start": "1998-01-01T00:00:00Z",
  "end": "1999-12-31T23:59:59Z"
}
```

#### Member `provenance.format` {#member-provenance-format}

The `provenance.format` member describes the modality or media type of the data within the dataset.
The value is a sequence of `ModalityFormat` values. The sequence MUST contain at least one entry and all entries MUST be unique.

```yaml <!--json-path($['$defs']['provenance-type'].properties.format)-->
DataProvenance:
  # ...
  provenance:
    # ...
    format:
      - String.Enum  # ModalityFormat: application/json | application/jsonld | application/msword | application/vnd.ms-excel | application/zip | image/bmp | image/gif | image/jpeg | image/png | image/x-png | other | text/csv | text/plain
    # ...
  # ...
# ...
```

*Example 1:*

```json
["text/csv", "application/json"]
```

#### Member `provenance.sub-provenance` {#member-provenance-sub-provenance}

The `provenance.sub-provenance` member holds provenance information for a component of the current dataset, enabling a recursive provenance tree.
Its structure is identical to the enclosing `provenance` member.

```yaml <!--json-path($['$defs']['provenance-type'].properties['sub-provenance']['$ref'])-->
DataProvenance:
  # ...
  provenance:
    # ...
    sub-provenance:
      origin-geography: Sequence
      date: String.Date
      generation-method: Sequence
      # ... (same optional members as provenance)
    # ...
  # ...
# ...
```
