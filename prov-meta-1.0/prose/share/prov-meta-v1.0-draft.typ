
// Passthrough conf: this template owns all layout; pandoc keyword args are accepted
// but ignored — the positional arg (doc body) is what we use.
#let conf(..args) = args.pos().first()


// ── Shared OASIS brand (typography, code, headings, tables, …) ────────────────

#import "../etc/oasis.typ": oasis-setup

// ── Page layout (per-spec) ────────────────────────────────────────────────────

#set page(
  paper: "a4",
  margin: (top: 2cm, bottom: 2cm, left: 1cm, right: 1cm),
  header: align(center, text(size: 10pt)[Standards Track Work Product]),
  footer: context grid(
    inset: (top: 0.4em),
    stroke: (top: 0.5pt),
    columns: (1fr, 2fr, 1fr),
    align: (left + horizon, center + horizon, right + horizon),
    text(size: 8pt)[prov-meta-v1.0-csd02],
    text(size: 8pt)[Copyright © OASIS Open 2026. All Rights Reserved.],
    text(size: 8pt)[30 June 2026 — Page #counter(page).display()
      of #counter(page).final().first()],
  ),
)

// Language (font and base size come from oasis-setup)
#set text(lang: "en")

// ── Apply OASIS brand + pandoc passthrough ────────────────────────────────────

#show: oasis-setup
#show: doc => conf(
  sectionnumbering: none,
  pagenumbering: none,
  cols: 1,
  doc,
)

#set heading(numbering: (..nums) => {
  let n = nums.pos()
  let base = numbering("1.1", ..n)
  if n.len() == 1 { base + "." } else { base }
})
#show raw: set text(size: 0.85em)
#box(image("images/OASISLogo-v3.0.png"))

#heading(level: 1, outlined: false, numbering: none)[Data Provenance
Metadata Version 1.0]
<data-provenance-metadata-version-1-0>
#heading(level: 2, outlined: false, numbering: none)[Committee
Specification Draft 02]
<committee-specification-draft-02>
#heading(level: 2, outlined: false, numbering: none)[19 July 2026]
<19-july-2026>
#heading(level: 3, outlined: false, numbering: none)[This version]
<this-version>
- #link("https://docs.oasis-open.org/dps/prov-meta/v1.0/csd01/prov-meta-v1.0-csd02.md")[https:/\/docs.oasis-open.org/dps/prov-meta/v1.0/csd02/prov-meta-v1.0-csd02.md]
  (Authoritative)
- #link("https://docs.oasis-open.org/dps/prov-meta/v1.0/csd01/prov-meta-v1.0-csd02.html")[https:/\/docs.oasis-open.org/dps/prov-meta/v1.0/csd02/prov-meta-v1.0-csd02.html]
- #link("https://docs.oasis-open.org/dps/prov-meta/v1.0/csd01/prov-meta-v1.0-csd02.pdf")[https:/\/docs.oasis-open.org/dps/prov-meta/v1.0/csd02/prov-meta-v1.0-csd02.pdf]

#heading(level: 3, outlined: false, numbering: none)[Latest version]
<latest-version>
- #link("https://docs.oasis-open.org/dps/prov-meta/v1.0/prov-meta-v1.0.md")
  (Authoritative)
- #link("https://docs.oasis-open.org/dps/prov-meta/v1.0/prov-meta-v1.0.html")
- #link("https://docs.oasis-open.org/dps/prov-meta/v1.0/prov-meta-v1.0.pdf")

#heading(level: 3, outlined: false, numbering: none)[Previous version]
<previous-version>
- #link("https://docs.oasis-open.org/dps/prov-meta/v1.0/csd01/prov-meta-v1.0-csd01.md")
  (Authoritative)
- #link("https://docs.oasis-open.org/dps/prov-meta/v1.0/csd01/prov-meta-v1.0-csd01.html")
- #link("https://docs.oasis-open.org/dps/prov-meta/v1.0/csd01/prov-meta-v1.0-csd01.pdf")

#heading(level: 3, outlined: false, numbering: none)[Technical
Committee]
<technical-committee>
#link("https://groups.oasis-open.org/communities/tc-community-home2?CommunityKey=2c60b2cf-45d3-48cd-8594-0194f182b33d")[Data Provenance Standard Technical Committee]

#heading(level: 3, outlined: false, numbering: none)[Chairs]
<chairs>
- Lisa Bobbitt, Cisco, lbobbitt\@cisco.com
- Bryan Bortnick, IBM, bortnick\@us.ibm.com
- Fotis Psallidas, Microsoft, Fotis.Psallidas\@microsoft.com

#heading(level: 3, outlined: false, numbering: none)[Secretaries]
<secretaries>
- Jamie Yu, Cisco, jamyu2\@cisco.com

#heading(level: 3, outlined: false, numbering: none)[Editors]
<editors>
- David Kemp, NSA, d.kemp\@cyber.nsa.gov
- Stefan Hagen, individual, stefan\@hagen.link

#heading(level: 3, outlined: false, numbering: none)[Additional
Artifacts]
<additional-artifacts>
This prose specification is one component of a Work Product that also
includes:

- Data Provenance Metadata JSON schema:
  https:/\/docs.oasis-open.org/dps/prov-meta/v1.0/csd02/schema/data-provenance.json.
  \ Latest stage:
  https:/\/docs.oasis-open.org/dps/prov-meta/v1.0/schema/data-provenance.json.
- Data Provenance Metadata Configuration JSON schema:
  https:/\/docs.oasis-open.org/dps/prov-meta/v1.0/csd02/schema/data-provenance-configuration.json.
  \ Latest stage:
  https:/\/docs.oasis-open.org/dps/prov-meta/v1.0/schema/data-provenance-configuration.json.

#heading(level: 3, outlined: false, numbering: none)[Declared JSON
namespaces]
<declared-json-namespaces>
- #link("https://docs.oasis-open.org/dps/prov-meta/v1.0/schema/data-provenance.json")
- #link("https://docs.oasis-open.org/dps/prov-meta/v1.0/schema/data-provenance-configuration.json")

#heading(level: 3, outlined: false, numbering: none)[Abstract]
<abstract>
This OASIS Data Provenance Metadata specification provides an
information model and several specialized data schemata for describing
and managing data provenance and data lineage. The resulting common
language provides transparency for data provenance and enables assessing
where data comes from, how it has been created, and in what scenarios it
can be used, legally.

#heading(level: 3, outlined: false, numbering: none)[Citation Format]
<citation-format>
When referencing this document, the following citation format should be
used:

#strong[\[prov-meta-v1.0\]]

#emph[Data Provenance Metadata Version 1.0]. Edited by David Kemp and
Stefan Hagen. 19 July 2026. OASIS Committee Specification Draft 02. \
https:/\/docs.oasis-open.org/dps/prov-meta/v1.0/csd02/prov-meta-v1.0-csd02.html.
\ Latest stage:
https:/\/docs.oasis-open.org/dps/prov-meta/v1.0/prov-meta-v1.0.html.

#heading(level: 3, outlined: false, numbering: none)[Related Work]
<related-work>
This document replaces or supersedes:

N/A

This document is related to:

N/A

#heading(level: 2, outlined: false, numbering: none)[License, Document
Status, and Notices]
<license-document-status-and-notices>
Copyright © OASIS Open 2026. All Rights Reserved. \ For license and
copyright information, and complete status, please see
#link(<annex-a>)[Annex A] which contains the License, Document Status
and Notices.

#pagebreak(weak: true)
// set channels.typst.toc-dots: true in nide.yaml to add dot leaders
#show outline.entry: set outline.entry(fill: none)
#outline(title: "Table of Contents", depth: 2)
#pagebreak(weak: true)
= Scope
<scope>
Data is a core enterprise asset that underpins strategic
decision-making, drives operational priorities, and supports risk
governance. Dependence on data creates a need for validation by
understanding data's origin, quality, and intended use. Understanding
data is a requirement for organizations operating at scale. The OASIS
Data Provenance Standards (DPS) are created to solve for this need.
Developed through cross-industry collaboration, the DPS provide a
consistent framework to track the origin, movement, integrity, and
quality of data. The DPS address the growing demand for transparency in
artificial intelligence (AI), cybersecurity, supply chains, and areas
where data quality and accountability are foundational to performance
and compliance - especially in regulated and high-risk environments.

#pagebreak(weak: true)
= Definitions and Acronyms
<definitions-and-acronyms>
== Definitions
<definitions>
=== Terms Defined Elsewhere
<terms-defined-elsewhere>
This document uses the following terms defined elsewhere:

/ ​Data Provenance<def:data-provenance>: #block[
In the context of computers and law enforcement use, it is synonymous to
chain of custody. It involves the method of generation, transmission and
storage of information that may be used to trace the origin of a piece
of information processed by community resources. Cf.
\[#link(<CNSSI-4009>)[CNSSI-4009]\] for more details.
]

/ ​Data Lineage<def:data-lineage>: #block[
Data lineage is the process of tracking the (use and) flow of data over
time, providing a clear understanding of where the data originated, how
it has changed, and its ultimate destination within the data pipeline.
Cf. "Data Lineage at IBM" https:/\/www.ibm.com/think/topics/data-lineage
for more details.
]

/ ​Data Transparency<def:data-transparency>: #block[
Data transparency refers to the clear, open, and honest handling of data
within an organization. It means that businesses, governments, and
institutions disclose how they collect, store, use, and share data,
ensuring users, customers, and stakeholders understand their practices.
Cf. "What is data transparency at BigID"
https:/\/bigid.com/blog/what-is-data-transparency for more details.
]

=== Terms Defined in this Document
<terms-defined-in-this-document>
None

== Abbreviations and Acronyms
<abbreviations-and-acronyms>
/ AI: #block[
Artificial Intelligence
]

/ DET: #block[
Data Enhancing Technologies
]

/ DPS: #block[
Data Provenance Standard
]

/ PET: #block[
Privacy Enhancing Technologies
]

#pagebreak(weak: true)
= Document Conventions
<document-conventions>
== Key Words
<key-words>
The key words "#strong[MUST]", "#strong[MUST NOT]", "#strong[REQUIRED]",
"#strong[SHALL]", "#strong[SHALL NOT]", "#strong[SHOULD]",
"#strong[SHOULD NOT]", "#strong[RECOMMENDED]", "#strong[NOT
RECOMMENDED]", "#strong[MAY]", and "#strong[OPTIONAL]" in this document
are to be interpreted as described in BCP 14
\[#link(<RFC2119>)[RFC2119]\] and \[#link(<RFC8174>)[RFC8174]\] when,
and only when, they appear in all capitals, as shown here.

== Typographical Conventions
<typographical-conventions>
Keywords defined by this specification use this `monospaced` font.

```
    Normative source code uses this paragraph style.
```

Some sections of this specification are illustrated with non-normative
examples introduced with "Example" or "Examples" like so:

#emph[Example 1:]#box()<typographical-conventions-eg-1>

```
    Informative examples also use this paragraph style but preceded by the text "Example(s)".
```

All examples in this document are informative only.

All other text is normative unless otherwise labeled e.g.~like the
following informative comment:

#quote(block: true)[
This is a pure informative comment that may be present, because the
information conveyed is deemed useful advice or common pitfalls learned
from implementer or operator experience and often given including the
rationale.
]

This document adheres to the Modern Language Association (MLA) style
guidelines for formatting titles and terms.

#pagebreak(weak: true)
= Introduction
<introduction>
Data is a core enterprise asset. It underpins strategic decision-making,
drives operational priorities, and supports risk governance. Dependence
on data creates a need for validation and an understanding of the data's
origin, quality, and intended use. Understanding data is a requirement
for organizations operating at scale. The OASIS Data Provenance
Standards (DPS) are created to solve for this need.

== Any Additional Introduction Subsections That are Needed
<any-additional-introduction-subsections-that-are-needed>
None

== Changes From the Previous Version
<changes-from-the-previous-version>
N/A

#pagebreak(weak: true)
= Provenance Schema
<provenance-schema>
The schema of the provenance metadata is described in human-readable
property tables. The technical encoding may be found in section
#link(<provenance-information-model-encoding>)[6 "Provenance Information Model Encoding"].

The Data Provenance Standards record metadata elements in three
segmented categories: Source, Provenance, and Use.

#figure(image("images/metadata.svg", alt: "Metadata"),
  caption: [
    Metadata
  ]
)

The property tables first define metadata about the specification
itself, then describe how a record is made of the 3 primary metadata
elements. The three segmented categories (Source, Provenance, and Use)
are comprised of various metadata element input fields. Each field is
described in more detail below.

== Primary Metadata Elements
<primary-metadata-elements>
The root object of a Data Provenance Metadata record contains five
required members.

#figure(
  align(center)[#table(
    columns: (6%, 15%, 15%, 6%, 58%),
    align: (right,left,left,left,left,),
    table.header([ID], [Name], [Type], [\#], [Description],),
    table.hline(),
    [1], [\$schema], [String /uri], [1], [The URI identifying the schema
    this JSON object must be valid against. For this version the value
    is always the URI of the data-provenance JSON schema.],
    [2], [set], [Set], [1], [Set-level metadata about this provenance
    metadata record.],
    [3], [source], [Source], [1], [Characterizes the content and source
    of the dataset.],
    [4], [provenance], [Provenance], [1], [Describes the provenance of
    the dataset.],
    [5], [use], [Use], [1], [Describes legal use and restrictions that
    apply to the dataset.],
  )]
  , caption: [Type `DataProvenance` (Record)]
  , kind: table
  )
<tab:data-provenance-record>

== Set
<set>
The `set` member captures metadata about the provenance metadata record
itself.

#figure(
  align(center)[#table(
    columns: (6%, 15%, 15%, 6%, 58%),
    align: (right,left,left,left,left,),
    table.header([ID], [Name], [Type], [\#], [Description],),
    table.hline(),
    [1], [category], [String], [1], [A short canonical name, chosen by
    the set producer, informing the end user of the category of the
    metadata set.],
    [2], [schema-version], [String], [1], [The version of the Data
    Provenance Core specification this record was generated for. The
    value for this version is always `"1.0"`.],
    [3], [publisher], [Publisher], [1], [Information about the publisher
    of the metadata set.],
    [4], [label], [String], [1], [The per-publisher unique title of this
    metadata set.],
    [5], [tracking], [Tracking], [1], [Management attributes used to
    track this metadata set as a whole.],
    [6], [language], [Language], [0..1], [The language used in this
    document, corresponding to IETF BCP 47.],
    [7], [source-language], [Language], [0..1], [If this is a
    translation, the language this document was translated from.],
    [8], [acknowledgments], [Acknowledgment], [0..\*], [Acknowledgment
    elements associated with the whole set.],
    [9], [notes], [Note], [0..\*], [Notes associated with this metadata
    set.],
    [10], [references], [Reference], [0..\*], [References associated
    with this metadata set.],
  )]
  , caption: [Type `Set` (Record)]
  , kind: table
  )
<tab:set-record>

#figure(
  align(center)[#table(
    columns: (6%, 15%, 15%, 6%, 58%),
    align: (right,left,left,left,left,),
    table.header([ID], [Name], [Type], [\#], [Description],),
    table.hline(),
    [1], [name], [String], [1], [The name of the issuing party.],
    [2], [namespace], [String /uri], [1], [A URI under the control of
    the issuing party, used as a globally unique identifier for that
    party.],
    [3], [contact-details], [String], [0..1], [Information on how to
    contact the publisher.],
  )]
  , caption: [Type `Publisher` (Record)]
  , kind: table
  )
<tab:publisher-record>

#figure(
  align(center)[#table(
    columns: (6%, 15%, 15%, 6%, 58%),
    align: (right,left,left,left,left,),
    table.header([ID], [Name], [Type], [\#], [Description],),
    table.hline(),
    [1], [current-release-date], [String /date-time], [1], [The date
    when the current revision of this document was released.],
    [2], [id], [String], [1], [A unique identifier for this metadata
    set, assigned and maintained by the original issuing authority. MUST
    NOT start or end with whitespace.],
    [3], [initial-release-date], [String /date-time], [1], [The date
    when this metadata set was first published.],
    [4], [revision-history], [Revision], [1..\*], [One revision item for
    each version of the metadata set, including the initial one.],
    [5], [status], [TrackingStatus], [1], [The draft status of the
    metadata set.],
    [6], [version], [Version], [1], [The version of the current metadata
    set.],
    [7], [aliases], [String], [0..\*], [Alternate names for this
    metadata set.],
    [8], [generator], [Generator], [0..1], [Information about the engine
    that generated this metadata set.],
  )]
  , caption: [Type `Tracking` (Record)]
  , kind: table
  )
<tab:tracking-record>

#figure(
  align(center)[#table(
    columns: (5%, 12%, 83%),
    align: (right,left,left,),
    table.header([ID], [Item], [Description],),
    table.hline(),
    [0], [draft], [The metadata set is a draft.],
    [1], [final], [The metadata set is final.],
    [2], [interim], [The metadata set has interim status.],
  )]
  , caption: [Type `TrackingStatus` (Enumerated)]
  , kind: table
  )
<tab:tracking-status-enum>

#figure(
  align(center)[#table(
    columns: (6%, 15%, 15%, 6%, 58%),
    align: (right,left,left,left,left,),
    table.header([ID], [Name], [Type], [\#], [Description],),
    table.hline(),
    [1], [date], [String /date-time], [1], [The date of this revision
    entry.],
    [2], [number], [Version], [1], [The version number of this
    revision.],
    [3], [summary], [String], [1], [A short description of the changes
    in this revision.],
    [4], [legacy-version], [String], [0..1], [A version string from an
    existing set with the same content, tracing from DP-Core compliant
    to historic items.],
  )]
  , caption: [Type `Revision` (Record)]
  , kind: table
  )
<tab:revision-record>

#figure(
  align(center)[#table(
    columns: (6%, 15%, 15%, 6%, 58%),
    align: (right,left,left,left,left,),
    table.header([ID], [Name], [Type], [\#], [Description],),
    table.hline(),
    [1], [engine], [GeneratorEngine], [1], [Information about the engine
    used to generate this metadata set.],
    [2], [date], [String /date-time], [0..1], [The date this metadata
    set was generated.],
  )]
  , caption: [Type `Generator` (Record)]
  , kind: table
  )
<tab:generator-record>

#figure(
  align(center)[#table(
    columns: (6%, 15%, 15%, 6%, 58%),
    align: (right,left,left,left,left,),
    table.header([ID], [Name], [Type], [\#], [Description],),
    table.hline(),
    [1], [name], [String], [1], [The name of the engine that generated
    this metadata set.],
    [2], [version], [Version], [0..1], [The version of the engine that
    generated this metadata set.],
  )]
  , caption: [Type `GeneratorEngine` (Record)]
  , kind: table
  )
<tab:generator-engine-record>

#figure(
  align(center)[#table(
    columns: (6%, 15%, 15%, 6%, 58%),
    align: (right,left,left,left,left,),
    table.header([ID], [Name], [Type], [\#], [Description],),
    table.hline(),
    [1], [category], [NoteCategory], [1], [The category of the note.],
    [2], [text], [String], [1], [The content of the note, varying
    depending on type.],
    [3], [audience], [String], [0..1], [The intended audience for the
    note.],
    [4], [title], [String], [0..1], [A concise description of what is
    contained in the text of the note.],
  )]
  , caption: [Type `Note` (Record)]
  , kind: table
  )
<tab:note-record>

#figure(
  align(center)[#table(
    columns: (4%, 20%, 76%),
    align: (right,left,left,),
    table.header([ID], [Item], [Description],),
    table.hline(),
    [0], [description], [A descriptive note about the subject.],
    [1], [details], [A note with detailed supplemental information.],
    [2], [faq], [A note in frequently-asked-questions format.],
    [3], [general], [A general note.],
    [4], [legal-disclaimer], [A note containing a legal disclaimer.],
    [5], [other], [A note that does not fit other categories.],
    [6], [summary], [A summary note.],
  )]
  , caption: [Type `NoteCategory` (Enumerated)]
  , kind: table
  )
<tab:note-category-enum>

#figure(
  align(center)[#table(
    columns: (6%, 15%, 15%, 6%, 58%),
    align: (right,left,left,left,left,),
    table.header([ID], [Name], [Type], [\#], [Description],),
    table.hline(),
    [1], [summary], [String], [1], [A short description of what this
    reference refers to.],
    [2], [url], [String /uri], [1], [The URL of the referenced
    resource.],
    [3], [category], [ReferenceCategory], [0..1], [Whether this
    reference is external or self-referential.],
  )]
  , caption: [Type `Reference` (Record)]
  , kind: table
  )
<tab:reference-record>

#figure(
  align(center)[#table(
    columns: (5%, 12%, 83%),
    align: (right,left,left,),
    table.header([ID], [Item], [Description],),
    table.hline(),
    [0], [external], [The reference points to an external resource.],
    [1], [self], [The reference points back to the same information item
    in focus.],
  )]
  , caption: [Type `ReferenceCategory` (Enumerated)]
  , kind: table
  )
<tab:reference-category-enum>

== Source
<source>
The `source` member characterizes the content and source of the dataset.

#figure(
  align(center)[#table(
    columns: (6%, 15%, 15%, 6%, 58%),
    align: (right,left,left,left,left,),
    table.header([ID], [Name], [Type], [\#], [Description],),
    table.hline(),
    [1], [about], [About], [1], [A detailed narrative explaining the
    contents, scope, and purpose of the dataset.],
    [2], [id], [Identity], [1], [A unique identifier for this dataset,
    using at least one identification method.],
    [3], [issuer], [Organization], [1..\*], [The legal entity or
    entities responsible for creating the dataset.],
    [4], [location], [String /uri], [1], [The web address where this
    dataset's metadata is published and can be accessed.],
    [5], [name], [String], [1], [The official name of the dataset.],
    [6], [data-version], [Version], [1], [The version of the dataset
    this metadata set describes.],
  )]
  , caption: [Type `Source` (Record)]
  , kind: table
  )
<tab:source-record>

#figure(
  align(center)[#table(
    columns: (6%, 15%, 15%, 6%, 58%),
    align: (right,left,left,left,left,),
    table.header([ID], [Name], [Type], [\#], [Description],),
    table.hline(),
    [1], [content], [String], [1], [Contextual information helping users
    understand what the data represents and how it was collected.],
    [2], [purpose], [String], [1], [The recommended uses for this
    dataset.],
    [3], [scope], [String], [0..1], [Any limitations of the dataset.],
  )]
  , caption: [Type `About` (Record)]
  , kind: table
  )
<tab:about-record>

The `Identity` type provides at least one identifier for the dataset. At
least one of its fields MUST be present.

#figure(
  align(center)[#table(
    columns: (6%, 15%, 15%, 6%, 58%),
    align: (right,left,left,left,left,),
    table.header([ID], [Name], [Type], [\#], [Description],),
    table.hline(),
    [1], [hashes], [HashEntry], [0..\*], [Cryptographic hash-based
    identifiers for the dataset.],
    [2], [uris], [String /uri], [0..\*], [URI identifiers for the
    dataset.],
    [3], [uuids], [String /uuid], [0..\*], [UUID identifiers for the
    dataset.],
    [4], [custom-ids], [CustomId], [0..\*], [Identifiers in any text
    format.],
  )]
  , caption: [Type `Identity` (Map)]
  , kind: table
  )
<tab:identity-map>

#figure(
  align(center)[#table(
    columns: (6%, 15%, 15%, 6%, 58%),
    align: (right,left,left,left,left,),
    table.header([ID], [Name], [Type], [\#], [Description],),
    table.hline(),
    [1], [tree-hashes], [TreeHash], [1..\*], [The cryptographic hash
    values for this file or tree.],
    [2], [path], [String], [1], [The path (file or filesystem tree root)
    identified by these hash values.],
  )]
  , caption: [Type `HashEntry` (Record)]
  , kind: table
  )
<tab:hash-entry-record>

#figure(
  align(center)[#table(
    columns: (6%, 15%, 15%, 6%, 58%),
    align: (right,left,left,left,left,),
    table.header([ID], [Name], [Type], [\#], [Description],),
    table.hline(),
    [1], [algorithm], [String], [1], [The name of the hash or tree/seal
    algorithm used to calculate the value.],
    [2], [value], [String], [1], [The cryptographic hash value in
    hexadecimal representation.],
  )]
  , caption: [Type `TreeHash` (Record)]
  , kind: table
  )
<tab:tree-hash-record>

#figure(
  align(center)[#table(
    columns: (6%, 15%, 15%, 6%, 58%),
    align: (right,left,left,left,left,),
    table.header([ID], [Name], [Type], [\#], [Description],),
    table.hline(),
    [1], [method], [String], [1], [The name of the method used to derive
    this identifier.],
    [2], [value], [String], [1], [The identifier value.],
    [3], [tool], [String], [0..1], [The name of the tool used to derive
    this identifier.],
    [4], [parameter-list], [String], [0..\*], [Parameters used when
    invoking the tool.],
  )]
  , caption: [Type `CustomId` (Record)]
  , kind: table
  )
<tab:custom-id-record>

== Provenance
<provenance>
The `provenance` member describes the provenance of the dataset.

#figure(
  align(center)[#table(
    columns: (6%, 15%, 15%, 6%, 58%),
    align: (right,left,left,left,left,),
    table.header([ID], [Name], [Type], [\#], [Description],),
    table.hline(),
    [1], [origin-geography], [GeographicRegion], [1..\*], [The
    geographical locations where the data was originally collected.],
    [2], [date], [String /date], [1], [The date when the dataset was
    compiled or created (YYYY-MM-DD).],
    [3], [generation-method], [GenerationMethod], [1..\*], [The
    methodology or procedures used to collect, generate, or compile the
    data.],
    [4], [source], [String /uri], [0..1], [The URI of metadata for a
    source dataset contributing to this dataset, establishing lineage.],
    [5], [origin], [Organization], [0..\*], [The original source
    organization, if different from the dataset issuer.],
    [6], [previous-date], [String /date], [0..1], [The release date of
    the previous version of this dataset (YYYY-MM-DD).],
    [7], [generation-period], [GenerationPeriod], [0..1], [The span of
    time during which the data was collected or generated.],
    [8], [format], [ModalityFormat], [0..\*], [Describes the modality or
    media type of the data within the dataset.],
    [9], [sub-provenance], [Provenance], [0..1], [Nested provenance
    information for a component of this dataset.],
  )]
  , caption: [Type `Provenance` (Record)]
  , kind: table
  )
<tab:provenance-record>

#figure(
  align(center)[#table(
    columns: (6%, 15%, 15%, 6%, 58%),
    align: (right,left,left,left,left,),
    table.header([ID], [Name], [Type], [\#], [Description],),
    table.hline(),
    [1], [start], [String /date-time], [0..1], [The start of the data
    collection or generation period.],
    [2], [end], [String /date-time], [0..1], [The end of the data
    collection or generation period.],
  )]
  , caption: [Type `GenerationPeriod` (Record)]
  , kind: table
  )
<tab:generation-period-record>

#figure(
  align(center)[#table(
    columns: (6%, 15%, 15%, 6%, 58%),
    align: (right,left,left,left,left,),
    table.header([ID], [Name], [Type], [\#], [Description],),
    table.hline(),
    [1], [code], [GenerationMethodCode], [1], [A short code identifying
    the generation method.],
    [2], [system], [String], [0..1], [The code system used to interpret
    the code value.],
    [3], [long-description], [String], [0..1], [A detailed description
    of the method.],
  )]
  , caption: [Type `GenerationMethod` (Record)]
  , kind: table
  )
<tab:generation-method-record>

#figure(
  align(center)[#table(
    columns: (5%, 12%, 83%),
    align: (right,left,left,),
    table.header([ID], [Item], [Description],),
    table.hline(),
    [0], [data-augmentation], [Data generation through augmentation of
    existing data.],
    [1], [data-mining], [Data collected through automated data mining.],
    [2], [feeds], [Data received through data feeds.],
    [3], [machine-generated-ml-ops], [Data generated through machine
    learning operations.],
    [4], [other], [A generation method not listed here.],
    [5], [primary-user-source], [Data collected directly from primary
    users.],
    [6], [simulations], [Data generated through simulations.],
    [7], [social-media], [Data collected from social media platforms.],
    [8], [syndication], [Data received through syndication.],
    [9], [transfer-learning], [Data generated through transfer
    learning.],
    [10], [user-generated-content], [Data created by end users.],
    [11], [web-scraping-crawling], [Data collected by web scraping or
    crawling.],
  )]
  , caption: [Type `GenerationMethodCode` (Enumerated)]
  , kind: table
  )
<tab:generation-method-code-enum>

#figure(
  align(center)[#table(
    columns: (5%, 12%, 83%),
    align: (right,left,left,),
    table.header([ID], [Item], [Description],),
    table.hline(),
    [0], [application/json], [JSON data format.],
    [1], [application/jsonld], [JSON-LD linked data format.],
    [2], [application/msword], [Microsoft Word document format.],
    [3], [application/vnd.ms-excel], [Microsoft Excel spreadsheet
    format.],
    [4], [application/zip], [ZIP archive format.],
    [5], [image/bmp], [BMP image format.],
    [6], [image/gif], [GIF image format.],
    [7], [image/jpeg], [JPEG image format.],
    [8], [image/png], [PNG image format.],
    [9], [image/x-png], [PNG image format (legacy media type).],
    [10], [other], [A format not listed here.],
    [11], [text/csv], [CSV text format.],
    [12], [text/plain], [Plain text format.],
  )]
  , caption: [Type `ModalityFormat` (Enumerated)]
  , kind: table
  )
<tab:modality-format-enum>

== Use
<use>
The `use` member describes the legal use and restrictions applicable to
the dataset.

#figure(
  align(center)[#table(
    columns: (6%, 15%, 15%, 6%, 58%),
    align: (right,left,left,left,left,),
    table.header([ID], [Name], [Type], [\#], [Description],),
    table.hline(),
    [1], [intended-purpose], [Purpose], [1..\*], [The purpose or
    purposes for which the dataset was created.],
    [2], [classification], [Classification], [0..\*], [Confidentiality
    classifications applicable to the dataset.],
    [3], [consents], [String], [0..\*], [Locations of consent
    documentation or agreements related to the data.],
    [4], [data-risk-reducing], [DataRiskReducing], [0..\*], [Techniques
    used to reduce known data risk.],
    [5], [processing-included], [GeographicRegion], [0..\*], [Geographical
    boundaries within which the data may be processed.],
    [6], [processing-excluded], [GeographicRegion], [0..\*], [Geographical
    boundaries within which the data may not be processed.],
    [7], [storage-allowed], [GeographicRegion], [0..\*], [Geographical
    locations where the data may be stored.],
    [8], [storage-forbidden], [GeographicRegion], [0..\*], [Geographical
    locations where the data may not be stored.],
    [9], [license], [String], [0..\*], [The terms under which the
    dataset can be used, including any restrictions or obligations.],
    [10], [copyright], [String], [0..\*], [Copyright information
    covering proprietary information in the dataset.],
    [11], [patent], [String], [0..\*], [Patent information covering
    proprietary information in the dataset.],
    [12], [trademark], [String], [0..\*], [Trademark information
    covering proprietary information in the dataset.],
  )]
  , caption: [Type `Use` (Record)]
  , kind: table
  )
<tab:use-record>

#figure(
  align(center)[#table(
    columns: (6%, 15%, 15%, 6%, 58%),
    align: (right,left,left,left,left,),
    table.header([ID], [Name], [Type], [\#], [Description],),
    table.hline(),
    [1], [code], [PurposeCode], [1], [A short code identifying the
    intended purpose.],
    [2], [long-description], [String], [1], [A detailed description of
    the intended purpose.],
    [3], [system], [String], [0..1], [The code system used to interpret
    the code value.],
  )]
  , caption: [Type `Purpose` (Record)]
  , kind: table
  )
<tab:purpose-record>

#figure(
  align(center)[#table(
    columns: (6%, 15%, 15%, 6%, 58%),
    align: (right,left,left,left,left,),
    table.header([ID], [Name], [Type], [\#], [Description],),
    table.hline(),
    [1], [regulation], [Regulation], [1], [The regulation or
    classification standard being evaluated.],
    [2], [evaluated], [Boolean], [1], [Whether the dataset has been
    evaluated against this classification (`true`) or not (`false`).],
    [3], [tool], [String], [0..1], [The tool used to perform the
    evaluation.],
  )]
  , caption: [Type `Classification` (Record)]
  , kind: table
  )
<tab:classification-record>

#figure(
  align(center)[#table(
    columns: (6%, 15%, 15%, 6%, 58%),
    align: (right,left,left,left,left,),
    table.header([ID], [Name], [Type], [\#], [Description],),
    table.hline(),
    [1], [code], [ConfidentialityCode], [1], [A short code identifying
    the confidentiality classification.],
    [2], [system], [String], [0..1], [The code system used to interpret
    the code value.],
    [3], [long-description], [String], [0..1], [A detailed description
    of the regulation or classification.],
  )]
  , caption: [Type `Regulation` (Record)]
  , kind: table
  )
<tab:regulation-record>

#figure(
  align(center)[#table(
    columns: (5%, 12%, 83%),
    align: (right,left,left,),
    table.header([ID], [Item], [Description],),
    table.hline(),
    [0], [other], [A confidentiality classification not listed here.],
    [1], [pci], [Payment Card Industry (PCI) data.],
    [2], [pfi], [Personal Financial Information (PFI).],
    [3], [phi], [Protected Health Information (PHI).],
    [4], [pi], [Personal Information (PI).],
    [5], [sci], [Sensitive Compartmented Information (SCI).],
    [6], [spi], [Sensitive Personal Information (SPI).],
  )]
  , caption: [Type `ConfidentialityCode` (Enumerated)]
  , kind: table
  )
<tab:confidentiality-code-enum>

#figure(
  align(center)[#table(
    columns: (5%, 12%, 83%),
    align: (right,left,left,),
    table.header([ID], [Item], [Description],),
    table.hline(),
    [0], [alignment], [Dataset intended for model alignment tasks.],
    [1], [evaluation], [Dataset intended for evaluation or
    benchmarking.],
    [2], [other], [A purpose not listed here.],
    [3], [pre-training], [Dataset intended for model pre-training.],
    [4], [production], [Dataset intended for production use.],
    [5], [quality-assurance], [Dataset intended for quality assurance
    testing.],
    [6], [research], [Dataset intended for research use.],
    [7], [staging-testing], [Dataset intended for staging or testing
    environments.],
    [8], [synthetic-data-generation], [Dataset intended for generating
    synthetic data.],
  )]
  , caption: [Type `PurposeCode` (Enumerated)]
  , kind: table
  )
<tab:purpose-code-enum>

#figure(
  align(center)[#table(
    columns: (6%, 15%, 15%, 6%, 58%),
    align: (right,left,left,left,left,),
    table.header([ID], [Name], [Type], [\#], [Description],),
    table.hline(),
    [1], [tool-used], [String], [1], [The name of the tool used for data
    risk reduction.],
    [2], [tool-category], [Method], [0..1], [The category of the tool
    used for data risk reduction.],
    [3], [technology], [DataTechnology], [0..1], [The privacy-enhancing
    or data-reducing technology applied.],
    [4], [parameters], [Parameter], [0..\*], [The parameters passed to
    the tool.],
    [5], [results], [String], [0..\*], [The results of applying the
    tool.],
  )]
  , caption: [Type `DataRiskReducing` (Record)]
  , kind: table
  )
<tab:data-risk-reducing-record>

#figure(
  align(center)[#table(
    columns: (6%, 15%, 15%, 6%, 58%),
    align: (right,left,left,left,left,),
    table.header([ID], [Name], [Type], [\#], [Description],),
    table.hline(),
    [1], [name], [String], [1], [The parameter name.],
    [2], [value], [String], [0..1], [The parameter value.],
  )]
  , caption: [Type `Parameter` (Record)]
  , kind: table
  )
<tab:parameter-record>

#figure(
  align(center)[#table(
    columns: (5%, 12%, 83%),
    align: (right,left,left,),
    table.header([ID], [Item], [Description],),
    table.hline(),
    [0], [data-anonymization], [Transforms the dataset so that
    individuals cannot be identified, directly or indirectly, from the
    resulting records.],
    [1], [data-encryption], [Encodes dataset content so that it is
    readable only by parties holding the decryption key; typically
    applied at rest or in transit.],
    [2], [data-masking], [Replaces sensitive field values with realistic
    but fictitious substitutes, preserving format and statistical
    properties without exposing the originals.],
    [3], [data-minimization], [Reduces the dataset to only the fields
    and records necessary for the stated purpose, limiting exposure of
    personal or sensitive data.],
    [4], [data-redaction], [Removes or obscures specific values or text
    spans identified as sensitive, such as names, identifiers, or health
    information.],
    [5], [differential-privacy], [Adds calibrated statistical noise so
    that the presence or absence of any individual record cannot be
    reliably inferred from the released data.],
    [6], [federated-learning], [Produces model artefacts by training
    across distributed sources without centralising raw data, so the
    original dataset is never directly shared.],
    [7], [homomorphic-encryption], [Enables computation on ciphertext
    without decryption, so analytical results can be derived without
    exposing plaintext values.],
    [8], [k-anonymity], [Generalises quasi-identifying attributes so
    that each record is indistinguishable from at least k-1 other
    records in the dataset.],
    [9], [l-diversity], [Extends k-anonymity by requiring that each
    equivalence class contains at least l well-represented distinct
    sensitive attribute values.],
    [10], [other], [A data risk reduction technology not covered by the
    defined values; use `tool-category` or `results` to describe the
    specific technique applied.],
    [11], [pseudonymization], [Replaces direct identifiers with
    artificial pseudonyms; re-identification remains possible through a
    separate, controlled mapping table.],
    [12], [secure-multi-party-computation], [Allows multiple parties to
    jointly compute over their respective inputs without revealing those
    inputs to each other (SMC).],
    [13], [t-closeness], [Extends l-diversity by requiring that the
    distribution of sensitive values within each equivalence class
    closely matches their overall distribution in the dataset.],
    [14], [tokenization], [Substitutes sensitive values with
    non-sensitive tokens; the originals are recoverable only through a
    separate, secured token vault.],
  )]
  , caption: [Type `DataTechnology` (Enumerated)]
  , kind: table
  )
<tab:data-technology-enum>

== Shared Types
<shared-types>
The following types are used in more than one of the sections above.

#figure(
  align(center)[#table(
    columns: (6%, 15%, 15%, 6%, 58%),
    align: (right,left,left,left,left,),
    table.header([ID], [Name], [Type], [\#], [Description],),
    table.hline(),
    [1], [legal-name], [String], [1], [The legal name of the
    organization.],
    [2], [address], [Address], [0..1], [The postal address of the
    organization.],
    [3], [url], [String /uri], [0..1], [A URL for the organization.],
  )]
  , caption: [Type `Organization` (Record)]
  , kind: table
  )
<tab:organization-record>

#figure(
  align(center)[#table(
    columns: (5%, 12%, 83%),
    align: (left,left,left,),
    table.header([Type Name], [Type Definition], [Description],),
    table.hline(),
    [Address], [ArrayOf(String)], [Lines of a postal address. At least
    one required.],
  )]
  , caption: [Type `Address` (ArrayOf(String))]
  , kind: table
  )
<tab:address-array>

#figure(
  align(center)[#table(
    columns: (6%, 15%, 15%, 6%, 58%),
    align: (right,left,left,left,left,),
    table.header([ID], [Name], [Type], [\#], [Description],),
    table.hline(),
    [1], [country], [String], [1], [The country name or code.],
    [2], [state], [String], [0..1], [The state or province name or
    code.],
  )]
  , caption: [Type `GeographicRegion` (Record)]
  , kind: table
  )
<tab:geographic-region-record>

#figure(
  align(center)[#table(
    columns: (6%, 15%, 15%, 6%, 58%),
    align: (right,left,left,left,left,),
    table.header([ID], [Name], [Type], [\#], [Description],),
    table.hline(),
    [1], [code], [String], [1], [A short code identifying the method,
    regulation, or classification.],
    [2], [system], [String], [0..1], [The code system used to interpret
    the code value.],
    [3], [long-description], [String], [0..1], [A detailed description
    of the method, regulation, or classification.],
  )]
  , caption: [Type `Method` (Record)]
  , kind: table
  )
<tab:method-record>

The `Acknowledgment` type describes a contributor. At least one of its
fields MUST be present.

#figure(
  align(center)[#table(
    columns: (6%, 15%, 15%, 6%, 58%),
    align: (right,left,left,left,left,),
    table.header([ID], [Name], [Type], [\#], [Description],),
    table.hline(),
    [1], [names], [String], [0..\*], [Names of individual contributors
    being acknowledged.],
    [2], [organization], [String], [0..1], [Name of a contributing
    organization being acknowledged.],
    [3], [summary], [String], [0..1], [Contextual details about the
    acknowledgment.],
    [4], [urls], [String /uri], [0..\*], [URLs of references being
    acknowledged.],
  )]
  , caption: [Type `Acknowledgment` (Map)]
  , kind: table
  )
<tab:acknowledgment-map>

#figure(
  align(center)[#table(
    columns: (5%, 12%, 83%),
    align: (left,left,left,),
    table.header([Type Name], [Type Definition], [Description],),
    table.hline(),
    [Version], [String], [An integer or semantic versioning string.
    Examples: `"1"`, `"2.0.0"`, `"1.0.0-beta"`.],
  )]
  , caption: [Type `Version` (String)]
  , kind: table
  )
<tab:version-string>

#figure(
  align(center)[#table(
    columns: (5%, 12%, 83%),
    align: (left,left,left,),
    table.header([Type Name], [Type Definition], [Description],),
    table.hline(),
    [Language], [String], [A language tag conforming to IETF BCP 47 /
    RFC 5646.],
  )]
  , caption: [Type `Language` (String)]
  , kind: table
  )
<tab:language-string>

#pagebreak(weak: true)
= Provenance Information Model Encoding
<provenance-information-model-encoding>
The technical encoding of the information model is specified in both
JADN and YAML in the following subsections.

== JADN Encoding
<jadn-encoding>
The JADN encoding of the data provenance metadata information model is
specified in `jadn/data-provenance.jadn`.

The file contains 43 named types derived directly from the property
tables in Section 5. The exported root type is `DataProvenance`. Six
named primitive aliases (`URI`, `UUID`, `DateTime`, `Date`, `Version`,
`Language`) carry format constraints that apply wherever those types
appear as field types, keeping the field-level definitions free of
inline format options. Eight enumerated types carry the closed code
vocabularies introduced in Section 5.

== YAML Encoding
<yaml-encoding>
The YAML encoding of the data provenance metadata information model is
specified in `yaml/data-provenance.yaml`.

This file is a YAML serialization of `json/data-provenance.json` and is
normatively equivalent to it. It is provided for tooling that consumes
YAML-format schemas natively. All field names, constraints, type
references, and enumeration values are identical to those in the JSON
schema.

#pagebreak(weak: true)
= Provenance Data Model Encoding
<provenance-data-model-encoding>
#quote(block: true)[
The information model defines the complete set of metadata elements and
associated attributes specified by the Data Provenance Standard. It
establishes a common conceptual framework for representing provenance
information, including the structures and relationships necessary to
describe the origin, history, and handling of data. The information
model is intended to provide a consistent semantic basis for provenance
across implementations, independent of any particular serialization or
storage mechanism.

In order to support interoperability and exchange of provenance
information between systems, the information model requires one or more
concrete encodings. An encoding provides a standardized,
machine-readable representation of the information model suitable for
electronic transmission, persistence, and processing. While the
information model defines what information is conveyed, the encoding
defines how that information is represented for exchange between
conforming implementations.

This section describes a set of possible encodings for the Data
Provenance Standard. Each encoding maps the constructs defined in the
information model to a specific representation format intended for
storage or system-to-system exchange. The encodings described herein are
non-exclusive and are provided to support diverse implementation
environments and usage scenarios. Implementations MAY support one or
more of these encodings, subject to their interoperability, performance,
and deployment requirements.
]

== JSON Encoding
<json-encoding>
The technical encoding of the data provenance metadata data model is
specified in the following schema artifacts for JSON data:

- Data Provenance Metadata JSON schema
- Data Provenance Metadata Configuration JSON schema

The Data Provenance Metadata Configuration JSON schema configures
validators to enforce all type and subtype constraints.

The Data Provenance Metadata JSON schema provides definitions and the
structure for any data provenance metadata JSON instance.

The required top-level members are:

```yaml
DataProvenance:
  $schema: String.Constant
  set: Mapping
  source: Mapping
  provenance: Mapping
  use: Mapping
```

=== Member `$schema`
<member-schema>
The value of the `$schema` member for this version of the specification
is always:

```
https://docs.oasis-open.org/dps/prov-meta/v1.0/schema/data-provenance.json
```

=== Member `set`
<member-set>
The `set` member specifies set-level meta-data. It captures meta-data
about the provenance metadata record describing a particular dataset.

The required members of `set` are `category`, `schema-version`,
`publisher`, `label`, and `tracking`. The optional members `language`,
`source-language`, `acknowledgments`, `notes`, and `references` MAY also
be present.

```yaml
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

==== Member `set.category`
<member-set-category>
The `set.category` member defines a short canonical name, chosen by the
set producer, which will inform the end user as to the category of the
metadata set.

```yaml
DataProvenance:
  # ...
  set:
    category: String.Pattern
    # ...
  # ...
# ...
```

#emph[Examples 1:]#box()<member-set-category-eg-1>

```
dp_base
dp_event_source
dp_profile_xyz
Example Data Protection Notice Exemption
```

==== Member `set.schema-version`
<member-set-schema-version>
The `set.schema-version` member gives the version of the Data Provenance
Core specification which the document was generated for.

```yaml
DataProvenance:
  # ...
  set:
    # ...
    schema-version: String.Constant
    # ...
  # ...
# ...
```

The value of the `set.schema-version` member for this version of the
specification is always:

```
1.0
```

==== Member `set.publisher`
<member-set-publisher>
The `set.publisher` member provides information about the publisher of
the metadata set. The publisher is the party responsible for issuing the
metadata set.

The required members of `set.publisher` are `name` and `namespace`. The
optional member `contact-details` MAY also be present.

```yaml
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

===== Member `set.publisher.name`
<member-set-publisher-name>
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
# ...
```

#emph[Example 1:]#box()<member-set-publisher-name-eg-1>

```
Cisco
```

===== Member `set.publisher.namespace`
<member-set-publisher-namespace>
The `set.publisher.namespace` member contains a URI which is under the
control of the issuing party and can be used as a globally unique
identifier for that issuing party.

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
# ...
```

The value of `set.publisher.namespace` MUST be a valid URI.

#emph[Example 1:]#box()<member-set-publisher-namespace-eg-1>

```
https://cisco.com
```

===== Member `set.publisher.contact-details`
<member-set-publisher-contact-details>
The `set.publisher.contact-details` member provides information on how
to contact the publisher, such as web sites, email addresses, phone
numbers, or postal mail addresses.

```yaml
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

#emph[Example 1:]#box()<member-set-publisher-contact-details-eg-1>

```
Example Company can be reached at contact_us@example.com, or via our website at https://www.example.com/contact.
```

==== Member `set.label`
<member-set-label>
The `set.label` member provides the per-publisher unique title of the
metadata set.

```yaml
DataProvenance:
  # ...
  set:
    # ...
    label: String
    # ...
  # ...
# ...
```

The value of `set.label` SHOULD be a canonical name for the set, and
sufficiently unique to distinguish it from similar sets.

#emph[Examples 1:]#box()<member-set-label-eg-1>

```
Learning Set for Regression Modelling for Stats 101
Example Data Protection Dataset in Example Generator
```

==== Member `set.tracking`
<member-set-tracking>
The `set.tracking` member is a container designated to hold all
management attributes necessary to track a DP-Core set as a whole.

The required members of `set.tracking` are `current-release-date`, `id`,
`initial-release-date`, `revision-history`, `status`, and `version`. The
optional members `aliases` and `generator` MAY also be present.

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
      # aliases: Sequence   (optional)
      # generator: Mapping  (optional)
    # ...
  # ...
# ...
```

===== Member `set.tracking.current-release-date`
<member-set-tracking-current-release-date>
The `set.tracking.current-release-date` member contains the date when
the current revision of this document was released.

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
# ...
```

The value of `set.tracking.current-release-date` MUST be a valid
date-time string conforming to \[RFC 3339\].

#emph[Example 1:]#box()<member-set-tracking-current-release-date-eg-1>

```
2000-01-01T01:01:01Z
```

===== Member `set.tracking.id`
<member-set-tracking-id>
The `set.tracking.id` member provides the unique identifier for the
metadata set. The ID is a simple label that provides for a wide range of
numbering values, types, and schemes. Its value SHOULD be assigned and
maintained by the original metadata set issuing authority.

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
# ...
```

The value of `set.tracking.id` MUST NOT start or end with whitespace.

#emph[Examples 1:]#box()<member-set-tracking-id-eg-1>

```
7aedeb0a-22dd-428a-ab76-c950b43cbbc6
abcdef-orga-ds-0815
cisco-sa-20190513-secureboot
```

===== Member `set.tracking.initial-release-date`
<member-set-tracking-initial-release-date>
The `set.tracking.initial-release-date` member contains the date when
this set was first published.

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
# ...
```

The value of `set.tracking.initial-release-date` MUST be a valid
date-time string conforming to \[RFC 3339\].

#emph[Example 1:]#box()<member-set-tracking-initial-release-date-eg-1>

```
2000-01-01T01:01:01Z
```

===== Member `set.tracking.revision-history`
<member-set-tracking-revision-history>
The `set.tracking.revision-history` member holds one revision item for
each version of the DP-Core set, including the initial one. The sequence
MUST contain at least one revision item.

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
          # legacy-version: String  (optional)
      # ...
    # ...
  # ...
# ...
```

Each revision item MUST contain the following members:

- `date`: The date of the revision entry. MUST be a valid date-time
  string conforming to \[RFC 3339\].
- `number`: The version number of the revision. MUST conform to
  `$defs.version-type` (integer or semantic versioning string).
- `summary`: A short description of the changes made in this revision.

The optional `legacy-version` member traces entries back to historic,
DP-Core-unaware version strings.

#emph[Example 1:]#box()<member-set-tracking-revision-history-eg-1>

```json
[
  {
    "date": "2000-01-01T01:01:01Z",
    "number": "1",
    "summary": "Initial version."
  }
]
```

===== Member `set.tracking.status`
<member-set-tracking-status>
The `set.tracking.status` member defines the draft status of the
metadata set. This allows processing DP-Core sets of various maturity
per version.

```yaml
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

===== Member `set.tracking.version`
<member-set-tracking-version>
The `set.tracking.version` member specifies the version of the current
DP-Core set.

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
# ...
```

The value of `set.tracking.version` MUST conform to
`$defs.version-type`, which requires either an integer or a semantic
versioning string.

#emph[Examples 1:]#box()<member-set-tracking-version-eg-1>

```
1
2.0.0
1.0.0-beta+exp.sha.a1c44f85
```

===== Member `set.tracking.aliases`
<member-set-tracking-aliases>
The `set.tracking.aliases` member contains a list of alternate names for
the same set. Each alias MUST be a non-empty string and all entries MUST
be unique.

```yaml
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

#emph[Example 1:]#box()<member-set-tracking-aliases-eg-1>

```json
["0bacba95-ceb9-4fae-bf07-d5683a9481c1"]
```

===== Member `set.tracking.generator`
<member-set-tracking-generator>
The `set.tracking.generator` member holds information about the engine
that generated the metadata set. The required sub-member is `engine`.
The optional sub-member `date` MAY also be present.

```yaml
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

- `engine.name`: The name of the tool or system that produced the
  metadata set.
- `engine.version`: The version of that tool. MUST conform to
  `$defs.version-type` when present.
- `date`: The date-time at which the metadata set was generated. MUST
  conform to \[RFC 3339\] when present.

#emph[Example 1:]#box()<member-set-tracking-generator-eg-1>

```json
{
  "engine": {"name": "DPCoreX", "version": "1.0.0"},
  "date": "2025-01-15T10:00:00Z"
}
```

==== Member `set.language`
<member-set-language>
The `set.language` member identifies the language used in this document,
corresponding to IETF BCP 47 / RFC 5646.

```yaml
DataProvenance:
  # ...
  set:
    # ...
    language: String.BCP47
    # ...
  # ...
# ...
```

#emph[Examples 1:]#box()<member-set-language-eg-1>

```
de
en
fr
```

==== Member `set.source-language`
<member-set-source-language>
The `set.source-language` member identifies the language this document
was translated from, when this copy is a translation.

```yaml
DataProvenance:
  # ...
  set:
    # ...
    source-language: String.BCP47
    # ...
  # ...
# ...
```

==== Member `set.acknowledgments`
<member-set-acknowledgments>
The `set.acknowledgments` member contains a list of acknowledgment
elements associated with the whole set. Each acknowledgment item MUST
have at least one of the following members: `names`, `organization`,
`summary`, or `urls`.

```yaml
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

#emph[Example 1:]#box()<member-set-acknowledgments-eg-1>

```json
[
  {
    "names": ["A. Big Data"],
    "organization": "ETH Zurich",
    "summary": "First analysis of the merged data-set"
  }
]
```

==== Member `set.notes`
<member-set-notes>
The `set.notes` member contains a list of notes associated with this
metadata set. Each note MUST have a `category` and `text`. The optional
members `audience` and `title` MAY also be present. The `category` value
MUST be one of: `general`, `other`, `privacy`, `summary`.

```yaml
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
- `title`: A concise description of what is contained in the text of the
  note.

==== Member `set.references`
<member-set-references>
The `set.references` member contains a list of references associated
with this metadata set. Each reference MUST have a `summary` and a
`url`. The optional member `category` MAY also be present. The
`category` value MUST be one of: `external`, `self`.

```yaml
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
- `category`: Whether this reference is external or self-referential
  (default: `external`).

=== Member `source`
<member-source>
The `source` member characterizes the content and source of the dataset.
All six of its members are required.

```yaml
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

==== Member `source.about`
<member-source-about>
The `source.about` member contains a detailed narrative that explains
the contents, scope, and purpose of the dataset. The required members
are `content` and `purpose`. The optional member `scope` MAY also be
present.

```yaml
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

- `content`: Provides essential contextual information that helps users
  understand what the data represents and how it was collected.
- `purpose`: Explains the recommended uses.
- `scope`: Points out any limitations of the dataset.

#emph[Example 1:]#box()<member-source-about-eg-1>

```json
{
  "content": "We found these numbers on the parking lot.",
  "purpose": "Use only for learning regression modeling. Not for production use.",
  "scope": "We did not verify anything. Use at your own risk."
}
```

==== Member `source.id`
<member-source-id>
The `source.id` member provides a unique identifier for the dataset's
metadata. At least one identification method MUST be provided.

```yaml
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

- `hashes`: A list of cryptographic hash entries, each containing
  `tree-hashes` (a list of `{algorithm, value}` pairs) and a `path`.
- `uris`: A list of identifiers in URI format.
- `uuids`: A list of identifiers in UUID format.
- `custom-ids`: A list of identifiers in any text format, each with a
  required `method` and `value`, and optional `tool` and
  `parameter-list`.

#emph[Example 1:]#box()<member-source-id-eg-1>

```json
{
  "uuids": ["e5471657-9ede-4335-843b-c1376ef29bfa"]
}
```

#emph[Example 2:]#box()<member-source-id-eg-2>

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

==== Member `source.issuer`
<member-source-issuer>
The `source.issuer` member identifies the legal entity or entities
responsible for creating the dataset. The value is a sequence of
organization objects. Each organization MUST provide a `legal-name`. The
sequence MUST contain at least one organization and all entries MUST be
unique. The optional members `address` and `url` MAY also be present in
each organization.

```yaml
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

#emph[Example 1:]#box()<member-source-issuer-eg-1>

```json
[
  {
    "legal-name": "Sampling Ltd.",
    "url": "https://example.com/smplng/about"
  }
]
```

==== Member `source.location`
<member-source-location>
The `source.location` member provides the web address where the
dataset's metadata is published and can be accessed. Typically this will
be a unique URI of the current dataset.

```yaml
DataProvenance:
  # ...
  source:
    # ...
    location: String.URI
    # ...
  # ...
# ...
```

==== Member `source.name`
<member-source-name>
The `source.name` member provides the official name of the dataset,
which should be descriptive and help easily identify the dataset's
content and purpose.

```yaml
DataProvenance:
  # ...
  source:
    # ...
    name: String
    # ...
  # ...
# ...
```

==== Member `source.data-version`
<member-source-data-version>
The `source.data-version` member specifies the version of the dataset
this DP-Core set describes, allowing the dataset to evolve over time and
keeping consistent labeling.

```yaml
DataProvenance:
  # ...
  source:
    # ...
    data-version: $defs.version-type
    # ...
  # ...
# ...
```

The value of `source.data-version` MUST conform to `$defs.version-type`,
which requires either an integer or a semantic versioning string.

#emph[Examples 1:]#box()<member-source-data-version-eg-1>

```
1
2.0.0
```

=== Member `provenance`
<member-provenance>
The `provenance` member describes the provenance of the dataset.

The required members are `origin-geography`, `date`, and
`generation-method`. The optional members `source`, `origin`,
`previous-date`, `generation-period`, `format`, and `sub-provenance` MAY
also be present.

```yaml
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

The required members of `provenance` are described in subsections
7.1.4.1--7.1.4.3; optional members in 7.1.4.4--7.1.4.9.

==== Member `provenance.origin-geography`
<member-provenance-origin-geography>
The `provenance.origin-geography` member identifies the geographical
locations where the data was originally collected, which can be
important for compliance with regional laws and understanding the data's
context.

The value is a sequence of geographic region objects. Each entry MUST
contain a `country`. The optional `state` member MAY also be present.
The sequence MUST contain at least one entry and all entries MUST be
unique.

```yaml
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

#emph[Example 1:]#box()<member-provenance-origin-geography-eg-1>

```json
[
  {"country": "US"},
  {"country": "DE", "state": "Bavaria"}
]
```

==== Member `provenance.date`
<member-provenance-date>
The `provenance.date` member provides the date when the dataset was
compiled or created, providing a temporal context for the data.

```yaml
DataProvenance:
  # ...
  provenance:
    # ...
    date: String.Date
    # ...
  # ...
# ...
```

The value of `provenance.date` MUST be a valid date string in full-date
format (YYYY-MM-DD).

#emph[Example 1:]#box()<member-provenance-date-eg-1>

```
2000-01-01
```

==== Member `provenance.generation-method`
<member-provenance-generation-method>
The `provenance.generation-method` member describes the methodology or
procedures used to collect, generate, or compile the data, giving
insight into its reliability and validity.

The value is a sequence of method objects. Each method MUST contain a
`code` drawn from the `GenerationMethodCode` vocabulary. The optional
members `system` and `long-description` MAY also be present. The
sequence MUST contain at least one method and all entries MUST be
unique.

```yaml
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

#emph[Example 1:]#box()<member-provenance-generation-method-eg-1>

```json
[
  {"code": "web-scraping-crawling"},
  {"code": "primary-user-source", "long-description": "Direct survey responses from participants."}
]
```

==== Member `provenance.source`
<member-provenance-source>
The `provenance.source` member identifies where the metadata for the
source dataset contributing to the current dataset can be found,
establishing lineage.

```yaml
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

#emph[Example 1:]#box()<member-provenance-source-eg-1>

```
https://example.com/datasets/source-dataset-42/provenance.json
```

==== Member `provenance.origin`
<member-provenance-origin>
The `provenance.origin` member identifies the original source
organization when it differs from the issuer of the dataset. The value
is a sequence of organization objects following the same structure as
`source.issuer`.

```yaml
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

#emph[Example 1:]#box()<member-provenance-origin-eg-1>

```json
[{"legal-name": "Original Data Collector Inc."}]
```

==== Member `provenance.previous-date`
<member-provenance-previous-date>
The `provenance.previous-date` member provides the release date of the
previous version of the dataset, to track changes and updates over time.

```yaml
DataProvenance:
  # ...
  provenance:
    # ...
    previous-date: String.Date
    # ...
  # ...
# ...
```

The value of `provenance.previous-date` MUST be a valid date string in
full-date format (YYYY-MM-DD).

#emph[Example 1:]#box()<member-provenance-previous-date-eg-1>

```
1999-06-15
```

==== Member `provenance.generation-period`
<member-provenance-generation-period>
The `provenance.generation-period` member describes the span of time
during which the data within the dataset was collected or generated.
Both `start` and `end` are optional but MUST each conform to \[RFC
3339\] when present.

```yaml
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

#emph[Example 1:]#box()<member-provenance-generation-period-eg-1>

```json
{
  "start": "1998-01-01T00:00:00Z",
  "end": "1999-12-31T23:59:59Z"
}
```

==== Member `provenance.format`
<member-provenance-format>
The `provenance.format` member describes the modality or media type of
the data within the dataset. The value is a sequence of `ModalityFormat`
values. The sequence MUST contain at least one entry and all entries
MUST be unique.

```yaml
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

#emph[Example 1:]#box()<member-provenance-format-eg-1>

```json
["text/csv", "application/json"]
```

==== Member `provenance.sub-provenance`
<member-provenance-sub-provenance>
The `provenance.sub-provenance` member holds provenance information for
a component of the current dataset, enabling a recursive provenance
tree. Its structure is identical to the enclosing `provenance` member.

```yaml
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

=== Member `use`
<member-use>
The `use` member describes legal use and restrictions that apply to the
dataset.

The only required member is `intended-purpose`. All other members are
optional.

```yaml
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

==== Member `use.intended-purpose`
<member-use-intended-purpose>
The `use.intended-purpose` member describes the purpose for which the
dataset was created, guiding users on its intended use and potential
applications.

The value is a sequence of purpose objects. Each purpose MUST contain a
`code` drawn from the `PurposeCode` vocabulary and a `long-description`.
The optional `system` member MAY also be present. The sequence MUST
contain at least one purpose and all entries MUST be unique.

```yaml
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

#emph[Example 1:]#box()<member-use-intended-purpose-eg-1>

```json
[
  {
    "code": "research",
    "long-description": "Use only for learning regression modeling. Not for production use."
  }
]
```

==== Member `use.classification`
<member-use-classification>
The `use.classification` member indicates whether the dataset includes
data falling into various confidentiality classifications. The value is
a sequence of classification objects. Each item MUST contain a
`regulation` object whose `code` MUST be drawn from the
`ConfidentialityCode` vocabulary, and an `evaluated` boolean. The
optional `tool` member MAY also be present. All entries MUST be unique.

```yaml
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

#emph[Example 1:]#box()<member-use-classification-eg-1>

```json
[
  {"regulation": {"code": "phi"}, "evaluated": true},
  {"regulation": {"code": "pii"}, "evaluated": false}
]
```

==== Member `use.consents`
<member-use-consents>
The `use.consents` member specifies where consent documentation or
agreements related to the data can be found, ensuring legal compliance
and regulatory use. The value is a sequence of strings. The sequence
MUST contain at least one entry and all entries MUST be unique.

```yaml
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

#emph[Example 1:]#box()<member-use-consents-eg-1>

```json
["https://example.com/consent-policy-2024"]
```

==== Member `use.data-risk-reducing`
<member-use-data-risk-reducing>
The `use.data-risk-reducing` member indicates the techniques used to
reduce known data risk. The value is a sequence of objects. Each item
MUST contain `tool-used`. The optional members `tool-category`,
`technology`, `parameters`, and `results` MAY also be present. All
entries MUST be unique.

```yaml
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

#emph[Example 1:]#box()<member-use-data-risk-reducing-eg-1>

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

==== Member `use.processing-included`
<member-use-processing-included>
The `use.processing-included` member defines the geographical boundaries
within which the data MAY be processed. The value is a sequence of
geographic region objects following the same structure as
`provenance.origin-geography`.

```yaml
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

#emph[Example 1:]#box()<member-use-processing-included-eg-1>

```json
[{"country": "DE"}, {"country": "FR"}]
```

==== Member `use.processing-excluded`
<member-use-processing-excluded>
The `use.processing-excluded` member defines the geographical boundaries
within which the data MUST NOT be processed. The value is a sequence of
geographic region objects following the same structure as
`provenance.origin-geography`.

```yaml
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

==== Member `use.storage-allowed`
<member-use-storage-allowed>
The `use.storage-allowed` member specifies geographical locations where
the data MAY be stored. The value is a sequence of geographic region
objects following the same structure as `provenance.origin-geography`.

```yaml
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

==== Member `use.storage-forbidden`
<member-use-storage-forbidden>
The `use.storage-forbidden` member specifies geographical locations
where the data MUST NOT be stored. The value is a sequence of geographic
region objects following the same structure as
`provenance.origin-geography`.

```yaml
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

==== Member `use.license`
<member-use-license>
The `use.license` member details the terms under which the dataset can
be used, including any restrictions or obligations. License entries MAY
include End User License Agreements (EULA) or Data Use Agreements (DUA).
The value is a sequence of strings. The sequence MUST contain at least
one entry and all entries MUST be unique.

```yaml
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

#emph[Example 1:]#box()<member-use-license-eg-1>

```json
["https://creativecommons.org/licenses/by/4.0/"]
```

==== Member `use.copyright`
<member-use-copyright>
The `use.copyright` member indicates whether the dataset contains
proprietary information covered by a copyright, and the terms of that
copyright. The value is a sequence of strings. The sequence MUST contain
at least one entry and all entries MUST be unique.

```yaml
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

#emph[Example 1:]#box()<member-use-copyright-eg-1>

```json
["Copyright © 2024 Example Corp. All rights reserved."]
```

==== Member `use.patent`
<member-use-patent>
The `use.patent` member indicates whether the dataset contains
proprietary information covered by a patent, and the patent number. The
value is a sequence of strings. The sequence MUST contain at least one
entry and all entries MUST be unique.

```yaml
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

==== Member `use.trademark`
<member-use-trademark>
The `use.trademark` member indicates whether the dataset contains
proprietary information covered by a trademark, and the terms of that
trademark. The value is a sequence of strings. The sequence MUST contain
at least one entry and all entries MUST be unique.

```yaml
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

#pagebreak(weak: true)
= Safety, Security, and Data Protection
<safety-security-and-data-protection>
All safety, security, and data protection requirements relevant to the
context in which Data Provenance Metadata documents are used MUST be
translated into, and consistently enforced through, Data Provenance
Metadata implementations and processes.

For Data Provenance Metadata documents based on JSON, the security
considerations of \[#link(<RFC8259>)[RFC8259]\] apply and are repeated
here as a service for the reader:

#quote(block: true)[
Generally, there are security issues with scripting languages. JSON is a
subset of JavaScript but excludes assignment and invocation.

Since JSON's syntax is borrowed from JavaScript, it is possible to use
that language's `eval()` function to parse most JSON texts (but not all;
certain characters such as `U+2028 LINE SEPARATOR` and
`U+2029 PARAGRAPH SEPARATOR` are legal in JSON but not JavaScript). This
generally constitutes an unacceptable security risk, since the text
could contain executable code along with data declarations. The same
consideration applies to the use of eval()-like functions in any other
programming language in which JSON texts conform to that language's
syntax.
]

Implementations SHOULD validate Data Provenance Metadata documents
against the normative JSON Schema prior to processing. Documents that do
not validate MUST NOT be treated as authoritative provenance records.

== Integrity and Authenticity of Provenance Claims
<integrity-and-authenticity>
This specification defines the structure and vocabulary of provenance
metadata but does not define mechanisms for verifying that the claims
made within a record are accurate or have not been tampered with. A Data
Provenance Metadata document is only as trustworthy as the process and
party that produced it.

Implementations that rely on provenance metadata for access control,
compliance, or risk decisions SHOULD obtain records through channels
that provide integrity guarantees, such as transport-layer security
(TLS) when fetching from the URI identified in `source.location`, or
cryptographic signatures applied to the document by the `set.publisher`.

The `set.tracking.id` and `source.id` fields provide identifiers for the
record and the described dataset respectively, but do not themselves
provide integrity protection.

== URI Safety
<uri-safety>
Several fields in this specification accept URI values, including
`source.location`, `set.publisher.namespace`, `source.id.uris`,
`set.acknowledgments[].urls`, and `set.references[].url`.
Implementations that automatically dereference these URIs MUST apply the
same defences required for any externally supplied URL, including
protection against server-side request forgery (SSRF) and open redirect
attacks. URIs MUST be validated as well-formed before dereferencing.
Implementations SHOULD restrict dereferenceable schemes to `https` and,
where appropriate, `http`.

== Sensitive Information in Provenance Records
<sensitive-information>
Provenance records may incidentally contain information that publishers
consider sensitive, including internal tool names in
`use.data-risk-reducing`, personnel names in `set.acknowledgments`,
internal geographic constraints in `use.processing-included` and related
fields, and organizational contact details in
`set.publisher.contact-details`.

Publishers MUST consider whether information included in a provenance
record is appropriate for the audience that will consume it. Provenance
records intended for public distribution SHOULD be reviewed to ensure
they do not expose internal operational details beyond what is required
to describe the dataset's provenance.

== Data Protection Compliance
<data-protection-compliance>
The `use.classification` field records whether a dataset has been
evaluated against confidentiality classifications such as PHI, PI, PCI,
SCI, or SPI. The presence of a classification entry, including the value
of the `evaluated` field, does not itself constitute compliance with any
applicable law or regulation. Implementers that process datasets
described by provenance records containing such classifications MUST
apply the data handling controls required by the relevant regulations in
the jurisdictions where the data is processed and stored.

The geographic restriction fields (`use.processing-included`,
`use.processing-excluded`, `use.storage-allowed`,
`use.storage-forbidden`) express the publisher's stated intent but are
not self-enforcing. Implementers are responsible for establishing
technical and organizational controls that honour these restrictions.

#pagebreak(weak: true)
= Conformance
<conformance>
This document defines requirements for the data-provenance in the JSON
file format and for certain software components that interact with it.

#pagebreak(weak: true)
#heading(level: 1, numbering: none)[Annex A. License, Document Status
and Notices]
<annex-a>
\(This annex forms an integral part of this Specification.)

#heading(level: 2, numbering: none)[A.1 Document Status]
<document-status>
This document was last revised or approved by the OASIS DPS TC on the
above date. The level of approval is also listed above. Check the
"Latest version" location noted above for possible later revisions of
this document. Any other numbered Versions and other technical work
produced by the Technical Committee (TC) are listed at
#link("https://groups.oasis-open.org/communities/tc-community-home2?CommunityKey=2c60b2cf-45d3-48cd-8594-0194f182b33d").

TC members should send comments on this document to the TC's email list.
Others should send comments to the TC's public comment list, after
subscribing to it by following the instructions at the "Send A Comment"
button on the TC's web page at
#link("https://www.oasis-open.org/committees/dps/").

NOTE: any machine-readable content (Computer Language Definitions)
declared Normative for this Work Product is provided in separate plain
text files. In the event of a discrepancy between any such plain text
file and display content in the Work Product's prose narrative
document(s), the content in the separate plain text file prevails.

#heading(level: 2, numbering: none)[A.2 License and Notices]
<license-and-notices>
Copyright © OASIS Open 2026. All Rights Reserved.

All capitalized terms in the following text have the meanings assigned
to them in the OASIS Intellectual Property Rights Policy (the "OASIS IPR
Policy"). The full Policy, which governs the licensure of this document,
may be found at the OASIS website:
\[#link("https://www.oasis-open.org/policies-guidelines/ipr/")\]

This document and translations of it may be copied and furnished to
others, and derivative works that comment on or otherwise explain it or
assist in its implementation may be prepared, copied, published, and
distributed, in whole or in part, without restriction of any kind,
provided that the above copyright notice and this section are included
on all such copies and derivative works. However, this document itself
may not be modified in any way, including by removing the copyright
notice or references to OASIS, except as needed for the purpose of
developing any document or deliverable produced by an OASIS Technical
Committee (in which case the rules applicable to copyrights, as set
forth in the OASIS IPR Policy, must be followed) or as required to
translate it into languages other than English.

The limited permissions granted above are perpetual and will not be
revoked by OASIS or its successors or assigns, as provided in the OASIS
IPR Policy.

This document is provided under the "Non-Assertion" IPR mode that was
chosen when the project was established, as defined in the IPR Policy.
For information on whether any patents have been disclosed that may be
essential to implementing this document, and any offers of patent
licensing terms, please refer to the Intellectual Property Rights
section of the project's web page
(#link("https://www.oasis-open.org/committees/dps/ipr.php")).

This document and the information contained herein is provided on an "AS
IS" basis and OASIS DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE
INFORMATION HEREIN WILL NOT INFRINGE ANY OWNERSHIP RIGHTS OR ANY IMPLIED
WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. OASIS
AND ITS MEMBERS WILL NOT BE LIABLE FOR ANY DIRECT, INDIRECT, SPECIAL OR
CONSEQUENTIAL DAMAGES ARISING OUT OF ANY USE OF THIS DOCUMENT OR ANY
PART THEREOF.

As stated in the OASIS IPR Policy, the following three paragraphs in
brackets apply to OASIS Standards Final Deliverable documents (Committee
Specifications, OASIS Standards, or Approved Errata).

OASIS requests that any OASIS Party or any other party that believes it
has patent claims that would necessarily be infringed by implementations
of this OASIS Standards Final Deliverable, to notify OASIS TC
Administrator and provide an indication of its willingness to grant
patent licenses to such patent claims in a manner consistent with the
IPR Mode of the OASIS Technical Committee that produced this
deliverable.

OASIS invites any party to contact the OASIS TC Administrator if it is
aware of a claim of ownership of any patent claims that would
necessarily be infringed by implementations of this OASIS Standards
Final Deliverable by a patent holder that is not willing to provide a
license to such patent claims in a manner consistent with the IPR Mode
of the OASIS Technical Committee that produced this OASIS Standards
Final Deliverable. OASIS may include such claims on its website, but
disclaims any obligation to do so.

OASIS takes no position regarding the validity or scope of any
intellectual property or other rights that might be claimed to pertain
to the implementation or use of the technology described in this OASIS
Standards Final Deliverable or the extent to which any license under
such rights might or might not be available; neither does it represent
that it has made any effort to identify any such rights. Information on
OASIS' procedures with respect to rights in any document or deliverable
produced by an OASIS Technical Committee can be found on the OASIS
website. Copies of claims of rights made available for publication and
any assurances of licenses to be made available, or the result of an
attempt made to obtain a general license or permission for the use of
such proprietary rights by implementers or users of this OASIS Standards
Final Deliverable, can be obtained from the OASIS TC Administrator.
OASIS makes no representation that any information or list of
intellectual property rights will at any time be complete, or that any
claims in such list are, in fact, Essential Claims.

The name "OASIS" is a trademark of OASIS, the owner and developer of
this document, and should be used only to refer to the organization and
its official outputs. OASIS welcomes reference to, and implementation
and use of, its documents, while reserving the right to enforce its
marks against misleading uses. Please see
#link("https://www.oasis-open.org/policies-guidelines/trademark/") for
guidance.

#pagebreak(weak: true)
#heading(level: 1, numbering: none)[Annex B. References]
<annex-b>
\(This annex forms an integral part of this Specification.)

This section contains the normative and informative references that are
used in this document.

Normative references are specific (identified by date of publication
and/or edition number or version number) and Informative references are
either specific or non-specific. For specific references, only the cited
version applies. For non-specific references, the latest version of the
reference document (including any amendments) applies. While any
hyperlinks included in this section were valid at the time of
publication, OASIS cannot guarantee their long term validity.

#heading(level: 2, numbering: none)[B.1 Normative References]
<normative-references>
The following documents are referenced in such a way that some or all of
their content constitutes requirements of this document.

#strong[\[]<RFC2119>#strong[RFC2119\]] #emph[Key Words for Use in RFCs
to Indicate Requirement Levels], BCP 14, RFC 2119, March 1997.
\[Online\]. Available: https:/\/www.rfc-editor.org/info/rfc2119

#strong[\[]<RFC8174>#strong[RFC8174\]] #emph[Ambiguity of Uppercase vs
Lowercase in RFC 2119 Key Words], BCP 14, RFC 8174, May 2017.
\[Online\]. Available: https:/\/www.rfc-editor.org/info/rfc8174

#strong[\[]<RFC8259>#strong[RFC8259\]] Bray, T., "The JavaScript Object
Notation (JSON) Data Interchange Format", RFC 8259, DOI
10.17487/RFC8259, December 2017,
#link("http://www.rfc-editor.org/info/rfc8259").

#heading(level: 2, numbering: none)[B.2 Informative References]
<informative-references>
The following referenced documents are not required for the application
of this document but may assist the reader with regard to a particular
subject area.

#strong[\[]<CNSSI-4009>#strong[CNSSI-4009\]] #emph[Committee on National
Security Systems (CNSS) Glossary], Committee on National Security
Systems, CNSSI No.~4009, April 6, 2015, Available:
https:/\/nsarchive.gwu.edu/document/22385-document-08-committee-national-security

#pagebreak(weak: true)
#heading(level: 1, numbering: none)[Annex C. Example Instances]
<annex-c>
\(This annex forms an integral part of this Specification.)

This annex provides three example instances of the Data Provenance
Metadata schema, each serving a distinct purpose in learning and
applying the standard.

The #strong[minimal example]
(#link(<minimal-example>)[C.1 "Minimal Example"]) contains only the
fields that are required by the schema, populated with the smallest
valid values. It is intended as a starting point for new implementers
and as a quick reference for the mandatory structure of a DP-Core set.

The #strong[moderate example]
(#link(<moderate-example>)[C.2 "Moderate Example"]) extends the minimal
case by adding a representative selection of optional fields at each
level. It is intended to illustrate common real-world usage --- a
dataset with multiple geographies, a revision history, licensing
information, and a confidentiality classification --- without attempting
to cover every possible field.

The #strong[complete example]
(#link(<complete-example>)[C.3 "Complete Example"]) is a comprehensive
instance that exercises every field defined in the schema at least once.
It is not intended to represent a typical implementation; its purpose is
to serve as a normative reference for tool developers verifying parser
completeness and for authors checking field semantics under realistic
conditions.

All three instances are available as JSON files in the `examples/`
directory of the specification distribution.

#heading(level: 2, numbering: none)[C.1 Minimal Example]
<minimal-example>
The following instance contains only the fields required by the schema.
The scenario is a single-issuer survey dataset with one generation
method and one intended purpose.

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

#heading(level: 2, numbering: none)[C.2 Moderate Example]
<moderate-example>
The moderate example extends the minimal case with a representative but
non-exhaustive selection of optional fields. The scenario is a
multilingual news corpus assembled from syndicated feeds and published
by a single commercial data provider.

Key features illustrated by this instance:

- #strong[Set level]: `language`, `acknowledgments`, and publisher
  `contact-details` are present. The tracking block includes two
  revision entries, reflecting a real update cycle.
- #strong[Source level]: `scope` is populated in `about`, limiting the
  stated purpose of the dataset. Two identification methods are used
  (`uuids` and `uris`). The issuer entry includes a postal `address` and
  a `url`.
- #strong[Provenance level]: Three `origin-geography` entries span
  multiple countries. `generation-method` carries a `long-description`
  explaining the feed mechanism. `format`, `generation-period`, and a
  lineage `source` URI are all present.
- #strong[Use level]: Two `intended-purpose` entries distinguish
  pre-training from academic research use. A single `classification`
  entry records evaluation against the Personal Information (PI)
  regulation. `consents` and `license` are populated.

The file `examples/dp-core-moderate.json` contains this instance.

#heading(level: 2, numbering: none)[C.3 Complete Example]
<complete-example>
The complete example is a comprehensive instance designed to exercise
every field in the schema. The scenario is a large merged biomedical
text corpus assembled by a research consortium from three distinct
sub-sources: PubMed abstracts, ClinicalTrials.gov result summaries, and
de-identified hospital discharge summaries.

Key features illustrated by this instance that are not present in the
moderate example:

- #strong[Set level]: All optional tracking fields are used, including
  `aliases` and `generator` (with engine name, version, and generation
  date). `source-language`, `notes`, and `references` are present. The
  `notes` array contains two entries --- a `legal_disclaimer` for the
  clinical content and a `summary` note describing what changed in
  version 3. The `references` array demonstrates both `external` and
  `self` category values.
- #strong[Source level]: All four `identity` methods are used: `uuids`,
  `uris`, `hashes` (with a SHA-256 tree hash), and `custom-ids` (a
  DataCite DOI with tool parameters). Two `issuer` entries reflect the
  dual institutional origin. `scope` in `about` explicitly excludes
  document types not covered.
- #strong[Provenance level]: Three `generation-method` entries with
  different codes cover the full collection pipeline. `format` lists
  three media types. `origin` names the upstream data providers.
  `previous-date` establishes continuity with the prior version.
  `sub-provenance` records the provenance of the initial PubMed-only
  sub-corpus from the v1 release.
- #strong[Use level]: Three `intended-purpose` entries (`pre-training`,
  `alignment`, `evaluation`). Three `classification` entries cover PHI,
  PI, and a free-text GDPR Article 9 entry using `code: other` with a
  `long-description`. Two `data-risk-reducing` entries document the
  NER-based redaction tool and the k-anonymity pipeline, each with
  `technology`, `parameters`, and `results`. All four geography
  restriction fields are populated (`processing-included`,
  `processing-excluded`, `storage-allowed`, `storage-forbidden`).
  `copyright`, `patent`, and `trademark` are present.

The file `examples/dp-core-complete.json` contains this instance.

#pagebreak(weak: true)
#heading(level: 1, numbering: none)[Appendix A. Acknowledgments]
<appendix-acknowledgments>
\(This appendix does not form an integral part of this Specification and
is informational.)

The following individuals were members of the OASIS DPS Technical
Committee during the creation of this specification and their
contributions are gratefully acknowledged:

#heading(level: 2, numbering: none)[Leadership]
<leadership>
The following individuals have had significant leadership positions
during the development of this document, not just this version of the
document, and they are gratefully acknowledged:

- Chairs
  - Lisa Bobbitt, Cisco, lbobbitt\@cisco.com
  - Bryan Bortnick, IBM, bortnick\@us.ibm.com
  - Fotis Psallidas, Microsoft, Fotis.Psallidas\@microsoft.com
- Secretaries
  - Jamie Yu, Cisco, jamyu2\@cisco.com
- Editors
  - David Kemp, NSA, d.kemp\@cyber.nsa.gov
  - Stefan Hagen, Individual, stefan\@hagen.link

#heading(level: 2, numbering: none)[Special Thanks]
<special-thanks>
The following individuals have made substantial contributions to this
document, not just this version of the document, and their contributions
are gratefully acknowledged:

The DPS TC thanks the following individuals for their assistance in the
development of this document: Kristina Podnar and the Data & Trust
Alliance for their contributions of the initial schema and example
applications. Duncan Sparrell for supporting the TC from the charter
definition to the initial structuring of this document.

#heading(level: 2, numbering: none)[Participants]
<participants>
The following individuals have participated in the creation of this
document and are gratefully acknowledged (given family, affiliation):

- David Kemp, NSA
- Duncan Sparrell, sFractal Consulting LLC
- Kristina Podnar, Data & Trust Alliance
- Lisa Bobbitt, Cisco
- Stefan Hagen, Individual

#pagebreak(weak: true)
#heading(level: 1, numbering: none)[Appendix B. Changes From Previous
Version]
<appendix-changes-from-previous-version>
\(This appendix does not form an integral part of this Specification and
is informational.)

This is the initial draft Committee Specification.

#heading(level: 2, numbering: none)[Revision History]
<revision-history>
Revision tracking is publicly available in the version control system at
#link("https://github.com/oasis-tcs/dps/commits/main").
