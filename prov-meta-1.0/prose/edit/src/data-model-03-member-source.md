### Member `source` {#member-source}

The `source` member characterizes the content and source of the dataset.
All six of its members are required.

```yaml <!--json-path($['$defs']['source-type'].properties)-->
DataProvenance:
  # ...
  source:
    about: Mapping
    id: Mapping
    issuer: Sequence
    location: String.URI
    name: String
    data-version: $defs.version-type
  # ...
# ...
```

The members of `source` are described in the following subsections.

#### Member `source.about` {#member-source-about}

The `source.about` member contains a detailed narrative that explains the contents, scope, and purpose of the dataset.
The required members are `content` and `purpose`. The optional member `scope` MAY also be present.

```yaml <!--json-path($['$defs']['about-type'].properties)-->
DataProvenance:
  # ...
  source:
    # ...
    about:
      content: String
      purpose: String
      # scope: String  (optional)
    # ...
  # ...
# ...
```

- `content`: Provides essential contextual information that helps users understand what the data represents and how it was collected.
- `purpose`: Explains the recommended uses.
- `scope`: Points out any limitations of the dataset.

*Example 1:*

```json
{
  "content": "We found these numbers on the parking lot.",
  "purpose": "Use only for learning regression modeling. Not for production use.",
  "scope": "We did not verify anything. Use at your own risk."
}
```

#### Member `source.id` {#member-source-id}

The `source.id` member provides a unique identifier for the dataset's metadata. At least one identification method MUST be provided.

```yaml <!--json-path($['$defs']['identity-type'].minProperties)-->
DataProvenance:
  # ...
  source:
    # ...
    id:  # at least one of the following
      hashes: Sequence
      uris: Sequence
      uuids: Sequence
      custom-ids: Sequence
    # ...
  # ...
# ...
```

The following identification methods are available:

- `hashes`: A list of cryptographic hash entries, each containing `tree-hashes` (a list of `{algorithm, value}` pairs) and a `path`.
- `uris`: A list of identifiers in URI format.
- `uuids`: A list of identifiers in UUID format.
- `custom-ids`: A list of identifiers in any text format, each with a required `method` and `value`, and optional `tool` and `parameter-list`.

*Example 1:*

```json
{
  "uuids": ["e5471657-9ede-4335-843b-c1376ef29bfa"]
}
```

*Example 2:*

```json
{
  "hashes": [
    {
      "tree-hashes": [{"algorithm": "sha256", "value": "af1349b9f5f9a1a6a0404dea36dcc9499bcb25c9adc112b7cc9a93cae41f3262"}],
      "path": "example-data.tar.xz"
    }
  ]
}
```

#### Member `source.issuer` {#member-source-issuer}

The `source.issuer` member identifies the legal entity or entities responsible for creating the dataset.
The value is a sequence of organization objects. Each organization MUST provide a `legal-name`. The sequence MUST contain at least one organization and all entries MUST be unique.
The optional members `address` and `url` MAY also be present in each organization.

```yaml <!--json-path($['$defs']['orga-type'].items.properties)-->
DataProvenance:
  # ...
  source:
    # ...
    issuer:
      - legal-name: String
        # address: Sequence  (optional)
        # url: String.URI    (optional)
    # ...
  # ...
# ...
```

*Example 1:*

```json
[
  {
    "legal-name": "Sampling Ltd.",
    "url": "https://example.com/smplng/about"
  }
]
```

#### Member `source.location` {#member-source-location}

The `source.location` member provides the web address where the dataset's metadata is published and can be accessed. Typically this will be a unique URI of the current dataset.

```yaml <!--json-path($['$defs']['source-type'].properties.location.type)-->
DataProvenance:
  # ...
  source:
    # ...
    location: String.URI
    # ...
  # ...
# ...
```

#### Member `source.name` {#member-source-name}

The `source.name` member provides the official name of the dataset, which should be descriptive and help easily identify the dataset's content and purpose.

```yaml <!--json-path($['$defs']['source-type'].properties.name.type)-->
DataProvenance:
  # ...
  source:
    # ...
    name: String
    # ...
  # ...
# ...
```

#### Member `source.data-version` {#member-source-data-version}

The `source.data-version` member specifies the version of the dataset this DP-Core set describes, allowing the dataset to evolve over time and keeping consistent labeling.

```yaml <!--json-path($['$defs']['source-type'].properties['data-version']['$ref'])-->
DataProvenance:
  # ...
  source:
    # ...
    data-version: $defs.version-type
    # ...
  # ...
# ...
```

The value of `source.data-version` MUST conform to `$defs.version-type`, which requires either an integer or a semantic versioning string.

*Examples 1:*

```
1
2.0.0
```
