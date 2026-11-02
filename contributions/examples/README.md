# Contributions - Examples

In this folder we store incoming examples for data provenance information items from the community and
regardless of the governing schema.

The intent is to maximize relevance through considering real-world data sets.

# DPS 1.0 examples

Real, sanitized DPS records exported from a live implementation (mnēSara), contributed at the request of the TC (Group C/D call, 2026-10-16) for examples drawn from actual system output rather than built by hand from the spec. Two internal identifiers (project and matter IDs) in `source.about.content` are redacted. Nothing else is changed.

## Files

- **`kestrel-lineage-example.json`**: the raw DPS record. One document, `kestrel-northfield-q3-2026-compliance.pdf`, across three revisions.
- **`kestrel-lineage-example-note.md`**: the three-revision history, and why `tracking.version` and `source.data-version` diverge.

## What the record shows

The three revisions happened within about four minutes of each other (see `set.tracking.revision-history`):

| # | What happened | `tracking.version` | `source.data-version` |
|---|---------------|--------------------|-----------------------|
| 1 | Initial upload | 1 | 1 |
| 2 | Automatic enrichment: issuer and origin extracted from the document. File untouched. | 2 | 1 |
| 3 | File replaced with an updated version | 3 | 2 |

The record is the state after revision 3. Things worth looking at:

- **Lineage.** `provenance.source` points to the prior record and `provenance.source-digest` carries its sha256. That is how a revision chain is expressed today. `previous-date` gives the date of the record it replaces.
- **Artefact integrity.** `source.id.hashes[].tree-hashes[]` holds the sha256 of the current file.
- **Two version counters.** `tracking.version` counts revisions of the metadata record. `source.data-version` counts revisions of the file. They agree only when a revision changes the file. Revision 2 above is a metadata-only change, so they differ. The spec text does not currently say this is expected; it is raised for CSD02.
- **Latest revision.** `tracking.version` equals `number` in the most recent `revision-history` item (the rule added by PR #210).
- **Local vocabularies.** `use.intended-purpose` and `provenance.generation-method` use `code` and `system` with a publisher-defined vocabulary URI. This is how an implementation carries terms the spec does not define.

## Using this today

Read the JSON first, then the note. For field definitions, the authority is `prov-meta-1.0/prose/` and the JADN in `prov-meta-1.0/jadn/`, not this folder. These examples illustrate the spec. They do not extend or interpret it.

What this record does not demonstrate:

- No `proof` member. Signing is not exercised here.
- No handling, custody or transmission information.
- A single artefact. Set-level records covering many files are not shown.
- One implementation. Another producer may make different, equally valid choices (vocabulary URIs, how `source` is expressed, whether it emits metadata-only revisions at all).

Treat the divergence of the two counters as one implementation's behaviour, and not as a requirement. If your implementation increments both together, that is consistent with the current text.

## Note

`prov-meta-1.0/examples/` is a separate folder in this repo and holds `dp-core-minimal.json`, `dp-core-moderate.json` and `dp-core-complete.json`. Those predate this contribution and may be stale against the current schema. They are listed here only so readers know both sets exist. Reconciling them is for the TC.
