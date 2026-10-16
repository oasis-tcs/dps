---
# Contributions - Examples

In this folder we store incoming examples for data provenance information items from the community and
regardless of the governing schema.

The intent is to maximize relevance through considering real-world data sets.


# DPS 1.0 examples

Real, sanitized DPS records exported from a live implementation (mnēSara), per Stefan's request on the 2026-10-16 Group C/D call for examples drawn from actual system output rather than hand-built from the spec. Two internal identifiers (project/matter IDs) in `about.content` are redacted; everything else is unmodified real output.

## Files

- **`kestrel-lineage-example.json`** — the raw DPS record. One document (`kestrel-northfield-q3-2026-compliance.pdf`) across three real revisions: initial upload, an automated metadata-only enrichment (issuer/origin extracted from the document), and a full file replace. Demonstrates `source-digest`-backed lineage via `provenance.source` + `previous-date`, and a real case where `tracking.version` and `source.data-version` legitimately diverge.
- **`kestrel-lineage-example-note.md`** — short explanation of the three-revision history and why `tracking.version` and `source.data-version` diverge.

## Note

`prov-meta-1.0/examples/` (a separate folder in this repo) already contains `dp-core-minimal.json`, `dp-core-moderate.json`, and `dp-core-complete.json` from Stefan, dated three months prior to this request. Worth reconciling with those rather than treating this folder as the sole example set — flagged to Stefan directly.
