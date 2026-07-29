### Member `use` {#member-use}

The `use` member describes legal use and restrictions that apply to the dataset.

The only required member is `intended-purpose`. All other members are optional.

```yaml <!--json-path($['$defs']['use-type'].properties)-->
DataProvenance:
  # ...
  use:
    intended-purpose: Sequence
    # classification: Sequence      (optional)
    # consents: Sequence            (optional)
    # data-risk-reducing: Sequence  (optional)
    # processing-included: Sequence (optional)
    # processing-excluded: Sequence (optional)
    # storage-allowed: Sequence     (optional)
    # storage-forbidden: Sequence   (optional)
    # license: Sequence             (optional)
    # copyright: Sequence           (optional)
    # patent: Sequence              (optional)
    # trademark: Sequence           (optional)
  # ...
# ...
```

#### Member `use.intended-purpose` {#member-use-intended-purpose}

The `use.intended-purpose` member describes the purpose for which the dataset was created, guiding users on its intended use and potential applications.

The value is a sequence of purpose objects. Each purpose MUST contain a `code` drawn from the `PurposeCode` vocabulary and a `long-description`. The optional `system` member MAY also be present. The sequence MUST contain at least one purpose and all entries MUST be unique.

```yaml <!--json-path($['$defs']['use-type'].properties['intended-purpose'].items['$ref'])-->
DataProvenance:
  # ...
  use:
    # ...
    intended-purpose:
      - code: String.Enum  # PurposeCode: alignment | evaluation | other | pre-training | production | quality-assurance | research | staging-testing | synthetic-data-generation
        long-description: String
        # system: String  (optional)
    # ...
  # ...
# ...
```

*Example 1:*

```json
[
  {
    "code": "research",
    "long-description": "Use only for learning regression modeling. Not for production use."
  }
]
```

#### Member `use.classification` {#member-use-classification}

The `use.classification` member indicates whether the dataset includes data falling into various confidentiality classifications.
The value is a sequence of classification objects. Each item MUST contain a `regulation` object whose `code` MUST be drawn from the `ConfidentialityCode` vocabulary, and an `evaluated` boolean. The optional `tool` member MAY also be present. All entries MUST be unique.

```yaml <!--json-path($['$defs']['use-type'].properties.classification)-->
DataProvenance:
  # ...
  use:
    # ...
    classification:
      - regulation:
          code: String.Enum  # ConfidentialityCode: other | pci | pfi | phi | pi | sci | spi
          # system: String           (optional)
          # long-description: String (optional)
        evaluated: Boolean
        # tool: String  (optional)
    # ...
  # ...
# ...
```

*Example 1:*

```json
[
  {"regulation": {"code": "phi"}, "evaluated": true},
  {"regulation": {"code": "pii"}, "evaluated": false}
]
```

#### Member `use.consents` {#member-use-consents}

The `use.consents` member specifies where consent documentation or agreements related to the data can be found, ensuring legal compliance and regulatory use.
The value is a sequence of strings. The sequence MUST contain at least one entry and all entries MUST be unique.

```yaml <!--json-path($['$defs']['use-type'].properties.consents)-->
DataProvenance:
  # ...
  use:
    # ...
    consents:
      - String
    # ...
  # ...
# ...
```

*Example 1:*

```json
["https://example.com/consent-policy-2024"]
```

#### Member `use.data-risk-reducing` {#member-use-data-risk-reducing}

The `use.data-risk-reducing` member indicates the techniques used to reduce known data risk.
The value is a sequence of objects. Each item MUST contain `tool-used`. The optional members `tool-category`, `technology`, `parameters`, and `results` MAY also be present. All entries MUST be unique.

```yaml <!--json-path($['$defs']['use-type'].properties['data-risk-reducing'])-->
DataProvenance:
  # ...
  use:
    # ...
    data-risk-reducing:
      - tool-used: String
        # tool-category: Mapping  (optional, method object)
        # technology: String.Enum (optional, DataTechnology value)
        # parameters: Sequence    (optional, list of {name, value} pairs)
        # results: Sequence       (optional, list of strings)
    # ...
  # ...
# ...
```

*Example 1:*

```json
[
  {
    "tool-used": "DataMaskPro",
    "technology": "data-masking",
    "parameters": [{"name": "--level", "value": "high"}],
    "results": ["All PII fields masked."]
  }
]
```

#### Member `use.processing-included` {#member-use-processing-included}

The `use.processing-included` member defines the geographical boundaries within which the data MAY be processed.
The value is a sequence of geographic region objects following the same structure as `provenance.origin-geography`.

```yaml <!--json-path($['$defs']['use-type'].properties['processing-included']['$ref'])-->
DataProvenance:
  # ...
  use:
    # ...
    processing-included:
      - country: String
        # state: String  (optional)
    # ...
  # ...
# ...
```

*Example 1:*

```json
[{"country": "DE"}, {"country": "FR"}]
```

#### Member `use.processing-excluded` {#member-use-processing-excluded}

The `use.processing-excluded` member defines the geographical boundaries within which the data MUST NOT be processed.
The value is a sequence of geographic region objects following the same structure as `provenance.origin-geography`.

```yaml <!--json-path($['$defs']['use-type'].properties['processing-excluded']['$ref'])-->
DataProvenance:
  # ...
  use:
    # ...
    processing-excluded:
      - country: String
        # state: String  (optional)
    # ...
  # ...
# ...
```

#### Member `use.storage-allowed` {#member-use-storage-allowed}

The `use.storage-allowed` member specifies geographical locations where the data MAY be stored.
The value is a sequence of geographic region objects following the same structure as `provenance.origin-geography`.

```yaml <!--json-path($['$defs']['use-type'].properties['storage-allowed']['$ref'])-->
DataProvenance:
  # ...
  use:
    # ...
    storage-allowed:
      - country: String
        # state: String  (optional)
    # ...
  # ...
# ...
```

#### Member `use.storage-forbidden` {#member-use-storage-forbidden}

The `use.storage-forbidden` member specifies geographical locations where the data MUST NOT be stored.
The value is a sequence of geographic region objects following the same structure as `provenance.origin-geography`.

```yaml <!--json-path($['$defs']['use-type'].properties['storage-forbidden']['$ref'])-->
DataProvenance:
  # ...
  use:
    # ...
    storage-forbidden:
      - country: String
        # state: String  (optional)
    # ...
  # ...
# ...
```

#### Member `use.license` {#member-use-license}

The `use.license` member details the terms under which the dataset can be used, including any restrictions or obligations.
License entries MAY include End User License Agreements (EULA) or Data Use Agreements (DUA).
The value is a sequence of strings. The sequence MUST contain at least one entry and all entries MUST be unique.

```yaml <!--json-path($['$defs']['use-type'].properties.license)-->
DataProvenance:
  # ...
  use:
    # ...
    license:
      - String
    # ...
  # ...
# ...
```

*Example 1:*

```json
["https://creativecommons.org/licenses/by/4.0/"]
```

#### Member `use.copyright` {#member-use-copyright}

The `use.copyright` member indicates whether the dataset contains proprietary information covered by a copyright, and the terms of that copyright.
The value is a sequence of strings. The sequence MUST contain at least one entry and all entries MUST be unique.

```yaml <!--json-path($['$defs']['use-type'].properties.copyright)-->
DataProvenance:
  # ...
  use:
    # ...
    copyright:
      - String
    # ...
  # ...
# ...
```

*Example 1:*

```json
["Copyright © 2024 Example Corp. All rights reserved."]
```

#### Member `use.patent` {#member-use-patent}

The `use.patent` member indicates whether the dataset contains proprietary information covered by a patent, and the patent number.
The value is a sequence of strings. The sequence MUST contain at least one entry and all entries MUST be unique.

```yaml <!--json-path($['$defs']['use-type'].properties.patent)-->
DataProvenance:
  # ...
  use:
    # ...
    patent:
      - String
    # ...
  # ...
# ...
```

#### Member `use.trademark` {#member-use-trademark}

The `use.trademark` member indicates whether the dataset contains proprietary information covered by a trademark, and the terms of that trademark.
The value is a sequence of strings. The sequence MUST contain at least one entry and all entries MUST be unique.

```yaml <!--json-path($['$defs']['use-type'].properties.trademark)-->
DataProvenance:
  # ...
  use:
    # ...
    trademark:
      - String
    # ...
  # ...
# ...
```

---
