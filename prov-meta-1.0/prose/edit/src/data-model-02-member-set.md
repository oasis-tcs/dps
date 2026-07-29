### Member `set` {#member-set}

The `set` member specifies set-level meta-data.
It captures meta-data about the provenance metadata record describing a particular dataset.

The required members of `set` are `category`, `schema-version`, `publisher`, `label`, and `tracking`.
The optional members `language`, `source-language`, `acknowledgments`, `notes`, and `references` MAY also be present.

```yaml <!--json-path($..set.properties)-->
DataProvenance:
  # ...
  set:
    category: String.Pattern
    schema-version: String.Constant
    publisher: Mapping
    label: String
    tracking: Mapping
    # language: String.BCP47        (optional)
    # source-language: String.BCP47 (optional)
    # acknowledgments: Sequence     (optional)
    # notes: Sequence               (optional)
    # references: Sequence          (optional)
  # ...
# ...
```

#### Member `set.category` {#member-set-category}

The `set.category` member defines a short canonical name, chosen by the set producer, which will inform the end user as to the category of the metadata set.

```yaml <!--json-path($..set.properties.category.pattern)-->
DataProvenance:
  # ...
  set:
    category: String.Pattern
    # ...
  # ...
# ...
```

*Examples 1:*

```
dp_base
dp_event_source
dp_profile_xyz
Example Data Protection Notice Exemption
```

#### Member `set.schema-version` {#member-set-schema-version}

The `set.schema-version` member gives the version of the Data Provenance Core specification which the document was generated for.

```yaml <!--json-path($..set.properties['schema-version'].const)-->
DataProvenance:
  # ...
  set:
    # ...
    schema-version: String.Constant
    # ...
  # ...
# ...
```

The value of the `set.schema-version` member for this version of the specification is always:

```
1.0
```

#### Member `set.publisher` {#member-set-publisher}

The `set.publisher` member provides information about the publisher of the metadata set. The publisher is the party responsible for issuing the metadata set.

The required members of `set.publisher` are `name` and `namespace`. The optional member `contact-details` MAY also be present.

```yaml <!--json-path($..set.properties.publisher.properties)-->
DataProvenance:
  # ...
  set:
    # ...
    publisher:
      name: String
      namespace: String.URI
      # contact-details: String  (optional)
    # ...
  # ...
# ...
```

##### Member `set.publisher.name` {#member-set-publisher-name}

The `set.publisher.name` member contains the name of the issuing party.

```yaml <!--json-path($..set.properties.publisher.properties.name.type)-->
DataProvenance:
  # ...
  set:
    # ...
    publisher:
      name: String
      # ...
    # ...
  # ...
# ...
```

*Example 1:*

```
Cisco
```

##### Member `set.publisher.namespace` {#member-set-publisher-namespace}

The `set.publisher.namespace` member contains a URI which is under the control of the issuing party and can be used as a globally unique identifier for that issuing party.

```yaml <!--json-path($..set.properties.publisher.properties.namespace.format)-->
DataProvenance:
  # ...
  set:
    # ...
    publisher:
      # ...
      namespace: String.URI
      # ...
    # ...
  # ...
# ...
```

The value of `set.publisher.namespace` MUST be a valid URI.

*Example 1:*

```
https://cisco.com
```

##### Member `set.publisher.contact-details` {#member-set-publisher-contact-details}

The `set.publisher.contact-details` member provides information on how to contact the publisher, such as web sites, email addresses, phone numbers, or postal mail addresses.

```yaml <!--json-path($..set.properties.publisher.properties['contact-details'].type)-->
DataProvenance:
  # ...
  set:
    # ...
    publisher:
      # ...
      contact-details: String
    # ...
  # ...
# ...
```

*Example 1:*

```
Example Company can be reached at contact_us@example.com, or via our website at https://www.example.com/contact.
```

#### Member `set.label` {#member-set-label}

The `set.label` member provides the per-publisher unique title of the metadata set.

```yaml <!--json-path($..set.properties.label.type)-->
DataProvenance:
  # ...
  set:
    # ...
    label: String
    # ...
  # ...
# ...
```

The value of `set.label` SHOULD be a canonical name for the set, and sufficiently unique to distinguish it from similar sets.

*Examples 1:*

```
Learning Set for Regression Modelling for Stats 101
Example Data Protection Dataset in Example Generator
```

#### Member `set.tracking` {#member-set-tracking}

The `set.tracking` member is a container designated to hold all management attributes necessary to track a DP-Core set as a whole.

The required members of `set.tracking` are `current-release-date`, `id`, `initial-release-date`, `revision-history`, `status`, and `version`.
The optional members `aliases` and `generator` MAY also be present.

```yaml <!--json-path($..set.properties.tracking.properties)-->
DataProvenance:
  # ...
  set:
    # ...
    tracking:
      current-release-date: String.DateTime
      id: String.Pattern
      initial-release-date: String.DateTime
      revision-history: Sequence
      status: String.Enum
      version: $defs.version-type
      # aliases: Sequence   (optional)
      # generator: Mapping  (optional)
    # ...
  # ...
# ...
```

##### Member `set.tracking.current-release-date` {#member-set-tracking-current-release-date}

The `set.tracking.current-release-date` member contains the date when the current revision of this document was released.

```yaml <!--json-path($..set.properties.tracking.properties['current-release-date'].format)-->
DataProvenance:
  # ...
  set:
    # ...
    tracking:
      current-release-date: String.DateTime
      # ...
    # ...
  # ...
# ...
```

The value of `set.tracking.current-release-date` MUST be a valid date-time string conforming to \[RFC 3339\].

*Example 1:*

```
2000-01-01T01:01:01Z
```

##### Member `set.tracking.id` {#member-set-tracking-id}

The `set.tracking.id` member provides the unique identifier for the metadata set. The ID is a simple label that provides for a wide range of numbering values, types, and schemes. Its value SHOULD be assigned and maintained by the original metadata set issuing authority.

```yaml <!--json-path($..set.properties.tracking.properties.id.pattern)-->
DataProvenance:
  # ...
  set:
    # ...
    tracking:
      # ...
      id: String.Pattern
      # ...
    # ...
  # ...
# ...
```

The value of `set.tracking.id` MUST NOT start or end with whitespace.

*Examples 1:*

```
7aedeb0a-22dd-428a-ab76-c950b43cbbc6
abcdef-orga-ds-0815
cisco-sa-20190513-secureboot
```

##### Member `set.tracking.initial-release-date` {#member-set-tracking-initial-release-date}

The `set.tracking.initial-release-date` member contains the date when this set was first published.

```yaml <!--json-path($..set.properties.tracking.properties['initial-release-date'].format)-->
DataProvenance:
  # ...
  set:
    # ...
    tracking:
      # ...
      initial-release-date: String.DateTime
      # ...
    # ...
  # ...
# ...
```

The value of `set.tracking.initial-release-date` MUST be a valid date-time string conforming to \[RFC 3339\].

*Example 1:*

```
2000-01-01T01:01:01Z
```

##### Member `set.tracking.revision-history` {#member-set-tracking-revision-history}

The `set.tracking.revision-history` member holds one revision item for each version of the DP-Core set, including the initial one. The sequence MUST contain at least one revision item.

```yaml <!--json-path($..set.properties.tracking.properties['revision-history'].items.required)-->
DataProvenance:
  # ...
  set:
    # ...
    tracking:
      # ...
      revision-history:
        - date: String.DateTime
          number: $defs.version-type
          summary: String
          # legacy-version: String  (optional)
      # ...
    # ...
  # ...
# ...
```

Each revision item MUST contain the following members:

- `date`: The date of the revision entry. MUST be a valid date-time string conforming to \[RFC 3339\].
- `number`: The version number of the revision. MUST conform to `$defs.version-type` (integer or semantic versioning string).
- `summary`: A short description of the changes made in this revision.

The optional `legacy-version` member traces entries back to historic, DP-Core-unaware version strings.

*Example 1:*

```json
[
  {
    "date": "2000-01-01T01:01:01Z",
    "number": "1",
    "summary": "Initial version."
  }
]
```

##### Member `set.tracking.status` {#member-set-tracking-status}

The `set.tracking.status` member defines the draft status of the metadata set. This allows processing DP-Core sets of various maturity per version.

```yaml <!--json-path($..set.properties.tracking.properties.status.enum)-->
DataProvenance:
  # ...
  set:
    # ...
    tracking:
      # ...
      status: String.Enum
      # ...
    # ...
  # ...
# ...
```

The value of `set.tracking.status` MUST be one of the following:

- `draft`
- `final`
- `interim`

##### Member `set.tracking.version` {#member-set-tracking-version}

The `set.tracking.version` member specifies the version of the current DP-Core set.

```yaml <!--json-path($..set.properties.tracking.properties.version['$ref'])-->
DataProvenance:
  # ...
  set:
    # ...
    tracking:
      # ...
      version: $defs.version-type
      # ...
    # ...
  # ...
# ...
```

The value of `set.tracking.version` MUST conform to `$defs.version-type`, which requires either an integer or a semantic versioning string.

*Examples 1:*

```
1
2.0.0
1.0.0-beta+exp.sha.a1c44f85
```

##### Member `set.tracking.aliases` {#member-set-tracking-aliases}

The `set.tracking.aliases` member contains a list of alternate names for the same set.
Each alias MUST be a non-empty string and all entries MUST be unique.

```yaml <!--json-path($..set.properties.tracking.properties.aliases.items.type)-->
DataProvenance:
  # ...
  set:
    # ...
    tracking:
      # ...
      aliases:
        - String
    # ...
  # ...
# ...
```

*Example 1:*

```json
["0bacba95-ceb9-4fae-bf07-d5683a9481c1"]
```

##### Member `set.tracking.generator` {#member-set-tracking-generator}

The `set.tracking.generator` member holds information about the engine that generated the metadata set.
The required sub-member is `engine`. The optional sub-member `date` MAY also be present.

```yaml <!--json-path($..set.properties.tracking.properties.generator)-->
DataProvenance:
  # ...
  set:
    # ...
    tracking:
      # ...
      generator:
        engine:
          name: String
          # version: $defs.version-type  (optional)
        # date: String.DateTime  (optional)
    # ...
  # ...
# ...
```

- `engine.name`: The name of the tool or system that produced the metadata set.
- `engine.version`: The version of that tool. MUST conform to `$defs.version-type` when present.
- `date`: The date-time at which the metadata set was generated. MUST conform to \[RFC 3339\] when present.

*Example 1:*

```json
{
  "engine": {"name": "DPCoreX", "version": "1.0.0"},
  "date": "2025-01-15T10:00:00Z"
}
```

#### Member `set.language` {#member-set-language}

The `set.language` member identifies the language used in this document, corresponding to IETF BCP 47 / RFC 5646.

```yaml <!--json-path($..set.properties.language['$ref'])-->
DataProvenance:
  # ...
  set:
    # ...
    language: String.BCP47
    # ...
  # ...
# ...
```

*Examples 1:*

```
de
en
fr
```

#### Member `set.source-language` {#member-set-source-language}

The `set.source-language` member identifies the language this document was translated from, when this copy is a translation.

```yaml <!--json-path($..set.properties['source-language']['$ref'])-->
DataProvenance:
  # ...
  set:
    # ...
    source-language: String.BCP47
    # ...
  # ...
# ...
```

#### Member `set.acknowledgments` {#member-set-acknowledgments}

The `set.acknowledgments` member contains a list of acknowledgment elements associated with the whole set.
Each acknowledgment item MUST have at least one of the following members: `names`, `organization`, `summary`, or `urls`.

```yaml <!--json-path($..set.properties.acknowledgments['$ref'])-->
DataProvenance:
  # ...
  set:
    # ...
    acknowledgments:
      - # names: Sequence       (optional)
        # organization: String  (optional)
        # summary: String       (optional)
        # urls: Sequence        (optional)
  # ...
# ...
```

*Example 1:*

```json
[
  {
    "names": ["A. Big Data"],
    "organization": "ETH Zurich",
    "summary": "First analysis of the merged data-set"
  }
]
```

#### Member `set.notes` {#member-set-notes}

The `set.notes` member contains a list of notes associated with this metadata set.
Each note MUST have a `category` and `text`. The optional members `audience` and `title` MAY also be present.
The `category` value MUST be one of: `general`, `other`, `privacy`, `summary`.

```yaml <!--json-path($..set.properties.notes['$ref'])-->
DataProvenance:
  # ...
  set:
    # ...
    notes:
      - category: String.Enum  # NoteCategory: description | details | faq | general | legal_disclaimer | other | summary
        text: String
        # audience: String  (optional)
        # title: String     (optional)
  # ...
# ...
```

- `category`: The category of the note.
- `text`: The content of the note, varying depending on type.
- `audience`: The intended audience for the note.
- `title`: A concise description of what is contained in the text of the note.

#### Member `set.references` {#member-set-references}

The `set.references` member contains a list of references associated with this metadata set.
Each reference MUST have a `summary` and a `url`. The optional member `category` MAY also be present.
The `category` value MUST be one of: `external`, `self`.

```yaml <!--json-path($..set.properties.references['$ref'])-->
DataProvenance:
  # ...
  set:
    # ...
    references:
      - summary: String
        url: String.URI
        # category: String.Enum  # ReferenceCategory: external | self (optional)
  # ...
# ...
```

- `summary`: A short description of what this reference refers to.
- `url`: The URL of the referenced resource.
- `category`: Whether this reference is external or self-referential (default: `external`).
