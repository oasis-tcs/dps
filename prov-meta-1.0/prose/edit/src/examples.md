# Annex C Example Instances {#annex-c}

(This annex forms an integral part of this Specification.)

This annex provides four example instances of the Data Provenance Metadata schema,
each serving a distinct purpose in learning and applying the standard.

The **minimal example** ([sec](#minimal-example)) contains only the fields that are required by the schema,
populated with the smallest valid values.
It is intended as a starting point for new implementers and as a quick reference for
the mandatory structure of a DP-Core set.

The **moderate example** ([sec](#moderate-example)) extends the minimal case by adding a representative selection
of optional fields at each level.
It is intended to illustrate common real-world usage — a dataset with multiple geographies,
a revision history, licensing information, and a confidentiality classification — without
attempting to cover every possible field.

The **complete example** ([sec](#complete-example)) is a comprehensive instance that exercises every field
defined in the schema at least once.
It is not intended to represent a typical implementation; its purpose is to serve as a
normative reference for tool developers verifying parser completeness and for authors
checking field semantics under realistic conditions.

The **lineage example** ([sec](#lineage-example)) is a real record exported from a live implementation.
It shows how one record evolves over several revisions, and why the version of the metadata set
and the version of the dataset it describes are independent counters.

All four instances are available as JSON files in the `examples/` directory of the
specification distribution.

## C.1 Minimal Example {#minimal-example}

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

## C.2 Moderate Example {#moderate-example}

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

## C.3 Complete Example {#complete-example}

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

## C.4 Lineage Example {#lineage-example}

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
In this record they move together only when a revision changes the dataset;
revision 2 changes only the metadata and advances `set.tracking.version` alone.
Values that differ, as here (`3` and `2`), are permitted, not an error.

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
