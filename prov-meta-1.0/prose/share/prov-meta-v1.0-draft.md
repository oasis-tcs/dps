![](https://docs.oasis-open.org/templates/OASISLogo-v3.0.png)

# Data Provenance Metadata Version 1.0<a id='data-provenance-metadata-version-1-0'></a>

## Committee Specification Draft 02<a id='committee-specification-draft-02'></a>

## 3 November 2026<a id='3-november-2026'></a>

### This version<a id='this-version'></a>

- <https://docs.oasis-open.org/dps/prov-meta/v1.0/csd02/prov-meta-v1.0-csd02.md> (Authoritative)
- <https://docs.oasis-open.org/dps/prov-meta/v1.0/csd02/prov-meta-v1.0-csd02.html>
- <https://docs.oasis-open.org/dps/prov-meta/v1.0/csd02/prov-meta-v1.0-csd02.pdf>

### Latest version<a id='latest-version'></a>

- <https://docs.oasis-open.org/dps/prov-meta/v1.0/prov-meta-v1.0.md> (Authoritative)
- <https://docs.oasis-open.org/dps/prov-meta/v1.0/prov-meta-v1.0.html>
- <https://docs.oasis-open.org/dps/prov-meta/v1.0/prov-meta-v1.0.pdf>

### Previous version<a id='previous-version'></a>

- <https://docs.oasis-open.org/dps/prov-meta/v1.0/csd01/prov-meta-v1.0-csd01.md> (Authoritative)
- <https://docs.oasis-open.org/dps/prov-meta/v1.0/csd01/prov-meta-v1.0-csd01.html>
- <https://docs.oasis-open.org/dps/prov-meta/v1.0/csd01/prov-meta-v1.0-csd01.pdf>

### Technical Committee<a id='technical-committee'></a>

[Data Provenance Standard Technical Committee](https://groups.oasis-open.org/communities/tc-community-home2?CommunityKey=2c60b2cf-45d3-48cd-8594-0194f182b33d)

### Chairs<a id='chairs'></a>

- Lisa Bobbitt, Cisco, lbobbitt@cisco.com
- Bryan Bortnick, IBM, bortnick@us.ibm.com
- Fotis Psallidas, Microsoft, Fotis.Psallidas@microsoft.com

### Secretaries<a id='secretaries'></a>

- Jamie Yu, Cisco, jamyu2@cisco.com

### Editors<a id='editors'></a>

- David Kemp, NSA, d.kemp@cyber.nsa.gov
- Stefan Hagen, individual, stefan@hagen.link

### Additional Artifacts<a id='additional-artifacts'></a>

This prose specification is one component of a Work Product that also includes:

- Data Provenance Metadata JSON schema: <https://docs.oasis-open.org/dps/prov-meta/v1.0/csd02/schema/data-provenance.json>. \
  Latest stage: <https://docs.oasis-open.org/dps/prov-meta/v1.0/schema/data-provenance.json>.
- Data Provenance Metadata Configuration JSON schema: <https://docs.oasis-open.org/dps/prov-meta/v1.0/csd02/schema/data-provenance-configuration.json>. \
  Latest stage: <https://docs.oasis-open.org/dps/prov-meta/v1.0/schema/data-provenance-configuration.json>.

### Declared JSON namespaces<a id='declared-json-namespaces'></a>

- <https://docs.oasis-open.org/dps/prov-meta/v1.0/schema/data-provenance.json>
- <https://docs.oasis-open.org/dps/prov-meta/v1.0/schema/data-provenance-configuration.json>

### Abstract<a id='abstract'></a>

This OASIS Data Provenance Metadata specification provides an information model and several specialized data schemata for describing and managing data provenance and data lineage.
The resulting common language provides transparency for data provenance and enables assessing where data comes from,
how it has been created, and in what scenarios it can be used, legally.

### Citation Format<a id='citation-format'></a>

When referencing this document, the following citation format should be used:

**[prov-meta-v1.0]**

_Data Provenance Metadata Version 1.0_. Edited by David Kemp and Stefan Hagen. 3 November 2026. OASIS Committee Specification Draft 02.
<https://docs.oasis-open.org/dps/prov-meta/v1.0/csd02/prov-meta-v1.0-csd02.html>. \
Latest stage: <https://docs.oasis-open.org/dps/prov-meta/v1.0/prov-meta-v1.0.html>.

### Related Work<a id='related-work'></a>

This document replaces or supersedes:

N/A

This document is related to:

N/A

## License, Document Status, and Notices<a id='license-document-status-and-notices'></a>

Copyright © OASIS Open 2026.
All Rights Reserved.  
For license and copyright information, and complete status, please see [Annex A](#annex-a) which contains the License, Document Status and Notices.

---

-------

# Table of Contents

1. [Scope](#scope)  
2. [Definitions and Acronyms](#definitions-and-acronyms)  
	2.1 [Definitions](#definitions)  
		2.1.1 [Terms Defined Elsewhere](#terms-defined-elsewhere)  
		2.1.2 [Terms Defined in this Document](#terms-defined-in-this-document)  
	2.2 [Abbreviations and Acronyms](#abbreviations-and-acronyms)  
3. [Document Conventions](#document-conventions)  
	3.1 [Key Words](#key-words)  
	3.2 [Typographical Conventions](#typographical-conventions)  
4. [Introduction](#introduction)  
	4.1 [Changes From the Previous Version](#changes-from-the-previous-version)  
5. [Provenance Information Model Encoding](#provenance-information-model-encoding)  
	5.1 [JADN Encoding](#jadn-encoding)  
	5.2 [YAML Encoding](#yaml-encoding)  
6. [Provenance Data Model Encoding](#provenance-data-model-encoding)  
	6.1 [JSON Encoding](#json-encoding)  
		6.1.1 [Member `$schema`](#member-schema)  
		6.1.2 [Member `set`](#member-set)  
			6.1.2.1 [Member `set.category`](#member-set-category)  
			6.1.2.2 [Member `set.schema-version`](#member-set-schema-version)  
			6.1.2.3 [Member `set.publisher`](#member-set-publisher)  
				6.1.2.3.1 [Member `set.publisher.name`](#member-set-publisher-name)  
				6.1.2.3.2 [Member `set.publisher.namespace`](#member-set-publisher-namespace)  
				6.1.2.3.3 [Member `set.publisher.contact-details`](#member-set-publisher-contact-details)  
			6.1.2.4 [Member `set.label`](#member-set-label)  
			6.1.2.5 [Member `set.tracking`](#member-set-tracking)  
				6.1.2.5.1 [Member `set.tracking.current-release-date`](#member-set-tracking-current-release-date)  
				6.1.2.5.2 [Member `set.tracking.id`](#member-set-tracking-id)  
				6.1.2.5.3 [Member `set.tracking.initial-release-date`](#member-set-tracking-initial-release-date)  
				6.1.2.5.4 [Member `set.tracking.revision-history`](#member-set-tracking-revision-history)  
				6.1.2.5.5 [Member `set.tracking.status`](#member-set-tracking-status)  
				6.1.2.5.6 [Member `set.tracking.version`](#member-set-tracking-version)  
				6.1.2.5.7 [Member `set.tracking.aliases`](#member-set-tracking-aliases)  
				6.1.2.5.8 [Member `set.tracking.generator`](#member-set-tracking-generator)  
			6.1.2.6 [Member `set.language`](#member-set-language)  
			6.1.2.7 [Member `set.source-language`](#member-set-source-language)  
			6.1.2.8 [Member `set.acknowledgments`](#member-set-acknowledgments)  
			6.1.2.9 [Member `set.notes`](#member-set-notes)  
			6.1.2.10 [Member `set.references`](#member-set-references)  
		6.1.3 [Member `source`](#member-source)  
			6.1.3.1 [Member `source.about`](#member-source-about)  
			6.1.3.2 [Member `source.id`](#member-source-id)  
			6.1.3.3 [Member `source.issuer`](#member-source-issuer)  
			6.1.3.4 [Member `source.location`](#member-source-location)  
			6.1.3.5 [Member `source.name`](#member-source-name)  
			6.1.3.6 [Member `source.data-version`](#member-source-data-version)  
		6.1.4 [Member `provenance`](#member-provenance)  
			6.1.4.1 [Member `provenance.origin-geography`](#member-provenance-origin-geography)  
			6.1.4.2 [Member `provenance.date`](#member-provenance-date)  
			6.1.4.3 [Member `provenance.generation-method`](#member-provenance-generation-method)  
			6.1.4.4 [Member `provenance.source`](#member-provenance-source)  
			6.1.4.5 [Member `provenance.origin`](#member-provenance-origin)  
			6.1.4.6 [Member `provenance.previous-date`](#member-provenance-previous-date)  
			6.1.4.7 [Member `provenance.generation-period`](#member-provenance-generation-period)  
			6.1.4.8 [Member `provenance.format`](#member-provenance-format)  
			6.1.4.9 [Member `provenance.sub-provenance`](#member-provenance-sub-provenance)  
			6.1.4.10 [Member `provenance.source-digest`](#member-provenance-source-digest)  
		6.1.5 [Member `use`](#member-use)  
			6.1.5.1 [Member `use.intended-purpose`](#member-use-intended-purpose)  
			6.1.5.2 [Member `use.classification`](#member-use-classification)  
			6.1.5.3 [Member `use.consents`](#member-use-consents)  
			6.1.5.4 [Member `use.data-risk-reducing`](#member-use-data-risk-reducing)  
			6.1.5.5 [Member `use.processing-included`](#member-use-processing-included)  
			6.1.5.6 [Member `use.processing-excluded`](#member-use-processing-excluded)  
			6.1.5.7 [Member `use.storage-allowed`](#member-use-storage-allowed)  
			6.1.5.8 [Member `use.storage-forbidden`](#member-use-storage-forbidden)  
			6.1.5.9 [Member `use.license`](#member-use-license)  
			6.1.5.10 [Member `use.copyright`](#member-use-copyright)  
			6.1.5.11 [Member `use.patent`](#member-use-patent)  
			6.1.5.12 [Member `use.trademark`](#member-use-trademark)  
		6.1.6 [Member `proof`](#member-proof)  
7. [Provenance Schema](#provenance-schema)  
	7.1 [Primary Metadata Elements](#primary-metadata-elements)  
	7.2 [Set](#set)  
	7.3 [Source](#source)  
	7.4 [Provenance](#provenance)  
	7.5 [Use](#use)  
	7.6 [Shared Types](#shared-types)  
8. [Safety, Security, and Data Protection](#safety-security-and-data-protection)  
	8.1 [Integrity and Authenticity of Provenance Claims](#integrity-and-authenticity)  
	8.2 [URI Safety](#uri-safety)  
	8.3 [Sensitive Information in Provenance Records](#sensitive-information)  
	8.4 [Data Protection Compliance](#data-protection-compliance)  
9. [Conformance](#conformance)  

Annex A. [License, Document Status and Notices](#annex-a)  
	A.1 [Document Status](#document-status)  
	A.2 [License and Notices](#license-and-notices)  
Annex B. [References](#annex-b)  
	B.1 [Normative References](#normative-references)  
	B.2 [Informative References](#informative-references)  
Annex C. [Example Instances](#annex-c)  
	C.1 [Minimal Example](#minimal-example)  
	C.2 [Moderate Example](#moderate-example)  
	C.3 [Complete Example](#complete-example)  
	C.4 [Lineage Example](#lineage-example)  
Appendix A. [Acknowledgments](#appendix-acknowledgments)  
	 [Leadership](#leadership)  
	 [Special Thanks](#special-thanks)  
	 [Participants](#participants)  
Appendix B. [Changes From Previous Version](#appendix-changes-from-previous-version)  
	 [Revision History](#revision-history)  


-------

# 1. Scope<a id='scope'></a>

Data is a core enterprise asset that underpins strategic decision-making, drives operational priorities, and supports risk governance.
Dependence on data creates a need for validation by understanding data’s origin, quality, and intended use.
Understanding data is a requirement for organizations operating at scale.
The OASIS Data Provenance Standards (DPS) are created to solve for this need.
Developed through cross-industry collaboration, the DPS provide a consistent framework to track the origin, movement, integrity, and quality of data.
The DPS address the growing demand for transparency in artificial intelligence (AI), cybersecurity, supply chains,
and areas where data quality and accountability are foundational to performance and compliance - especially in regulated and high-risk environments.

---

# 2. Definitions and Acronyms<a id='definitions-and-acronyms'></a>

## 2.1 Definitions<a id='definitions'></a>

### 2.1.1 Terms Defined Elsewhere<a id='terms-defined-elsewhere'></a>

This document uses the following terms defined elsewhere:


Data Provenance
:    In the context of computers and law enforcement use, it is synonymous to chain of custody.
     It involves the method of generation, transmission and storage of information that
     may be used to trace the origin of a piece of information processed by community resources.
     Cf. \[[CNSSI-4009](#CNSSI-4009)\] for more details.

Data Lineage
:    Data lineage is the process of tracking the (use and) flow of data over time, providing a clear understanding of where the data originated,
     how it has changed, and its ultimate destination within the data pipeline.
     Cf. "Data Lineage at IBM" <https://www.ibm.com/think/topics/data-lineage> for more details.

Data Transparency
:   Data transparency refers to the clear, open, and honest handling of data within an organization.
    It means that businesses, governments, and institutions disclose how they collect, store, use, and share data, ensuring users, customers,
    and stakeholders understand their practices.
    Cf. "What is data transparency at BigID" <https://bigid.com/blog/what-is-data-transparency> for more details.


### 2.1.2 Terms Defined in this Document<a id='terms-defined-in-this-document'></a>

None

## 2.2 Abbreviations and Acronyms<a id='abbreviations-and-acronyms'></a>

AI
:    Artificial Intelligence

DET
:    Data Enhancing Technologies

DPS
:    Data Provenance Standard

PET
:    Privacy Enhancing Technologies

<!-- We will surely find more acronyms or abbreviations we do use in the document. -->

---

# 3. Document Conventions<a id='document-conventions'></a>

## 3.1 Key Words<a id='key-words'></a>

The key words "**MUST**", "**MUST NOT**", "**REQUIRED**", "**SHALL**", "**SHALL NOT**", "**SHOULD**", "**SHOULD NOT**", "**RECOMMENDED**", "**NOT RECOMMENDED**", "**MAY**",
and "**OPTIONAL**" in this document are to be interpreted as described in BCP 14 \[[RFC2119](#RFC2119)\] and \[[RFC8174](#RFC8174)\] when, and only when, they appear in all capitals, as shown here.

## 3.2 Typographical Conventions<a id='typographical-conventions'></a>

Keywords defined by this specification use this `monospaced` font.

```
    Normative source code uses this paragraph style.
```

Some sections of this specification are illustrated with non-normative examples introduced with "Example" or "Examples" like so:

*Example 1:*<a id='typographical-conventions-eg-1'></a><a id='sec-3-2-eg-1'></a><a id='example-4321'></a>

```
    Informative examples also use this paragraph style but preceded by the text "Example(s)".
```

All examples in this document are informative only.

All other text is normative unless otherwise labeled e.g. like the following informative comment:

> This is a pure informative comment that may be present, because the information conveyed is deemed useful advice or
> common pitfalls learned from implementer or operator experience and often given including the rationale.

---

This document adheres to the Modern Language Association (MLA) style guidelines for formatting titles and terms.

# 4. Introduction<a id='introduction'></a>

Data is a core enterprise asset.
It underpins strategic decision-making, drives operational priorities, and supports risk governance.
Dependence on data creates a need for validation and an understanding of the data's origin, quality, and intended use.
Understanding data is a requirement for organizations operating at scale.
The OASIS Data Provenance Standards (DPS) are created to solve for this need.

## 4.1 Changes From the Previous Version<a id='changes-from-the-previous-version'></a>

N/A

---

# 5. Provenance Information Model Encoding<a id='provenance-information-model-encoding'></a>

This specification defines the Data Provenance Metadata format by one normative artifact and views derived from it:

JSON schema
:   The Data Provenance Metadata JSON schema (`json/data-provenance.json`) is the normative definition of the format.
    It decides which documents are valid, and it carries the description of every member.

YAML outlines
:   The outlines in section [6 "Provenance Data Model Encoding"](#provenance-data-model-encoding) show where each member sits in a document,
    whether it is required, and its type, in a compact notation generated from the JSON schema.

Property tables
:   The tables in section [7 "Provenance Schema"](#provenance-schema) give, for each type, its members with their type, cardinality, and description.
    They are generated from the JADN encoding of the information model (section [5.1 "JADN Encoding"](#jadn-encoding)), which in turn is generated from the JSON schema.

The information model is also available in the following two informative encodings, both generated from the JSON schema.
The JSON encoding (section [6.1 "JSON Encoding"](#json-encoding)) is the only normative one.

## 5.1 JADN Encoding<a id='jadn-encoding'></a>

The JADN encoding of the data provenance metadata information model is provided in
`jadn/data-provenance.jadn`.

The file is generated from the JSON schema.
Each schema node that defines a type carries the JADN type name in the annotation `x-jadn-type`,
and each enumeration carries the descriptions of its values in the annotation `x-jadn-enum`;
the descriptions of the fields are the `description` annotations of the members.
Neither annotation affects validation.
The exported root type is `DataProvenance`.
The string formats of the JSON schema map to the primitive aliases `URI`, `UUID`, `DateTime`, and `Date`.

## 5.2 YAML Encoding<a id='yaml-encoding'></a>

The YAML encoding of the data provenance metadata information model is provided in
`yaml/data-provenance.yaml`.

This file is a YAML serialization of `json/data-provenance.json`, generated from it.
It is provided for tooling that consumes YAML-format schemas natively.
All field names, constraints, type references, and enumeration values are identical
to those in the JSON schema.

# 6. Provenance Data Model Encoding<a id='provenance-data-model-encoding'></a>

The information model defines which metadata elements a Data Provenance Metadata record contains and how they relate,
independent of any particular serialization.
JSON is the single normative encoding of the information model:
a Data Provenance Metadata record is a JSON document that is valid against the Data Provenance Metadata JSON schema.
The JADN and YAML encodings of section [5 "Provenance Information Model Encoding"](#provenance-information-model-encoding) are generated from that schema
and are informative.

## 6.1 JSON Encoding<a id='json-encoding'></a>

The technical encoding of the data provenance metadata data model
is specified in the following schema artifacts for JSON data:

- Data Provenance Metadata JSON schema
- Data Provenance Metadata Configuration JSON schema

The Data Provenance Metadata Configuration JSON schema configures validators
to enforce all type and subtype constraints.

The Data Provenance Metadata JSON schema provides definitions and the structure
for any data provenance metadata JSON instance.

The required top-level members are:

```yaml
DataProvenance:
  $schema: String.Const
  set: Mapping
  source: $defs.source-type
  provenance: $defs.provenance-type
  use: $defs.use-type
  proof: Mapping  # optional
```

### 6.1.1 Member `$schema`<a id='member-schema'></a>

The value of the `$schema` member for this version of the specification is always:

```
https://docs.oasis-open.org/dps/prov-meta/v1.0/schema/data-provenance.json
```

### 6.1.2 Member `set`<a id='member-set'></a>

The `set` member specifies set-level meta-data.
It captures meta-data about the provenance metadata record describing a particular dataset.

The required members of `set` are `category`, `schema-version`, `publisher`, `label`, and `tracking`.
The optional members `language`, `source-language`, `acknowledgments`, `notes`, and `references` MAY also be present.

```yaml
DataProvenance:
  # ...
  set:
    category: String.Pattern
    schema-version: String.Const
    publisher: Mapping
    label: String
    tracking: Mapping
    language: $defs.language-type                # optional
    source-language: $defs.language-type         # optional
    acknowledgments: $defs.acknowledgments-type  # optional
    notes: $defs.notes-type                      # optional
    references: $defs.references-type            # optional
  # ...
```

#### 6.1.2.1 Member `set.category`<a id='member-set-category'></a>

The `set.category` member defines a short canonical name, chosen by the set producer, which will inform the end user as to the category of the metadata set.

```yaml
DataProvenance:
  # ...
  set:
    category: String.Pattern
    # ...
  # ...
```

*Examples 1:*<a id='member-set-category-eg-1'></a><a id='sec-6-1-2-1-eg-1'></a><a id='example-1'></a>

```
dp_base
dp_event_source
dp_profile_xyz
Example Data Protection Notice Exemption
```

#### 6.1.2.2 Member `set.schema-version`<a id='member-set-schema-version'></a>

The `set.schema-version` member gives the version of the Data Provenance Core specification which the document was generated for.

```yaml
DataProvenance:
  # ...
  set:
    # ...
    schema-version: String.Const
    # ...
  # ...
```

The value of the `set.schema-version` member for this version of the specification is always:

```
1.0
```

#### 6.1.2.3 Member `set.publisher`<a id='member-set-publisher'></a>

The `set.publisher` member provides information about the publisher of the metadata set. The publisher is the party responsible for issuing the metadata set.

The required members of `set.publisher` are `name` and `namespace`. The optional member `contact-details` MAY also be present.

```yaml
DataProvenance:
  # ...
  set:
    # ...
    publisher:
      name: String
      namespace: String.URI
      contact-details: String  # optional
    # ...
  # ...
```

##### 6.1.2.3.1 Member `set.publisher.name`<a id='member-set-publisher-name'></a>

The `set.publisher.name` member contains the name of the issuing party.

```yaml
DataProvenance:
  # ...
  set:
    # ...
    publisher:
      name: String
      # ...
    # ...
  # ...
```

*Example 1:*<a id='member-set-publisher-name-eg-1'></a><a id='sec-6-1-2-3-1-eg-1'></a><a id='example-2'></a>

```
Cisco
```

##### 6.1.2.3.2 Member `set.publisher.namespace`<a id='member-set-publisher-namespace'></a>

The `set.publisher.namespace` member contains a URI which is under the control of the issuing party and can be used as a globally unique identifier for that issuing party.

```yaml
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
```

The value of `set.publisher.namespace` MUST be a valid URI.

*Example 1:*<a id='member-set-publisher-namespace-eg-1'></a><a id='sec-6-1-2-3-2-eg-1'></a><a id='example-3'></a>

```
https://cisco.com
```

##### 6.1.2.3.3 Member `set.publisher.contact-details`<a id='member-set-publisher-contact-details'></a>

The `set.publisher.contact-details` member provides information on how to contact the publisher, such as web sites, email addresses, phone numbers, or postal mail addresses.

```yaml
DataProvenance:
  # ...
  set:
    # ...
    publisher:
      # ...
      contact-details: String  # optional
    # ...
  # ...
```

*Example 1:*<a id='member-set-publisher-contact-details-eg-1'></a><a id='sec-6-1-2-3-3-eg-1'></a><a id='example-4'></a>

```
Example Company can be reached at contact_us@example.com, or via our website at https://www.example.com/contact.
```

#### 6.1.2.4 Member `set.label`<a id='member-set-label'></a>

The `set.label` member provides the per-publisher unique title of the metadata set.

```yaml
DataProvenance:
  # ...
  set:
    # ...
    label: String
    # ...
  # ...
```

The value of `set.label` SHOULD be a canonical name for the set, and sufficiently unique to distinguish it from similar sets.

*Examples 1:*<a id='member-set-label-eg-1'></a><a id='sec-6-1-2-4-eg-1'></a><a id='example-5'></a>

```
Learning Set for Regression Modelling for Stats 101
Example Data Protection Dataset in Example Generator
```

#### 6.1.2.5 Member `set.tracking`<a id='member-set-tracking'></a>

The `set.tracking` member is a container designated to hold all management attributes necessary to track a DP-Core set as a whole.

The required members of `set.tracking` are `current-release-date`, `id`, `initial-release-date`, `revision-history`, `status`, and `version`.
The optional members `aliases` and `generator` MAY also be present.

```yaml
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
      aliases: Sequence   # optional
      generator: Mapping  # optional
    # ...
  # ...
```

##### 6.1.2.5.1 Member `set.tracking.current-release-date`<a id='member-set-tracking-current-release-date'></a>

The `set.tracking.current-release-date` member contains the date when the current revision of this document was released.

```yaml
DataProvenance:
  # ...
  set:
    # ...
    tracking:
      current-release-date: String.DateTime
      # ...
    # ...
  # ...
```

The value of `set.tracking.current-release-date` MUST be a valid date-time string conforming to \[RFC 3339\].

*Example 1:*<a id='member-set-tracking-current-release-date-eg-1'></a><a id='sec-6-1-2-5-1-eg-1'></a><a id='example-6'></a>

```
2000-01-01T01:01:01Z
```

##### 6.1.2.5.2 Member `set.tracking.id`<a id='member-set-tracking-id'></a>

The `set.tracking.id` member provides the unique identifier for the metadata set. The ID is a simple label that provides for a wide range of numbering values, types, and schemes. Its value SHOULD be assigned and maintained by the original metadata set issuing authority.

```yaml
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
```

The value of `set.tracking.id` MUST NOT start or end with whitespace.

*Examples 1:*<a id='member-set-tracking-id-eg-1'></a><a id='sec-6-1-2-5-2-eg-1'></a><a id='example-7'></a>

```
7aedeb0a-22dd-428a-ab76-c950b43cbbc6
abcdef-orga-ds-0815
cisco-sa-20190513-secureboot
```

##### 6.1.2.5.3 Member `set.tracking.initial-release-date`<a id='member-set-tracking-initial-release-date'></a>

The `set.tracking.initial-release-date` member contains the date when this set was first published.

```yaml
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
```

The value of `set.tracking.initial-release-date` MUST be a valid date-time string conforming to \[RFC 3339\].

*Example 1:*<a id='member-set-tracking-initial-release-date-eg-1'></a><a id='sec-6-1-2-5-3-eg-1'></a><a id='example-8'></a>

```
2000-01-01T01:01:01Z
```

##### 6.1.2.5.4 Member `set.tracking.revision-history`<a id='member-set-tracking-revision-history'></a>

The `set.tracking.revision-history` member holds one revision item for each version of the DP-Core set, including the initial one. The sequence MUST contain at least one revision item.

```yaml
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
          legacy-version: String  # optional
      # ...
    # ...
  # ...
```

Each revision item MUST contain the following members:

- `date`: The date of the revision entry. MUST be a valid date-time string conforming to \[RFC 3339\].
- `number`: The version number of the revision. MUST conform to `$defs.version-type` (integer or semantic versioning string).
- `summary`: A short description of the changes made in this revision.

The optional `legacy-version` member traces entries back to historic, DP-Core-unaware version strings.

*Example 1:*<a id='member-set-tracking-revision-history-eg-1'></a><a id='sec-6-1-2-5-4-eg-1'></a><a id='example-9'></a>

```json
[
  {
    "date": "2000-01-01T01:01:01Z",
    "number": "1",
    "summary": "Initial version."
  }
]
```

##### 6.1.2.5.5 Member `set.tracking.status`<a id='member-set-tracking-status'></a>

The `set.tracking.status` member defines the draft status of the metadata set. This allows processing DP-Core sets of various maturity per version.

```yaml
DataProvenance:
  # ...
  set:
    # ...
    tracking:
      # ...
      status: String.Enum  # draft | final | interim
      # ...
    # ...
  # ...
```

The value of `set.tracking.status` MUST be one of the following:

- `draft`
- `final`
- `interim`

##### 6.1.2.5.6 Member `set.tracking.version`<a id='member-set-tracking-version'></a>

The `set.tracking.version` member specifies the version of the current DP-Core set.

```yaml
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
```

The value of `set.tracking.version` MUST conform to `$defs.version-type`, which requires either an integer or a semantic versioning string.

The value of `set.tracking.version` MUST equal the value of `number` in the most recent item of `set.tracking.revision-history`, that is the item with the latest `date`.

The `set.tracking.version` member versions the metadata set, not the dataset it describes, whose version is `source.data-version` ([6.1.3.6 "Member `source.data-version`"](#member-source-data-version)).
A revision that changes only the metadata advances `set.tracking.version` without changing `source.data-version`,
so the two values differ under normal operation (see the lineage example in [C.4 "Lineage Example"](#lineage-example)).

*Examples 1:*<a id='member-set-tracking-version-eg-1'></a><a id='sec-6-1-2-5-6-eg-1'></a><a id='example-10'></a>

```
1
2.0.0
1.0.0-beta+exp.sha.a1c44f85
```

##### 6.1.2.5.7 Member `set.tracking.aliases`<a id='member-set-tracking-aliases'></a>

The `set.tracking.aliases` member contains a list of alternate names for the same set.
Each alias MUST be a non-empty string and all entries MUST be unique.

```yaml
DataProvenance:
  # ...
  set:
    # ...
    tracking:
      # ...
      aliases:  # optional
        - String
      # ...
    # ...
  # ...
```

*Example 1:*<a id='member-set-tracking-aliases-eg-1'></a><a id='sec-6-1-2-5-7-eg-1'></a><a id='example-11'></a>

```json
["0bacba95-ceb9-4fae-bf07-d5683a9481c1"]
```

##### 6.1.2.5.8 Member `set.tracking.generator`<a id='member-set-tracking-generator'></a>

The `set.tracking.generator` member holds information about the engine that generated the metadata set.
The required sub-member is `engine`. The optional sub-member `date` MAY also be present.

```yaml
DataProvenance:
  # ...
  set:
    # ...
    tracking:
      # ...
      generator:  # optional
        engine:
          name: String
          version: $defs.version-type  # optional
        date: String.DateTime  # optional
    # ...
  # ...
```

- `engine.name`: The name of the tool or system that produced the metadata set.
- `engine.version`: The version of that tool. MUST conform to `$defs.version-type` when present.
- `date`: The date-time at which the metadata set was generated. MUST conform to \[RFC 3339\] when present.

*Example 1:*<a id='member-set-tracking-generator-eg-1'></a><a id='sec-6-1-2-5-8-eg-1'></a><a id='example-12'></a>

```json
{
  "engine": {"name": "DPCoreX", "version": "1.0.0"},
  "date": "2025-01-15T10:00:00Z"
}
```

#### 6.1.2.6 Member `set.language`<a id='member-set-language'></a>

The `set.language` member identifies the language used in this document, corresponding to IETF BCP 47 / RFC 5646.

```yaml
DataProvenance:
  # ...
  set:
    # ...
    language: $defs.language-type  # optional
    # ...
  # ...
```

*Examples 1:*<a id='member-set-language-eg-1'></a><a id='sec-6-1-2-6-eg-1'></a><a id='example-13'></a>

```
de
en
fr
```

#### 6.1.2.7 Member `set.source-language`<a id='member-set-source-language'></a>

The `set.source-language` member identifies the language this document was translated from, when this copy is a translation.

```yaml
DataProvenance:
  # ...
  set:
    # ...
    source-language: $defs.language-type  # optional
    # ...
  # ...
```

#### 6.1.2.8 Member `set.acknowledgments`<a id='member-set-acknowledgments'></a>

The `set.acknowledgments` member contains a list of acknowledgment elements associated with the whole set.
Each acknowledgment item MUST have at least one of the following members: `names`, `organization`, `summary`, or `urls`.

```yaml
DataProvenance:
  # ...
  set:
    # ...
    acknowledgments:  # optional; at least one of these members
      - names:
          - String
        organization: String
        summary: String
        urls:
          - String.URI
    # ...
  # ...
```

*Example 1:*<a id='member-set-acknowledgments-eg-1'></a><a id='sec-6-1-2-8-eg-1'></a><a id='example-14'></a>

```json
[
  {
    "names": ["A. Big Data"],
    "organization": "ETH Zurich",
    "summary": "First analysis of the merged data-set"
  }
]
```

#### 6.1.2.9 Member `set.notes`<a id='member-set-notes'></a>

The `set.notes` member contains a list of notes associated with this metadata set.
Each note MUST have a `category` and `text`. The optional members `audience` and `title` MAY also be present.
The `category` value MUST be one of: `general`, `other`, `privacy`, `summary`.

```yaml
DataProvenance:
  # ...
  set:
    # ...
    notes:  # optional
      - category: String.Enum
        text: String
        audience: String  # optional
        title: String     # optional
    # ...
  # ...
```

- `category`: The category of the note.
- `text`: The content of the note, varying depending on type.
- `audience`: The intended audience for the note.
- `title`: A concise description of what is contained in the text of the note.

#### 6.1.2.10 Member `set.references`<a id='member-set-references'></a>

The `set.references` member contains a list of references associated with this metadata set.
Each reference MUST have a `summary` and a `url`. The optional member `category` MAY also be present.
The `category` value MUST be one of: `external`, `self`.

```yaml
DataProvenance:
  # ...
  set:
    # ...
    references:  # optional
      - summary: String
        url: String.URI
        category: String.Enum  # optional
  # ...
```

- `summary`: A short description of what this reference refers to.
- `url`: The URL of the referenced resource.
- `category`: Whether this reference is external or self-referential (default: `external`).

### 6.1.3 Member `source`<a id='member-source'></a>

The `source` member characterizes the content and source of the dataset.
All six of its members are required.

```yaml
DataProvenance:
  # ...
  source:
    about: $defs.about-type
    id: $defs.identity-type
    issuer: $defs.orga-type
    location: String.URI
    name: String
    data-version: $defs.version-type
  # ...
```

The members of `source` are described in the following subsections.

#### 6.1.3.1 Member `source.about`<a id='member-source-about'></a>

The `source.about` member contains a detailed narrative that explains the contents, scope, and purpose of the dataset.
The required members are `content` and `purpose`. The optional member `scope` MAY also be present.

```yaml
DataProvenance:
  # ...
  source:
    about:
      content: String
      purpose: String
      scope: String  # optional
    # ...
  # ...
```

- `content`: Provides essential contextual information that helps users understand what the data represents and how it was collected.
- `purpose`: Explains the recommended uses.
- `scope`: Points out any limitations of the dataset.

*Example 1:*<a id='member-source-about-eg-1'></a><a id='sec-6-1-3-1-eg-1'></a><a id='example-15'></a>

```json
{
  "content": "We found these numbers on the parking lot.",
  "purpose": "Use only for learning regression modeling. Not for production use.",
  "scope": "We did not verify anything. Use at your own risk."
}
```

#### 6.1.3.2 Member `source.id`<a id='member-source-id'></a>

The `source.id` member provides a unique identifier for the dataset's metadata. At least one identification method MUST be provided.

```yaml
DataProvenance:
  # ...
  source:
    # ...
    id:  # at least one of these members
      hashes:
        - tree-hashes:
            - algorithm: String
              value: String.Pattern
          path: String
      uris:
        - String.URI
      uuids:
        - String
      custom-ids:
        - method: String
          value: String
          tool: String  # optional
          parameter-list:  # optional
            - String
    # ...
  # ...
```

The following identification methods are available:

- `hashes`: A list of cryptographic hash entries, each containing `tree-hashes` (a list of `{algorithm, value}` pairs) and a `path`.
- `uris`: A list of identifiers in URI format.
- `uuids`: A list of identifiers in UUID format.
- `custom-ids`: A list of identifiers in any text format, each with a required `method` and `value`, and optional `tool` and `parameter-list`.

The value of `algorithm` MUST be lowercase.

*Examples:*

- sha256
- sha384
- sha512
- blake2b512
- sha3-512

`source.id` identifies the dataset itself. It is distinct from `set.tracking.id`, which identifies this metadata record.

*Example 1:*<a id='member-source-id-eg-1'></a><a id='sec-6-1-3-2-eg-1'></a><a id='example-16'></a>

```json
{
  "uuids": ["e5471657-9ede-4335-843b-c1376ef29bfa"]
}
```

*Example 2:*<a id='member-source-id-eg-2'></a><a id='sec-6-1-3-2-eg-2'></a><a id='example-17'></a>

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

#### 6.1.3.3 Member `source.issuer`<a id='member-source-issuer'></a>

The `source.issuer` member identifies the legal entity or entities responsible for creating the dataset.
The value is a sequence of organization objects. Each organization MUST provide a `legal-name`.
The sequence MUST contain at least one organization and all entries MUST be unique for the organization record members — `legal-name`, `address`, and `url` together — not by `legal-name` alone.
The optional members `address` and `url` MAY also be present in each organization.

```yaml
DataProvenance:
  # ...
  source:
    # ...
    issuer:
      - legal-name: String
        address: $defs.address-type  # optional
        url: String.URI              # optional
    # ...
  # ...
```

*Example 1:*<a id='member-source-issuer-eg-1'></a><a id='sec-6-1-3-3-eg-1'></a><a id='example-18'></a>

```json
[
  {
    "legal-name": "Sampling Ltd.",
    "url": "https://example.com/smplng/about"
  }
]
```

#### 6.1.3.4 Member `source.location`<a id='member-source-location'></a>

The `source.location` member provides the web address where the dataset's metadata is published and can be accessed. Typically this will be a unique URI of the current dataset.

```yaml
DataProvenance:
  # ...
  source:
    # ...
    location: String.URI
    # ...
  # ...
```

#### 6.1.3.5 Member `source.name`<a id='member-source-name'></a>

The `source.name` member provides the official name of the dataset, which should be descriptive and help easily identify the dataset's content and purpose.

```yaml
DataProvenance:
  # ...
  source:
    # ...
    name: String
    # ...
  # ...
```

#### 6.1.3.6 Member `source.data-version`<a id='member-source-data-version'></a>

The `source.data-version` member specifies the version of the dataset this DP-Core set describes, allowing the dataset to evolve over time and keeping consistent labeling.

```yaml
DataProvenance:
  # ...
  source:
    # ...
    data-version: $defs.version-type
  # ...
```

The value of `source.data-version` MUST conform to `$defs.version-type`, which requires either an integer or a semantic versioning string.

The `source.data-version` member versions the dataset, independently of the version of the metadata set in `set.tracking.version` ([6.1.2.5.6 "Member `set.tracking.version`"](#member-set-tracking-version)).
It advances only when a revision changes the dataset itself, so the two values differ under normal operation (see the lineage example in [C.4 "Lineage Example"](#lineage-example)).

*Examples 1:*<a id='member-source-data-version-eg-1'></a><a id='sec-6-1-3-6-eg-1'></a><a id='example-19'></a>

```
1
2.0.0
```

### 6.1.4 Member `provenance`<a id='member-provenance'></a>

The `provenance` member describes the provenance of the dataset.

The required members are `origin-geography`, `date`, and `generation-method`.
The optional members `source`, `origin`, `previous-date`, `generation-period`, `format`, and `sub-provenance` MAY also be present.

```yaml
DataProvenance:
  # ...
  provenance:
    origin-geography: $defs.geographic-regions-type
    date: String.Date
    generation-method: Sequence
    source: String.URI                     # optional
    origin: $defs.orga-type                # optional
    previous-date: String.Date             # optional
    generation-period: Mapping             # optional
    format: Sequence                       # optional
    sub-provenance: $defs.provenance-type  # optional
    source-digest: Mapping                 # optional
  # ...
```

The required members of `provenance` are described in subsections 7.1.4.1–7.1.4.3; optional members in 7.1.4.4–7.1.4.9.

#### 6.1.4.1 Member `provenance.origin-geography`<a id='member-provenance-origin-geography'></a>

The `provenance.origin-geography` member identifies the geographical locations where the data was originally collected, which can be important for compliance with regional laws and understanding the data's context.

The value is a sequence of geographic region objects. Each entry MUST contain a `country`. The optional `state` member MAY also be present. The sequence MUST contain at least one entry and all entries MUST be unique.

```yaml
DataProvenance:
  # ...
  provenance:
    origin-geography:
      - country: String
        state: String  # optional
    # ...
  # ...
```

*Example 1:*<a id='member-provenance-origin-geography-eg-1'></a><a id='sec-6-1-4-1-eg-1'></a><a id='example-20'></a>

```json
[
  {"country": "US"},
  {"country": "DE", "state": "Bavaria"}
]
```

#### 6.1.4.2 Member `provenance.date`<a id='member-provenance-date'></a>

The `provenance.date` member provides the date when the dataset was compiled or created, providing a temporal context for the data.

```yaml
DataProvenance:
  # ...
  provenance:
    # ...
    date: String.Date
    # ...
  # ...
```

The value of `provenance.date` MUST be a valid date string in full-date format (YYYY-MM-DD).

*Example 1:*<a id='member-provenance-date-eg-1'></a><a id='sec-6-1-4-2-eg-1'></a><a id='example-21'></a>

```
2000-01-01
```

#### 6.1.4.3 Member `provenance.generation-method`<a id='member-provenance-generation-method'></a>

The `provenance.generation-method` member describes the methodology or procedures used to collect, generate, or compile the data, giving insight into its reliability and validity.

The value is a sequence of method objects. Each method MUST contain a `code` drawn from the `GenerationMethodCode` vocabulary. The optional members `system` and `long-description` MAY also be present. The sequence MUST contain at least one method and all entries MUST be unique.

```yaml
DataProvenance:
  # ...
  provenance:
    # ...
    generation-method:
      - code: $defs.generation-method-code-type
        system: String            # optional
        long-description: String  # optional
    # ...
  # ...
```

*Example 1:*<a id='member-provenance-generation-method-eg-1'></a><a id='sec-6-1-4-3-eg-1'></a><a id='example-22'></a>

```json
[
  {"code": "web-scraping-crawling"},
  {"code": "primary-user-source", "long-description": "Direct survey responses from participants."}
]
```

#### 6.1.4.4 Member `provenance.source`<a id='member-provenance-source'></a>

The `provenance.source` member identifies where the metadata for the source dataset contributing to the current dataset can be found, establishing lineage.

```yaml
DataProvenance:
  # ...
  provenance:
    # ...
    source: String.URI  # optional
    # ...
  # ...
```

The value of `provenance.source` MUST be a valid URI.

*Example 1:*<a id='member-provenance-source-eg-1'></a><a id='sec-6-1-4-4-eg-1'></a><a id='example-23'></a>

```
https://example.com/datasets/source-dataset-42/provenance.json
```

#### 6.1.4.5 Member `provenance.origin`<a id='member-provenance-origin'></a>

The `provenance.origin` member identifies the original source organization when it differs from the issuer of the dataset.
The value is a sequence of organization objects following the same structure as `source.issuer`.

```yaml
DataProvenance:
  # ...
  provenance:
    # ...
    origin:  # optional
      - legal-name: String
        address: $defs.address-type  # optional
        url: String.URI              # optional
    # ...
  # ...
```

*Example 1:*<a id='member-provenance-origin-eg-1'></a><a id='sec-6-1-4-5-eg-1'></a><a id='example-24'></a>

```json
[{"legal-name": "Original Data Collector Inc."}]
```

#### 6.1.4.6 Member `provenance.previous-date`<a id='member-provenance-previous-date'></a>

The `provenance.previous-date` member provides the release date of the previous version of the dataset, to track changes and updates over time.

```yaml
DataProvenance:
  # ...
  provenance:
    # ...
    previous-date: String.Date  # optional
    # ...
  # ...
```

The value of `provenance.previous-date` MUST be a valid date string in full-date format (YYYY-MM-DD).

*Example 1:*<a id='member-provenance-previous-date-eg-1'></a><a id='sec-6-1-4-6-eg-1'></a><a id='example-25'></a>

```
1999-06-15
```

#### 6.1.4.7 Member `provenance.generation-period`<a id='member-provenance-generation-period'></a>

The `provenance.generation-period` member describes the span of time during which the data within the dataset was collected or generated.
Both `start` and `end` are optional but MUST each conform to \[RFC 3339\] when present.

```yaml
DataProvenance:
  # ...
  provenance:
    # ...
    generation-period:  # optional
      start: String.DateTime  # optional
      end: String.DateTime    # optional
    # ...
  # ...
```

*Example 1:*<a id='member-provenance-generation-period-eg-1'></a><a id='sec-6-1-4-7-eg-1'></a><a id='example-26'></a>

```json
{
  "start": "1998-01-01T00:00:00Z",
  "end": "1999-12-31T23:59:59Z"
}
```

#### 6.1.4.8 Member `provenance.format`<a id='member-provenance-format'></a>

The `provenance.format` member describes the modality or media type of the data within the dataset.
The value is a sequence of `ModalityFormat` values. The sequence MUST contain at least one entry and all entries MUST be unique.

```yaml
DataProvenance:
  # ...
  provenance:
    # ...
    format:  # optional
      - String.Enum  # application/json | application/jsonld | application/msword | application/vnd.ms-excel | application/zip | image/bmp | image/gif | image/jpeg | image/png | image/x-png | other | text/csv | text/plain
    # ...
  # ...
```

*Example 1:*<a id='member-provenance-format-eg-1'></a><a id='sec-6-1-4-8-eg-1'></a><a id='example-27'></a>

```json
["text/csv", "application/json"]
```

#### 6.1.4.9 Member `provenance.sub-provenance`<a id='member-provenance-sub-provenance'></a>

The `provenance.sub-provenance` member holds provenance information for a component of the current dataset, enabling a recursive provenance tree.
Its structure is identical to the enclosing `provenance` member.

```yaml
DataProvenance:
  # ...
  provenance:
    # ...
    sub-provenance:  # optional
      origin-geography: $defs.geographic-regions-type
      date: String.Date
      generation-method:
        - $defs.generation-method-item-type
      source: String.URI          # optional
      origin: $defs.orga-type     # optional
      previous-date: String.Date  # optional
      generation-period:  # optional
        start: String.DateTime  # optional
        end: String.DateTime    # optional
      format:  # optional
        - String.Enum
      sub-provenance: $defs.provenance-type  # optional
      source-digest:  # optional
        algorithm: String
        value: String.Pattern
    # ...
  # ...
```

#### 6.1.4.10 Member `provenance.source-digest`<a id='member-provenance-source-digest'></a>

The `provenance.source-digest` member records a cryptographic digest of the metadata record that `provenance.source` references,
computed when the current record is issued.
It lets a consumer who retrieves the referenced record check that it is the record the current one was issued against.

```yaml
DataProvenance:
  # ...
  provenance:
    # ...
    source-digest:  # optional
      algorithm: String
      value: String.Pattern
  # ...
```

The value MUST contain the members `algorithm` and `value`.
The `algorithm` member names the digest algorithm, for example `sha256`, and MUST be a non-empty string.
The `value` member MUST be the hex-encoded digest value with at least 32 hexadecimal digits.

*Example 1:*<a id='member-provenance-source-digest-eg-1'></a><a id='sec-6-1-4-10-eg-1'></a><a id='example-28'></a>

```
{
  "algorithm": "sha256",
  "value": "bb121f5f3ae0ee44d8e21d50b92ed8bcdd1f3a20887615b2f81083a6edf190e5"
}
```

### 6.1.5 Member `use`<a id='member-use'></a>

The `use` member describes legal use and restrictions that apply to the dataset.

The only required member is `intended-purpose`. All other members are optional.

```yaml
DataProvenance:
  # ...
  use:
    intended-purpose: Sequence
    classification: Sequence                            # optional
    consents: Sequence                                  # optional
    data-risk-reducing: Sequence                        # optional
    processing-included: $defs.geographic-regions-type  # optional
    processing-excluded: $defs.geographic-regions-type  # optional
    storage-allowed: $defs.geographic-regions-type      # optional
    storage-forbidden: $defs.geographic-regions-type    # optional
    license: Sequence                                   # optional
    copyright: Sequence                                 # optional
    patent: Sequence                                    # optional
    trademark: Sequence                                 # optional
  # ...
```

#### 6.1.5.1 Member `use.intended-purpose`<a id='member-use-intended-purpose'></a>

The `use.intended-purpose` member describes the purpose for which the dataset was created, guiding users on its intended use and potential applications.

The value is a sequence of purpose objects. Each purpose MUST contain a `code` drawn from the `PurposeCode` vocabulary and a `long-description`. The optional `system` member MAY also be present. The sequence MUST contain at least one purpose and all entries MUST be unique.

```yaml
DataProvenance:
  # ...
  use:
    intended-purpose:
      - code: $defs.purpose-code-type
        long-description: String
        system: String  # optional
    # ...
  # ...
```

*Example 1:*<a id='member-use-intended-purpose-eg-1'></a><a id='sec-6-1-5-1-eg-1'></a><a id='example-29'></a>

```json
[
  {
    "code": "research",
    "long-description": "Use only for learning regression modeling. Not for production use."
  }
]
```

#### 6.1.5.2 Member `use.classification`<a id='member-use-classification'></a>

The `use.classification` member indicates whether the dataset includes data falling into various confidentiality classifications.
The value is a sequence of classification objects. Each item MUST contain a `regulation` object whose `code` MUST be drawn from the `ConfidentialityCode` vocabulary, and an `evaluated` boolean. The optional `tool` member MAY also be present. All entries MUST be unique.

```yaml
DataProvenance:
  # ...
  use:
    # ...
    classification:  # optional
      - regulation: $defs.confidentiality-regulation-type
        evaluated: Boolean
        tool: String  # optional
    # ...
  # ...
```

*Example 1:*<a id='member-use-classification-eg-1'></a><a id='sec-6-1-5-2-eg-1'></a><a id='example-30'></a>

```json
[
  {"regulation": {"code": "phi"}, "evaluated": true},
  {"regulation": {"code": "pii"}, "evaluated": false}
]
```

#### 6.1.5.3 Member `use.consents`<a id='member-use-consents'></a>

The `use.consents` member specifies where consent documentation or agreements related to the data can be found, ensuring legal compliance and regulatory use.
The value is a sequence of strings. The sequence MUST contain at least one entry and all entries MUST be unique.

```yaml
DataProvenance:
  # ...
  use:
    # ...
    consents:  # optional
      - String
    # ...
  # ...
```

*Example 1:*<a id='member-use-consents-eg-1'></a><a id='sec-6-1-5-3-eg-1'></a><a id='example-31'></a>

```json
["https://example.com/consent-policy-2024"]
```

#### 6.1.5.4 Member `use.data-risk-reducing`<a id='member-use-data-risk-reducing'></a>

The `use.data-risk-reducing` member indicates the techniques used to reduce known data risk.
The value is a sequence of objects. Each item MUST contain `tool-used`. The optional members `tool-category`, `technology`, `parameters`, and `results` MAY also be present. All entries MUST be unique.

```yaml
DataProvenance:
  # ...
  use:
    # ...
    data-risk-reducing:  # optional
      - tool-used: String
        tool-category: $defs.method-type  # optional
        technology: String.Enum           # optional
        parameters:  # optional
          - name: String
            value: String  # optional
        results:  # optional
          - String
    # ...
  # ...
```

*Example 1:*<a id='member-use-data-risk-reducing-eg-1'></a><a id='sec-6-1-5-4-eg-1'></a><a id='example-32'></a>

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

#### 6.1.5.5 Member `use.processing-included`<a id='member-use-processing-included'></a>

The `use.processing-included` member defines the geographical boundaries within which the data MAY be processed.
The value is a sequence of geographic region objects following the same structure as `provenance.origin-geography`.

```yaml
DataProvenance:
  # ...
  use:
    # ...
    processing-included:  # optional
      - country: String
        state: String  # optional
    # ...
  # ...
```

*Example 1:*<a id='member-use-processing-included-eg-1'></a><a id='sec-6-1-5-5-eg-1'></a><a id='example-33'></a>

```json
[{"country": "DE"}, {"country": "FR"}]
```

#### 6.1.5.6 Member `use.processing-excluded`<a id='member-use-processing-excluded'></a>

The `use.processing-excluded` member defines the geographical boundaries within which the data MUST NOT be processed.
The value is a sequence of geographic region objects following the same structure as `provenance.origin-geography`.

```yaml
DataProvenance:
  # ...
  use:
    # ...
    processing-excluded:  # optional
      - country: String
        state: String  # optional
    # ...
  # ...
```

#### 6.1.5.7 Member `use.storage-allowed`<a id='member-use-storage-allowed'></a>

The `use.storage-allowed` member specifies geographical locations where the data MAY be stored.
The value is a sequence of geographic region objects following the same structure as `provenance.origin-geography`.

```yaml
DataProvenance:
  # ...
  use:
    # ...
    storage-allowed:  # optional
      - country: String
        state: String  # optional
    # ...
  # ...
```

#### 6.1.5.8 Member `use.storage-forbidden`<a id='member-use-storage-forbidden'></a>

The `use.storage-forbidden` member specifies geographical locations where the data MUST NOT be stored.
The value is a sequence of geographic region objects following the same structure as `provenance.origin-geography`.

```yaml
DataProvenance:
  # ...
  use:
    # ...
    storage-forbidden:  # optional
      - country: String
        state: String  # optional
    # ...
  # ...
```

#### 6.1.5.9 Member `use.license`<a id='member-use-license'></a>

The `use.license` member details the terms under which the dataset can be used, including any restrictions or obligations.
License entries MAY include End User License Agreements (EULA) or Data Use Agreements (DUA).
The value is a sequence of strings. The sequence MUST contain at least one entry and all entries MUST be unique.

```yaml
DataProvenance:
  # ...
  use:
    # ...
    license:  # optional
      - String
    # ...
  # ...
```

*Example 1:*<a id='member-use-license-eg-1'></a><a id='sec-6-1-5-9-eg-1'></a><a id='example-34'></a>

```json
["https://creativecommons.org/licenses/by/4.0/"]
```

#### 6.1.5.10 Member `use.copyright`<a id='member-use-copyright'></a>

The `use.copyright` member indicates whether the dataset contains proprietary information covered by a copyright, and the terms of that copyright.
The value is a sequence of strings. The sequence MUST contain at least one entry and all entries MUST be unique.

```yaml
DataProvenance:
  # ...
  use:
    # ...
    copyright:  # optional
      - String
    # ...
  # ...
```

*Example 1:*<a id='member-use-copyright-eg-1'></a><a id='sec-6-1-5-10-eg-1'></a><a id='example-35'></a>

```json
["Copyright © 2024 Example Corp. All rights reserved."]
```

#### 6.1.5.11 Member `use.patent`<a id='member-use-patent'></a>

The `use.patent` member indicates whether the dataset contains proprietary information covered by a patent, and the patent number.
The value is a sequence of strings. The sequence MUST contain at least one entry and all entries MUST be unique.

```yaml
DataProvenance:
  # ...
  use:
    # ...
    patent:  # optional
      - String
    # ...
  # ...
```

#### 6.1.5.12 Member `use.trademark`<a id='member-use-trademark'></a>

The `use.trademark` member indicates whether the dataset contains proprietary information covered by a trademark, and the terms of that trademark.
The value is a sequence of strings. The sequence MUST contain at least one entry and all entries MUST be unique.

```yaml
DataProvenance:
  # ...
  use:
    # ...
    trademark:  # optional
      - String
  # ...
```

### 6.1.6 Member `proof`<a id='member-proof'></a>

The `proof` member is reserved for the proof material of an external integrity or signing envelope, such as a signature over the record.
Its internal structure is opaque to this specification: a record defines only where such material is carried, not how it is produced or verified
(see section [8.1 "Integrity and Authenticity of Provenance Claims"](#integrity-and-authenticity)).

```yaml
DataProvenance:
  # ...
  proof: Mapping  # optional
```

The value of `proof`, when present, MUST be a JSON object.

---

# 7. Provenance Schema<a id='provenance-schema'></a>

The property tables of this section give, for each type, its members with their type, cardinality, and description.
They are generated from the JADN encoding of the information model (section [5.1 "JADN Encoding"](#jadn-encoding)),
which is generated from the JSON schema, the normative definition of the format.

The Data Provenance Standards record metadata elements in three segmented categories: Source, Provenance, and Use.

[Figure 1](#fig:metadata), generated from the JSON schema like the tables, shows the root type with the type of each of its members.

<a id="fig:metadata"></a>
![Overview of the record: the root type and the type of each member](images/metadata.svg)

Figure 1: Overview of the record: the root type and the type of each member

The property tables first define metadata about the specification itself,
then describe how a record is made of the 3 primary metadata elements.
The three segmented categories (Source, Provenance, and Use) are comprised of various
metadata element input fields. Each field is described in more detail in section [6 "Provenance Data Model Encoding"](#provenance-data-model-encoding).

## 7.1 Primary Metadata Elements<a id='primary-metadata-elements'></a>

The root object of a Data Provenance Metadata record contains five required members.


<a id="tab:data-provenance-record"></a>
Table 1: Type `DataProvenance` (Record)

| ID | Name       | Type        | \#   | Description                                                                                                                                             |
|---:|:-----------|:------------|:-----|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | $schema    | String /uri | 1    | The URI identifying the schema this JSON object must be valid against. For this version the value is always the URI of the data-provenance JSON schema. |
|  2 | set        | Set         | 1    | Set-level metadata about this provenance metadata record.                                                                                               |
|  3 | source     | Source      | 1    | Characterizes the content and source of the dataset.                                                                                                    |
|  4 | provenance | Provenance  | 1    | Describes the provenance of the dataset.                                                                                                                |
|  5 | use        | Use         | 1    | Describes legal use and restrictions that apply to the dataset.                                                                                         |
|  6 | proof      | Proof       | 0..1 | Reserved for an external integrity or signing envelope's proof material. The internal structure is opaque to this specification.                        |



<a id="tab:proof-map"></a>
Table 2: Type `Proof` (Map)

| Type Name | Type Definition | Description                                                                                                                      |
|:----------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------|
| Proof     | Map             | Reserved for an external integrity or signing envelope's proof material. The internal structure is opaque to this specification. |


## 7.2 Set<a id='set'></a>

The `set` member captures metadata about the provenance metadata record itself.


<a id="tab:set-record"></a>
Table 3: Type `Set` (Record)

| ID | Name            | Type           | \#    | Description                                                                                                                        |
|---:|:----------------|:---------------|:------|:-----------------------------------------------------------------------------------------------------------------------------------|
|  1 | category        | String         | 1     | A short canonical name, chosen by the set producer, informing the end user of the category of the metadata set.                    |
|  2 | schema-version  | String         | 1     | The version of the Data Provenance Core specification this record was generated for. The value for this version is always `"1.0"`. |
|  3 | publisher       | Publisher      | 1     | Information about the publisher of the metadata set.                                                                               |
|  4 | label           | String         | 1     | The per-publisher unique title of this metadata set.                                                                               |
|  5 | tracking        | Tracking       | 1     | Management attributes used to track this metadata set as a whole.                                                                  |
|  6 | language        | Language       | 0..1  | The language used in this document, corresponding to IETF BCP 47.                                                                  |
|  7 | source-language | Language       | 0..1  | If this is a translation, the language this document was translated from.                                                          |
|  8 | acknowledgments | Acknowledgment | 0..\* | Acknowledgment elements associated with the whole set.                                                                             |
|  9 | notes           | Note           | 0..\* | Notes associated with this metadata set.                                                                                           |
| 10 | references      | Reference      | 0..\* | References associated with this metadata set.                                                                                      |



<a id="tab:publisher-record"></a>
Table 4: Type `Publisher` (Record)

| ID | Name            | Type        | \#   | Description                                                                                        |
|---:|:----------------|:------------|:-----|:---------------------------------------------------------------------------------------------------|
|  1 | name            | String      | 1    | The name of the issuing party.                                                                     |
|  2 | namespace       | String /uri | 1    | A URI under the control of the issuing party, used as a globally unique identifier for that party. |
|  3 | contact-details | String      | 0..1 | Information on how to contact the publisher.                                                       |



<a id="tab:tracking-record"></a>
Table 5: Type `Tracking` (Record)

| ID | Name                 | Type              | \#    | Description                                                                                                                                  |
|---:|:---------------------|:------------------|:------|:---------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | current-release-date | String /date-time | 1     | The date when the current revision of this document was released.                                                                            |
|  2 | id                   | String            | 1     | A unique identifier for this metadata set, assigned and maintained by the original issuing authority. MUST NOT start or end with whitespace. |
|  3 | initial-release-date | String /date-time | 1     | The date when this metadata set was first published.                                                                                         |
|  4 | revision-history     | Revision          | 1..\* | One revision item for each version of the metadata set, including the initial one.                                                           |
|  5 | status               | TrackingStatus    | 1     | The draft status of the metadata set.                                                                                                        |
|  6 | version              | Version           | 1     | The version of the current metadata set.                                                                                                     |
|  7 | aliases              | String            | 0..\* | Alternate names for this metadata set.                                                                                                       |
|  8 | generator            | Generator         | 0..1  | Information about the engine that generated this metadata set.                                                                               |



<a id="tab:tracking-status-enum"></a>
Table 6: Type `TrackingStatus` (Enumerated)

| ID | Item    | Description                          |
|---:|:--------|:-------------------------------------|
|  1 | draft   | The metadata set is a draft.         |
|  2 | final   | The metadata set is final.           |
|  3 | interim | The metadata set has interim status. |



<a id="tab:revision-record"></a>
Table 7: Type `Revision` (Record)

| ID | Name           | Type              | \#   | Description                                                                                                    |
|---:|:---------------|:------------------|:-----|:---------------------------------------------------------------------------------------------------------------|
|  1 | date           | String /date-time | 1    | The date of this revision entry.                                                                               |
|  2 | number         | Version           | 1    | The version number of this revision.                                                                           |
|  3 | summary        | String            | 1    | A short description of the changes in this revision.                                                           |
|  4 | legacy-version | String            | 0..1 | A version string from an existing set with the same content, tracing from DP-Core compliant to historic items. |



<a id="tab:generator-record"></a>
Table 8: Type `Generator` (Record)

| ID | Name   | Type              | \#   | Description                                                      |
|---:|:-------|:------------------|:-----|:-----------------------------------------------------------------|
|  1 | engine | GeneratorEngine   | 1    | Information about the engine used to generate this metadata set. |
|  2 | date   | String /date-time | 0..1 | The date this metadata set was generated.                        |



<a id="tab:generator-engine-record"></a>
Table 9: Type `GeneratorEngine` (Record)

| ID | Name    | Type    | \#   | Description                                                 |
|---:|:--------|:--------|:-----|:------------------------------------------------------------|
|  1 | name    | String  | 1    | The name of the engine that generated this metadata set.    |
|  2 | version | Version | 0..1 | The version of the engine that generated this metadata set. |



<a id="tab:note-record"></a>
Table 10: Type `Note` (Record)

| ID | Name     | Type         | \#   | Description                                                         |
|---:|:---------|:-------------|:-----|:--------------------------------------------------------------------|
|  1 | category | NoteCategory | 1    | The category of the note.                                           |
|  2 | text     | String       | 1    | The content of the note, varying depending on type.                 |
|  3 | audience | String       | 0..1 | The intended audience for the note.                                 |
|  4 | title    | String       | 0..1 | A concise description of what is contained in the text of the note. |



<a id="tab:note-category-enum"></a>
Table 11: Type `NoteCategory` (Enumerated)

| ID | Item             | Description                                    |
|---:|:-----------------|:-----------------------------------------------|
|  1 | description      | A descriptive note about the subject.          |
|  2 | details          | A note with detailed supplemental information. |
|  3 | faq              | A note in frequently-asked-questions format.   |
|  4 | general          | A general note.                                |
|  5 | legal_disclaimer | A note containing a legal disclaimer.          |
|  6 | other            | A note that does not fit other categories.     |
|  7 | summary          | A summary note.                                |



<a id="tab:reference-record"></a>
Table 12: Type `Reference` (Record)

| ID | Name     | Type              | \#   | Description                                             |
|---:|:---------|:------------------|:-----|:--------------------------------------------------------|
|  1 | summary  | String            | 1    | A short description of what this reference refers to.   |
|  2 | url      | String /uri       | 1    | The URL of the referenced resource.                     |
|  3 | category | ReferenceCategory | 0..1 | Whether this reference is external or self-referential. |



<a id="tab:reference-category-enum"></a>
Table 13: Type `ReferenceCategory` (Enumerated)

| ID | Item     | Description                                                      |
|---:|:---------|:-----------------------------------------------------------------|
|  1 | external | The reference points to an external resource.                    |
|  2 | self     | The reference points back to the same information item in focus. |


## 7.3 Source<a id='source'></a>

The `source` member characterizes the content and source of the dataset.


<a id="tab:source-record"></a>
Table 14: Type `Source` (Record)

| ID | Name         | Type         | \#    | Description                                                                      |
|---:|:-------------|:-------------|:------|:---------------------------------------------------------------------------------|
|  1 | about        | About        | 1     | A detailed narrative explaining the contents, scope, and purpose of the dataset. |
|  2 | id           | Identity     | 1     | A unique identifier for this dataset, using at least one identification method.  |
|  3 | issuer       | Organization | 1..\* | The legal entity or entities responsible for creating the dataset.               |
|  4 | location     | String /uri  | 1     | The web address where this dataset's metadata is published and can be accessed.  |
|  5 | name         | String       | 1     | The official name of the dataset.                                                |
|  6 | data-version | Version      | 1     | The version of the dataset this metadata set describes.                          |



<a id="tab:about-record"></a>
Table 15: Type `About` (Record)

| ID | Name    | Type   | \#   | Description                                                                                        |
|---:|:--------|:-------|:-----|:---------------------------------------------------------------------------------------------------|
|  1 | content | String | 1    | Contextual information helping users understand what the data represents and how it was collected. |
|  2 | purpose | String | 1    | The recommended uses for this dataset.                                                             |
|  3 | scope   | String | 0..1 | Any limitations of the dataset.                                                                    |


The `Identity` type provides at least one identifier for the dataset. At least one of its fields MUST be present.


<a id="tab:identity-map"></a>
Table 16: Type `Identity` (Map)

| ID | Name       | Type         | \#    | Description                                           |
|---:|:-----------|:-------------|:------|:------------------------------------------------------|
|  1 | hashes     | HashEntry    | 0..\* | Cryptographic hash-based identifiers for the dataset. |
|  2 | uris       | String /uri  | 0..\* | URI identifiers for the dataset.                      |
|  3 | uuids      | String /uuid | 0..\* | UUID identifiers for the dataset.                     |
|  4 | custom-ids | CustomId     | 0..\* | Identifiers in any text format.                       |



<a id="tab:hash-entry-record"></a>
Table 17: Type `HashEntry` (Record)

| ID | Name        | Type     | \#    | Description                                                              |
|---:|:------------|:---------|:------|:-------------------------------------------------------------------------|
|  1 | tree-hashes | TreeHash | 1..\* | The cryptographic hash values for this file or tree.                     |
|  2 | path        | String   | 1     | The path (file or filesystem tree root) identified by these hash values. |



<a id="tab:tree-hash-record"></a>
Table 18: Type `TreeHash` (Record)

| ID | Name      | Type   | \# | Description                                                              |
|---:|:----------|:-------|:---|:-------------------------------------------------------------------------|
|  1 | algorithm | String | 1  | The name of the hash or tree/seal algorithm used to calculate the value. |
|  2 | value     | String | 1  | The cryptographic hash value in hexadecimal representation.              |



<a id="tab:custom-id-record"></a>
Table 19: Type `CustomId` (Record)

| ID | Name           | Type   | \#    | Description                                            |
|---:|:---------------|:-------|:------|:-------------------------------------------------------|
|  1 | method         | String | 1     | The name of the method used to derive this identifier. |
|  2 | value          | String | 1     | The identifier value.                                  |
|  3 | tool           | String | 0..1  | The name of the tool used to derive this identifier.   |
|  4 | parameter-list | String | 0..\* | Parameters used when invoking the tool.                |


## 7.4 Provenance<a id='provenance'></a>

The `provenance` member describes the provenance of the dataset.


<a id="tab:provenance-record"></a>
Table 20: Type `Provenance` (Record)

| ID | Name              | Type             | \#    | Description                                                                                  |
|---:|:------------------|:-----------------|:------|:---------------------------------------------------------------------------------------------|
|  1 | origin-geography  | GeographicRegion | 1..\* | The geographical locations where the data was originally collected.                          |
|  2 | date              | String /date     | 1     | The date when the dataset was compiled or created (YYYY-MM-DD).                              |
|  3 | generation-method | GenerationMethod | 1..\* | The methodology or procedures used to collect, generate, or compile the data.                |
|  4 | source            | String /uri      | 0..1  | The URI of metadata for a source dataset contributing to this dataset, establishing lineage. |
|  5 | origin            | Organization     | 0..\* | The original source organization, if different from the dataset issuer.                      |
|  6 | previous-date     | String /date     | 0..1  | The release date of the previous version of this dataset (YYYY-MM-DD).                       |
|  7 | generation-period | GenerationPeriod | 0..1  | The span of time during which the data was collected or generated.                           |
|  8 | format            | ModalityFormat   | 0..\* | Describes the modality or media type of the data within the dataset.                         |
|  9 | sub-provenance    | Provenance       | 0..1  | Nested provenance information for a component of this dataset.                               |
| 10 | source-digest     | SourceDigest     | 0..1  | A cryptographic digest of the record referenced by `source`, computed at issuance.           |



<a id="tab:source-digest-record"></a>
Table 21: Type `SourceDigest` (Record)

| ID | Name      | Type   | \# | Description                                                |
|---:|:----------|:-------|:---|:-----------------------------------------------------------|
|  1 | algorithm | String | 1  | Digest algorithm identifier (e.g. sha256, sha384, sha512). |
|  2 | value     | String | 1  | The digest value, hex-encoded.                             |



<a id="tab:generation-period-record"></a>
Table 22: Type `GenerationPeriod` (Record)

| ID | Name  | Type              | \#   | Description                                            |
|---:|:------|:------------------|:-----|:-------------------------------------------------------|
|  1 | start | String /date-time | 0..1 | The start of the data collection or generation period. |
|  2 | end   | String /date-time | 0..1 | The end of the data collection or generation period.   |



<a id="tab:generation-method-record"></a>
Table 23: Type `GenerationMethod` (Record)

| ID | Name             | Type                 | \#   | Description                                       |
|---:|:-----------------|:---------------------|:-----|:--------------------------------------------------|
|  1 | code             | GenerationMethodCode | 1    | A short code identifying the generation method.   |
|  2 | system           | String               | 0..1 | The code system used to interpret the code value. |
|  3 | long-description | String               | 0..1 | A detailed description of the method.             |



<a id="tab:generation-method-code-enum"></a>
Table 24: Type `GenerationMethodCode` (Enumerated)

| ID | Item                     | Description                                            |
|---:|:-------------------------|:-------------------------------------------------------|
|  1 | data-augmentation        | Data generation through augmentation of existing data. |
|  2 | data-mining              | Data collected through automated data mining.          |
|  3 | feeds                    | Data received through data feeds.                      |
|  4 | machine-generated-ml-ops | Data generated through machine learning operations.    |
|  5 | other                    | A generation method not listed here.                   |
|  6 | primary-user-source      | Data collected directly from primary users.            |
|  7 | simulations              | Data generated through simulations.                    |
|  8 | social-media             | Data collected from social media platforms.            |
|  9 | syndication              | Data received through syndication.                     |
| 10 | transfer-learning        | Data generated through transfer learning.              |
| 11 | user-generated-content   | Data created by end users.                             |
| 12 | web-scraping-crawling    | Data collected by web scraping or crawling.            |



<a id="tab:modality-format-enum"></a>
Table 25: Type `ModalityFormat` (Enumerated)

| ID | Item                     | Description                           |
|---:|:-------------------------|:--------------------------------------|
|  1 | application/json         | JSON data format.                     |
|  2 | application/jsonld       | JSON-LD linked data format.           |
|  3 | application/msword       | Microsoft Word document format.       |
|  4 | application/vnd.ms-excel | Microsoft Excel spreadsheet format.   |
|  5 | application/zip          | ZIP archive format.                   |
|  6 | image/bmp                | BMP image format.                     |
|  7 | image/gif                | GIF image format.                     |
|  8 | image/jpeg               | JPEG image format.                    |
|  9 | image/png                | PNG image format.                     |
| 10 | image/x-png              | PNG image format (legacy media type). |
| 11 | other                    | A format not listed here.             |
| 12 | text/csv                 | CSV text format.                      |
| 13 | text/plain               | Plain text format.                    |


## 7.5 Use<a id='use'></a>

The `use` member describes the legal use and restrictions applicable to the dataset.


<a id="tab:use-record"></a>
Table 26: Type `Use` (Record)

| ID | Name                | Type             | \#    | Description                                                                               |
|---:|:--------------------|:-----------------|:------|:------------------------------------------------------------------------------------------|
|  1 | intended-purpose    | Purpose          | 1..\* | The purpose or purposes for which the dataset was created.                                |
|  2 | classification      | Classification   | 0..\* | Confidentiality classifications applicable to the dataset.                                |
|  3 | consents            | String           | 0..\* | Locations of consent documentation or agreements related to the data.                     |
|  4 | data-risk-reducing  | DataRiskReducing | 0..\* | Techniques used to reduce known data risk.                                                |
|  5 | processing-included | GeographicRegion | 0..\* | Geographical boundaries within which the data may be processed.                           |
|  6 | processing-excluded | GeographicRegion | 0..\* | Geographical boundaries within which the data may not be processed.                       |
|  7 | storage-allowed     | GeographicRegion | 0..\* | Geographical locations where the data may be stored.                                      |
|  8 | storage-forbidden   | GeographicRegion | 0..\* | Geographical locations where the data may not be stored.                                  |
|  9 | license             | String           | 0..\* | The terms under which the dataset can be used, including any restrictions or obligations. |
| 10 | copyright           | String           | 0..\* | Copyright information covering proprietary information in the dataset.                    |
| 11 | patent              | String           | 0..\* | Patent information covering proprietary information in the dataset.                       |
| 12 | trademark           | String           | 0..\* | Trademark information covering proprietary information in the dataset.                    |



<a id="tab:purpose-record"></a>
Table 27: Type `Purpose` (Record)

| ID | Name             | Type        | \#   | Description                                       |
|---:|:-----------------|:------------|:-----|:--------------------------------------------------|
|  1 | code             | PurposeCode | 1    | A short code identifying the intended purpose.    |
|  2 | long-description | String      | 1    | A detailed description of the intended purpose.   |
|  3 | system           | String      | 0..1 | The code system used to interpret the code value. |



<a id="tab:classification-record"></a>
Table 28: Type `Classification` (Record)

| ID | Name       | Type       | \#   | Description                                                                                   |
|---:|:-----------|:-----------|:-----|:----------------------------------------------------------------------------------------------|
|  1 | regulation | Regulation | 1    | The regulation or classification standard being evaluated.                                    |
|  2 | evaluated  | Boolean    | 1    | Whether the dataset has been evaluated against this classification (`true`) or not (`false`). |
|  3 | tool       | String     | 0..1 | The tool used to perform the evaluation.                                                      |



<a id="tab:regulation-record"></a>
Table 29: Type `Regulation` (Record)

| ID | Name             | Type                | \#   | Description                                                  |
|---:|:-----------------|:--------------------|:-----|:-------------------------------------------------------------|
|  1 | code             | ConfidentialityCode | 1    | A short code identifying the confidentiality classification. |
|  2 | system           | String              | 0..1 | The code system used to interpret the code value.            |
|  3 | long-description | String              | 0..1 | A detailed description of the regulation or classification.  |



<a id="tab:confidentiality-code-enum"></a>
Table 30: Type `ConfidentialityCode` (Enumerated)

| ID | Item  | Description                                       |
|---:|:------|:--------------------------------------------------|
|  1 | other | A confidentiality classification not listed here. |
|  2 | pci   | Payment Card Industry (PCI) data.                 |
|  3 | pfi   | Personal Financial Information (PFI).             |
|  4 | phi   | Protected Health Information (PHI).               |
|  5 | pi    | Personal Information (PI).                        |
|  6 | sci   | Sensitive Compartmented Information (SCI).        |
|  7 | spi   | Sensitive Personal Information (SPI).             |



<a id="tab:purpose-code-enum"></a>
Table 31: Type `PurposeCode` (Enumerated)

| ID | Item                      | Description                                           |
|---:|:--------------------------|:------------------------------------------------------|
|  1 | alignment                 | Dataset intended for model alignment tasks.           |
|  2 | evaluation                | Dataset intended for evaluation or benchmarking.      |
|  3 | other                     | A purpose not listed here.                            |
|  4 | pre-training              | Dataset intended for model pre-training.              |
|  5 | production                | Dataset intended for production use.                  |
|  6 | quality-assurance         | Dataset intended for quality assurance testing.       |
|  7 | research                  | Dataset intended for research use.                    |
|  8 | staging-testing           | Dataset intended for staging or testing environments. |
|  9 | synthetic-data-generation | Dataset intended for generating synthetic data.       |



<a id="tab:data-risk-reducing-record"></a>
Table 32: Type `DataRiskReducing` (Record)

| ID | Name          | Type           | \#    | Description                                                |
|---:|:--------------|:---------------|:------|:-----------------------------------------------------------|
|  1 | tool-used     | String         | 1     | The name of the tool used for data risk reduction.         |
|  2 | tool-category | Method         | 0..1  | The category of the tool used for data risk reduction.     |
|  3 | technology    | DataTechnology | 0..1  | The privacy-enhancing or data-reducing technology applied. |
|  4 | parameters    | Parameter      | 0..\* | The parameters passed to the tool.                         |
|  5 | results       | String         | 0..\* | The results of applying the tool.                          |



<a id="tab:parameter-record"></a>
Table 33: Type `Parameter` (Record)

| ID | Name  | Type   | \#   | Description          |
|---:|:------|:-------|:-----|:---------------------|
|  1 | name  | String | 1    | The parameter name.  |
|  2 | value | String | 0..1 | The parameter value. |



<a id="tab:data-technology-enum"></a>
Table 34: Type `DataTechnology` (Enumerated)

| ID | Item                           | Description                                                                                                                                                         |
|---:|:-------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | data-anonymization             | Transforms the dataset so that individuals cannot be identified, directly or indirectly, from the resulting records.                                                |
|  2 | data-encryption                | Encodes dataset content so that it is readable only by parties holding the decryption key; typically applied at rest or in transit.                                 |
|  3 | data-masking                   | Replaces sensitive field values with realistic but fictitious substitutes, preserving format and statistical properties without exposing the originals.             |
|  4 | data-minimization              | Reduces the dataset to only the fields and records necessary for the stated purpose, limiting exposure of personal or sensitive data.                               |
|  5 | data-redaction                 | Removes or obscures specific values or text spans identified as sensitive, such as names, identifiers, or health information.                                       |
|  6 | differential-privacy           | Adds calibrated statistical noise so that the presence or absence of any individual record cannot be reliably inferred from the released data.                      |
|  7 | federated-learning             | Produces model artefacts by training across distributed sources without centralising raw data, so the original dataset is never directly shared.                    |
|  8 | homomorphic-encryption         | Enables computation on ciphertext without decryption, so analytical results can be derived without exposing plaintext values.                                       |
|  9 | k-anonymity                    | Generalises quasi-identifying attributes so that each record is indistinguishable from at least k-1 other records in the dataset.                                   |
| 10 | l-diversity                    | Extends k-anonymity by requiring that each equivalence class contains at least l well-represented distinct sensitive attribute values.                              |
| 11 | other                          | A data risk reduction technology not covered by the defined values; use `tool-category` or `results` to describe the specific technique applied.                    |
| 12 | pseudonymization               | Replaces direct identifiers with artificial pseudonyms; re-identification remains possible through a separate, controlled mapping table.                            |
| 13 | secure-multi-party-computation | Allows multiple parties to jointly compute over their respective inputs without revealing those inputs to each other (SMC).                                         |
| 14 | t-closeness                    | Extends l-diversity by requiring that the distribution of sensitive values within each equivalence class closely matches their overall distribution in the dataset. |
| 15 | tokenization                   | Substitutes sensitive values with non-sensitive tokens; the originals are recoverable only through a separate, secured token vault.                                 |


## 7.6 Shared Types<a id='shared-types'></a>

The following types are used in more than one of the sections above.


<a id="tab:organization-record"></a>
Table 35: Type `Organization` (Record)

| ID | Name       | Type        | \#   | Description                             |
|---:|:-----------|:------------|:-----|:----------------------------------------|
|  1 | legal-name | String      | 1    | The legal name of the organization.     |
|  2 | address    | Address     | 0..1 | The postal address of the organization. |
|  3 | url        | String /uri | 0..1 | A URL for the organization.             |


The value of `url` SHOULD use the `https` scheme.


<a id="tab:address-array"></a>
Table 36: Type `Address` (ArrayOf(String))

| Type Name | Type Definition | Description                                       |
|:----------|:----------------|:--------------------------------------------------|
| Address   | ArrayOf(String) | Lines of a postal address. At least one required. |



<a id="tab:geographic-region-record"></a>
Table 37: Type `GeographicRegion` (Record)

| ID | Name    | Type   | \#   | Description                         |
|---:|:--------|:-------|:-----|:------------------------------------|
|  1 | country | String | 1    | The country name or code.           |
|  2 | state   | String | 0..1 | The state or province name or code. |



<a id="tab:method-record"></a>
Table 38: Type `Method` (Record)

| ID | Name             | Type   | \#   | Description                                                          |
|---:|:-----------------|:-------|:-----|:---------------------------------------------------------------------|
|  1 | code             | String | 1    | A short code identifying the method, regulation, or classification.  |
|  2 | system           | String | 0..1 | The code system used to interpret the code value.                    |
|  3 | long-description | String | 0..1 | A detailed description of the method, regulation, or classification. |


The `Acknowledgment` type describes a contributor. At least one of its fields MUST be present.


<a id="tab:acknowledgment-map"></a>
Table 39: Type `Acknowledgment` (Map)

| ID | Name         | Type        | \#    | Description                                             |
|---:|:-------------|:------------|:------|:--------------------------------------------------------|
|  1 | names        | String      | 0..\* | Names of individual contributors being acknowledged.    |
|  2 | organization | String      | 0..1  | Name of a contributing organization being acknowledged. |
|  3 | summary      | String      | 0..1  | Contextual details about the acknowledgment.            |
|  4 | urls         | String /uri | 0..\* | URLs of references being acknowledged.                  |



<a id="tab:version-string"></a>
Table 40: Type `Version` (String)

| Type Name | Type Definition | Description                                                                           |
|:----------|:----------------|:--------------------------------------------------------------------------------------|
| Version   | String          | An integer or semantic versioning string. Examples: `"1"`, `"2.0.0"`, `"1.0.0-beta"`. |



<a id="tab:language-string"></a>
Table 41: Type `Language` (String)

| Type Name | Type Definition | Description                                          |
|:----------|:----------------|:-----------------------------------------------------|
| Language  | String          | A language tag conforming to IETF BCP 47 / RFC 5646. |


# 8. Safety, Security, and Data Protection<a id='safety-security-and-data-protection'></a>

All safety, security, and data protection requirements relevant to the context in which Data Provenance Metadata documents are used MUST be translated into, and consistently enforced through, Data Provenance Metadata implementations and processes.

For Data Provenance Metadata documents based on JSON, the security considerations of \[[RFC8259](#RFC8259)\] apply and are repeated here as a service for the reader:

> Generally, there are security issues with scripting languages.  JSON is a subset of JavaScript but excludes assignment and invocation.
>
> Since JSON's syntax is borrowed from JavaScript, it is possible to use that language's `eval()` function to parse most JSON texts
> (but not all; certain characters such as `U+2028 LINE SEPARATOR` and `U+2029 PARAGRAPH SEPARATOR` are legal in JSON but not JavaScript).
> This generally constitutes an unacceptable security risk, since the text could contain executable code along with data declarations.
> The same consideration applies to the use of eval()-like functions in any other programming language in which JSON texts conform to
> that language's syntax.

Implementations SHOULD validate Data Provenance Metadata documents against the normative JSON Schema prior to processing.
Documents that do not validate MUST NOT be treated as authoritative provenance records.

## 8.1 Integrity and Authenticity of Provenance Claims<a id='integrity-and-authenticity'></a>

This specification defines the structure and vocabulary of provenance metadata but does not define mechanisms for verifying that the claims made within a record are accurate or have not been tampered with.
A Data Provenance Metadata document is only as trustworthy as the process and party that produced it.

Implementations that rely on provenance metadata for access control, compliance, or risk decisions SHOULD obtain records through channels that provide integrity guarantees, such as transport-layer security (TLS) when fetching from the URI identified in `source.location`, or cryptographic signatures applied to the document by the `set.publisher`.

The `set.tracking.id` and `source.id` fields provide identifiers for the record and the described dataset respectively, but do not themselves provide integrity protection.

## 8.2 URI Safety<a id='uri-safety'></a>

Several fields in this specification accept URI values, including `source.location`, `set.publisher.namespace`, `source.id.uris`, `set.acknowledgments[].urls`, and `set.references[].url`.
Implementations that automatically dereference these URIs MUST apply the same defences required for any externally supplied URL, including protection against server-side request forgery (SSRF) and open redirect attacks.
URIs MUST be validated as well-formed before dereferencing.
Implementations SHOULD restrict dereferenceable schemes to `https` and, where appropriate, `http`.

## 8.3 Sensitive Information in Provenance Records<a id='sensitive-information'></a>

Provenance records may incidentally contain information that publishers consider sensitive, including internal tool names in `use.data-risk-reducing`, personnel names in `set.acknowledgments`, internal geographic constraints in `use.processing-included` and related fields, and organizational contact details in `set.publisher.contact-details`.

Publishers MUST consider whether information included in a provenance record is appropriate for the audience that will consume it.
Provenance records intended for public distribution SHOULD be reviewed to ensure they do not expose internal operational details beyond what is required to describe the dataset's provenance.

## 8.4 Data Protection Compliance<a id='data-protection-compliance'></a>

The `use.classification` field records whether a dataset has been evaluated against confidentiality classifications such as PHI, PI, PCI, SCI, or SPI.
The presence of a classification entry, including the value of the `evaluated` field, does not itself constitute compliance with any applicable law or regulation.
Implementers that process datasets described by provenance records containing such classifications MUST apply the data handling controls required by the relevant regulations in the jurisdictions where the data is processed and stored.

The geographic restriction fields (`use.processing-included`, `use.processing-excluded`, `use.storage-allowed`, `use.storage-forbidden`) express the publisher's stated intent but are not self-enforcing.
Implementers are responsible for establishing technical and organizational controls that honour these restrictions.

---

# 9. Conformance<a id='conformance'></a>

This document defines requirements for the data-provenance in the JSON file format and for certain software components that interact with it. 

<!--
The editors guided by the TC shall add conformance targets in this section.
The above (non-commented) statement is a first attempt to start the process.
Existing OASIS specifications like CSAF, MQTT-SN, OpenEoX-Core, and SARIF use roles to anchor such conformance targets.
We may want to add a blanket statement that allows file formats in the wild to be valid as long as the information model matches the specification.
-->

---

# Annex A. License, Document Status and Notices<a id='annex-a'></a>

(This annex forms an integral part of this Specification.)

## A.1 Document Status<a id='document-status'></a>

This document was last revised or approved by the OASIS DPS TC on the above date. The level of approval is also listed above. Check the "Latest version" location noted above for possible later revisions of this document. Any other numbered Versions and other technical work produced by the Technical Committee (TC) are listed at <https://groups.oasis-open.org/communities/tc-community-home2?CommunityKey=2c60b2cf-45d3-48cd-8594-0194f182b33d>.

TC members should send comments on this document to the TC's email list. Others should send comments to the TC's public comment list, after subscribing to it by following the instructions at the "Send A Comment" button on the TC's web page at <https://www.oasis-open.org/committees/dps/>.

NOTE: any machine-readable content (Computer Language Definitions) declared Normative for this Work Product is provided in separate plain text files. In the event of a discrepancy between any such plain text file and display content in the Work Product's prose narrative document(s), the content in the separate plain text file prevails.

## A.2 License and Notices<a id='license-and-notices'></a>

<!-- Required section. Do not modify. -->

Copyright &copy; OASIS Open 2026. All Rights Reserved.

All capitalized terms in the following text have the meanings assigned to them in the OASIS Intellectual Property Rights Policy (the "OASIS IPR Policy"). The full Policy, which governs the licensure of this document, may be found at the OASIS website: [[https://www.oasis-open.org/policies-guidelines/ipr/](https://www.oasis-open.org/policies-guidelines/ipr/)]

This document and translations of it may be copied and furnished to others, and derivative works that comment on or otherwise explain it or assist in its implementation may be prepared, copied, published, and distributed, in whole or in part, without restriction of any kind, provided that the above copyright notice and this section are included on all such copies and derivative works. However, this document itself may not be modified in any way, including by removing the copyright notice or references to OASIS, except as needed for the purpose of developing any document or deliverable produced by an OASIS Technical Committee (in which case the rules applicable to copyrights, as set forth in the OASIS IPR Policy, must be followed) or as required to translate it into languages other than English.

The limited permissions granted above are perpetual and will not be revoked by OASIS or its successors or assigns, as provided in the OASIS IPR Policy.

This document is provided under the “Non-Assertion” IPR mode that was chosen when the project was established, as defined in the IPR Policy. For information on whether any patents have been disclosed that may be essential to implementing this document, and any offers of patent licensing terms, please refer to the Intellectual Property Rights section of the project’s web page ([https://www.oasis-open.org/committees/dps/ipr.php](https://www.oasis-open.org/committees/dps/ipr.php)).

This document and the information contained herein is provided on an "AS IS" basis and OASIS DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE INFORMATION HEREIN WILL NOT INFRINGE ANY OWNERSHIP RIGHTS OR ANY IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. OASIS AND ITS MEMBERS WILL NOT BE LIABLE FOR ANY DIRECT, INDIRECT, SPECIAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF ANY USE OF THIS DOCUMENT OR ANY PART THEREOF.

As stated in the OASIS IPR Policy, the following three paragraphs in brackets apply to OASIS Standards Final Deliverable documents (Committee Specifications, OASIS Standards, or Approved Errata).

OASIS requests that any OASIS Party or any other party that believes it has patent claims that would necessarily be infringed by implementations of this OASIS Standards Final Deliverable, to notify OASIS TC Administrator and provide an indication of its willingness to grant patent licenses to such patent claims in a manner consistent with the IPR Mode of the OASIS Technical Committee that produced this deliverable.

OASIS invites any party to contact the OASIS TC Administrator if it is aware of a claim of ownership of any patent claims that would necessarily be infringed by implementations of this OASIS Standards Final Deliverable by a patent holder that is not willing to provide a license to such patent claims in a manner consistent with the IPR Mode of the OASIS Technical Committee that produced this OASIS Standards Final Deliverable. OASIS may include such claims on its website, but disclaims any obligation to do so.

OASIS takes no position regarding the validity or scope of any intellectual property or other rights that might be claimed to pertain to the implementation or use of the technology described in this OASIS Standards Final Deliverable or the extent to which any license under such rights might or might not be available; neither does it represent that it has made any effort to identify any such rights. Information on OASIS' procedures with respect to rights in any document or deliverable produced by an OASIS Technical Committee can be found on the OASIS website. Copies of claims of rights made available for publication and any assurances of licenses to be made available, or the result of an attempt made to obtain a general license or permission for the use of such proprietary rights by implementers or users of this OASIS Standards Final Deliverable, can be obtained from the OASIS TC Administrator. OASIS makes no representation that any information or list of intellectual property rights will at any time be complete, or that any claims in such list are, in fact, Essential Claims.

The name "OASIS" is a trademark of OASIS, the owner and developer of this document, and should be used only to refer to the organization and its official outputs. OASIS welcomes reference to, and implementation and use of, its documents, while reserving the right to enforce its marks against misleading uses. Please see [https://www.oasis-open.org/policies-guidelines/trademark/](https://www.oasis-open.org/policies-guidelines/trademark/) for guidance.

---

# Annex B. References<a id='annex-b'></a>

(This annex forms an integral part of this Specification.)

This section contains the normative and informative references that are used in this document.

Normative references are specific (identified by date of publication and/or edition number or version number) and Informative references are either specific or non-specific. For specific references, only the cited version applies. For non-specific references, the latest version of the reference document (including any amendments) applies. While any hyperlinks included in this section were valid at the time of publication, OASIS cannot guarantee their long term validity.

## B.1 Normative References<a id='normative-references'></a>

The following documents are referenced in such a way that some or all of their content constitutes requirements of this document.

**\[**<span id="RFC2119" class="anchor"></span>**RFC2119\]** _Key Words for Use in RFCs to Indicate Requirement Levels_, BCP 14, RFC 2119, March 1997\. \[Online\]. Available: https://www.rfc-editor.org/info/rfc2119

**\[**<span id="RFC8174" class="anchor"></span>**RFC8174\]** _Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words_, BCP 14, RFC 8174, May 2017\. \[Online\]. Available: https://www.rfc-editor.org/info/rfc8174

**\[**<span id="RFC8259" class="anchor"></span>**RFC8259\]** Bray, T., "The JavaScript Object Notation (JSON) Data Interchange Format", RFC 8259, DOI 10.17487/RFC8259, December 2017, <http://www.rfc-editor.org/info/rfc8259>.

## B.2 Informative References<a id='informative-references'></a>

The following referenced documents are not required for the application of this document but may assist the reader with regard to a particular subject area.


**\[**<span id="CNSSI-4009" class="anchor"></span>**CNSSI-4009\]** _Committee on National Security Systems (CNSS) Glossary_, Committee on National Security Systems, CNSSI No. 4009, April 6, 2015, Available: https://nsarchive.gwu.edu/document/22385-document-08-committee-national-security

# Annex C. Example Instances<a id='annex-c'></a>

(This annex forms an integral part of this Specification.)

This annex provides four example instances of the Data Provenance Metadata schema,
each serving a distinct purpose in learning and applying the standard.

The **minimal example** ([C.1 "Minimal Example"](#minimal-example)) contains only the fields that are required by the schema,
populated with the smallest valid values.
It is intended as a starting point for new implementers and as a quick reference for
the mandatory structure of a DP-Core set.

The **moderate example** ([C.2 "Moderate Example"](#moderate-example)) extends the minimal case by adding a representative selection
of optional fields at each level.
It is intended to illustrate common real-world usage — a dataset with multiple geographies,
a revision history, licensing information, and a confidentiality classification — without
attempting to cover every possible field.

The **complete example** ([C.3 "Complete Example"](#complete-example)) is a comprehensive instance that exercises every field
defined in the schema at least once.
It is not intended to represent a typical implementation; its purpose is to serve as a
normative reference for tool developers verifying parser completeness and for authors
checking field semantics under realistic conditions.

The **lineage example** ([C.4 "Lineage Example"](#lineage-example)) is a real record exported from a live implementation.
It shows how one record evolves over several revisions, and why the version of the metadata set
and the version of the dataset it describes are independent counters.

All four instances are available as JSON files in the `examples/` directory of the
specification distribution.

## C.1 Minimal Example<a id='minimal-example'></a>

The following instance contains only the fields required by the schema.
The scenario is a single-issuer survey dataset with one generation method and one intended purpose.

```json
{
  "$schema": "https://docs.oasis-open.org/dps/prov-meta/v1.0/schema/data-provenance.json",
  "set": {
    "category": "training-data",
    "schema-version": "1.0",
    "publisher": {
      "name": "Example Organization",
      "namespace": "https://example.org/"
    },
    "label": "Example Dataset Provenance",
    "tracking": {
      "current-release-date": "2026-06-30T00:00:00Z",
      "id": "example-dataset-prov-001",
      "initial-release-date": "2026-06-30T00:00:00Z",
      "revision-history": [
        {
          "date": "2026-06-30T00:00:00Z",
          "number": "1",
          "summary": "Initial release."
        }
      ],
      "status": "final",
      "version": "1"
    }
  },
  "source": {
    "about": {
      "content": "A dataset of anonymized customer survey responses collected in 2025.",
      "purpose": "Intended for training binary sentiment analysis models."
    },
    "id": {
      "uuids": ["f47ac10b-58cc-4372-a567-0e02b2c3d479"]
    },
    "issuer": [
      {
        "legal-name": "Example Organization"
      }
    ],
    "location": "https://example.org/datasets/survey-2025/provenance.json",
    "name": "Customer Survey Dataset 2025",
    "data-version": "1"
  },
  "provenance": {
    "origin-geography": [
      {
        "country": "United States"
      }
    ],
    "date": "2026-06-01",
    "generation-method": [
      {
        "code": "primary-user-source"
      }
    ]
  },
  "use": {
    "intended-purpose": [
      {
        "code": "pre-training",
        "long-description": "To be used for pre-training binary sentiment classification models."
      }
    ]
  }
}
```

The file `examples/dp-core-minimal.json` contains this instance.

## C.2 Moderate Example<a id='moderate-example'></a>

The moderate example extends the minimal case with a representative but non-exhaustive
selection of optional fields.
The scenario is a multilingual news corpus assembled from syndicated feeds and published
by a single commercial data provider.

Key features illustrated by this instance:

- **Set level**: `language`, `acknowledgments`, and publisher `contact-details` are present.
  The tracking block includes two revision entries, reflecting a real update cycle.
- **Source level**: `scope` is populated in `about`, limiting the stated purpose of the dataset.
  Two identification methods are used (`uuids` and `uris`). The issuer entry includes a
  postal `address` and a `url`.
- **Provenance level**: Three `origin-geography` entries span multiple countries.
  `generation-method` carries a `long-description` explaining the feed mechanism.
  `format`, `generation-period`, and a lineage `source` URI are all present.
- **Use level**: Two `intended-purpose` entries distinguish pre-training from academic research use.
  A single `classification` entry records evaluation against the Personal Information (PI) regulation.
  `consents` and `license` are populated.

The file `examples/dp-core-moderate.json` contains this instance.

## C.3 Complete Example<a id='complete-example'></a>

The complete example is a comprehensive instance designed to exercise every field in the schema.
The scenario is a large merged biomedical text corpus assembled by a research consortium from
three distinct sub-sources: PubMed abstracts, ClinicalTrials.gov result summaries, and
de-identified hospital discharge summaries.

Key features illustrated by this instance that are not present in the moderate example:

- **Set level**: All optional tracking fields are used, including `aliases` and `generator`
  (with engine name, version, and generation date). `source-language`, `notes`, and `references`
  are present. The `notes` array contains two entries — a `legal_disclaimer` for the clinical
  content and a `summary` note describing what changed in version 3. The `references` array
  demonstrates both `external` and `self` category values.
- **Source level**: All four `identity` methods are used: `uuids`, `uris`, `hashes` (with a
  SHA-256 tree hash), and `custom-ids` (a DataCite DOI with tool parameters). Two `issuer`
  entries reflect the dual institutional origin. `scope` in `about` explicitly excludes
  document types not covered.
- **Provenance level**: Three `generation-method` entries with different codes cover the full
  collection pipeline. `format` lists three media types. `origin` names the upstream data
  providers. `previous-date` establishes continuity with the prior version. `sub-provenance`
  records the provenance of the initial PubMed-only sub-corpus from the v1 release.
- **Use level**: Three `intended-purpose` entries (`pre-training`, `alignment`, `evaluation`).
  Three `classification` entries cover PHI, PI, and a free-text GDPR Article 9 entry using
  `code: other` with a `long-description`. Two `data-risk-reducing` entries document the NER-based
  redaction tool and the k-anonymity pipeline, each with `technology`, `parameters`, and `results`.
  All four geography restriction fields are populated (`processing-included`, `processing-excluded`,
  `storage-allowed`, `storage-forbidden`). `copyright`, `patent`, and `trademark` are present.

The file `examples/dp-core-complete.json` contains this instance.

## C.4 Lineage Example<a id='lineage-example'></a>

The lineage example is a real record exported from a live implementation (mnēSara);
two internal identifiers in `source.about.content` are redacted, nothing else is changed.
It describes one document, a compliance report, across three revisions of the record:

1. **Initial upload**: the record is created.
   `set.tracking.version` is `1`, and `source.data-version` is `1`.
2. **Metadata enrichment**: the issuer is populated automatically from entities extracted from the document;
   the document itself is unchanged.
   `set.tracking.version` advances to `2`, and `source.data-version` stays `1`.
3. **Document replacement**: the document itself is replaced by a new file.
   `set.tracking.version` advances to `3`, and `source.data-version` advances to `2`.

The two counters version different things: `set.tracking.version` versions the metadata set,
`source.data-version` versions the dataset the metadata set describes.
They move together only when a revision changes the dataset;
a revision that changes only the metadata advances `set.tracking.version` alone, as revision 2 does.
Their values differing, as in this record (`3` and `2`), is the normal case, not an error.

Key features illustrated by this instance:

- **Set level**: three `revision-history` entries, the latest of which carries the `number` that
  `set.tracking.version` repeats, and a publisher `namespace` under the implementer's own domain.
- **Source level**: the document is identified both by a `uuids` entry and by a SHA-256 tree hash in `hashes`,
  and `location` uses the implementation's own URI scheme.
- **Provenance level**: the lineage to the previous record is expressed by `source`, the URI of that record,
  `source-digest`, the digest of that record computed at issuance, and `previous-date`.
  `generation-method` and `intended-purpose` use `code` together with an implementation-specific `system`.

```json
{
  "set": {
    "label": "Project Document: kestrel-northfield-q3-2026-compliance.pdf",
    "category": "general",
    "tracking": {
      "id": "399d80b1-df78-41d9-a7e3-bf303f5be0cf",
      "status": "final",
      "version": "3",
      "revision-history": [
        {
          "date": "2026-10-16T15:12:50.009Z",
          "number": "1",
          "summary": "Initial version."
        },
        {
          "date": "2026-10-16T15:13:10.568Z",
          "number": "2",
          "summary": "Issuer and origin populated from extracted document entities."
        },
        {
          "date": "2026-10-16T15:16:57.452Z",
          "number": "3",
          "summary": "updated compliance report"
        }
      ],
      "current-release-date": "2026-10-16T15:16:57.452Z",
      "initial-release-date": "2026-10-16T15:12:50.009Z"
    },
    "publisher": {
      "name": "mnēSara",
      "namespace": "https://mnesara.com"
    },
    "schema-version": "1.0"
  },
  "use": {
    "intended-purpose": [
      {
        "code": "production",
        "system": "https://mnesara.com/dps/vocab/purpose",
        "long-description": "operational-context"
      }
    ]
  },
  "source": {
    "id": {
      "uuids": [
        "33b4b06b-62bc-4ab3-ae4f-f0a3ce690f15"
      ],
      "hashes": [
        {
          "path": "kestrel-northfield-q3-2026-compliance.pdf",
          "tree-hashes": [
            {
              "value": "e1e59d27889c2058f98c79f76000c3b531741731cd9889f7df819dc8e71e68c4",
              "algorithm": "sha256"
            }
          ]
        }
      ]
    },
    "name": "kestrel-northfield-q3-2026-compliance.pdf",
    "about": {
      "content": "Document \"kestrel-northfield-q3-2026-compliance.pdf\" (application/pdf) ingested via project wizard into project <redacted> / matter <redacted>",
      "purpose": "Matter evidence for AI analysis and knowledge graph construction."
    },
    "issuer": [
      {
        "legal-name": "Kestrel Basin Water Authority"
      }
    ],
    "location": "mnesara://project-sources/33b4b06b-62bc-4ab3-ae4f-f0a3ce690f15",
    "data-version": "2"
  },
  "$schema": "https://docs.oasis-open.org/dps/prov-meta/v1.0/schema/data-provenance.json",
  "provenance": {
    "date": "2026-10-16",
    "source": "https://mnesara.com/dps/records/37268278-bb5f-4791-919d-e1f12ba11d33",
    "previous-date": "2026-10-16",
    "source-digest": {
      "value": "bb121f5f3ae0ee44d8e21d50b92ed8bcdd1f3a20887615b2f81083a6edf190e5",
      "algorithm": "sha256"
    },
    "origin-geography": [
      {
        "country": "Kestrel Basin Territory (ZZ)"
      }
    ],
    "generation-method": [
      {
        "code": "other",
        "system": "https://mnesara.com/dps/vocab/generation-method",
        "long-description": "project-document-ingestion"
      }
    ]
  }
}
```

The file `examples/dp-core-lineage.json` contains this instance.

---

# Appendix A. Acknowledgments<a id='appendix-acknowledgments'></a>

(This appendix does not form an integral part of this Specification and is informational.)

The following individuals were members of the OASIS DPS Technical Committee during the creation of this specification and their contributions are gratefully acknowledged:

## Leadership<a id='leadership'></a>

The following individuals have had significant leadership positions during the development of this document, not just this version of the document, and they are gratefully acknowledged:

- Chairs
  - Lisa Bobbitt, Cisco, lbobbitt@cisco.com
  - Bryan Bortnick, IBM, bortnick@us.ibm.com
  - Fotis Psallidas, Microsoft, Fotis.Psallidas@microsoft.com

- Secretaries
  - Jamie Yu, Cisco, jamyu2@cisco.com

- Editors
  - David Kemp, NSA, d.kemp@cyber.nsa.gov
  - Stefan Hagen, Individual, stefan@hagen.link

## Special Thanks<a id='special-thanks'></a>

The following individuals have made substantial contributions to this document, not just this version of the document, and their contributions are gratefully acknowledged:

The DPS TC thanks the following individuals for their assistance in the development of this document:
Kristina Podnar and the Data &amp; Trust Alliance for their contributions of the initial schema and example applications.
Duncan Sparrell for supporting the TC from the charter definition to the initial structuring of this document.

## Participants<a id='participants'></a>

The following individuals have participated in the creation of this document and are gratefully acknowledged (given family, affiliation):

- Charles Assaf, Individual
- David Kemp, NSA
- Duncan Sparrell, sFractal Consulting LLC
- Kristina Podnar, Data &amp; Trust Alliance
- Lisa Bobbitt, Cisco
- Stefan Hagen, Individual

---

# Appendix B. Changes From Previous Version<a id='appendix-changes-from-previous-version'></a>

(This appendix does not form an integral part of this Specification and is informational.)

This is the initial draft Committee Specification.

## Revision History<a id='revision-history'></a>

Revision tracking is publicly available in the version control system at
<https://github.com/oasis-tcs/dps/commits/main>.

---
