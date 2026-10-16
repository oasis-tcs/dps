## Note accompanying `kestrel-lineage-example.json`

This is a real, unmodified DPS record (two internal project/matter IDs in `source.about.content` redacted; nothing else changed), captured across three revisions of one document:

1. **Initial upload** — `tracking.version: 1`, `source.data-version: 1`.
2. **Post-ingest enrichment** — issuer and origin populated automatically from extracted document entities, no change to the underlying file. `tracking.version: 2`, `source.data-version` stays `1`.
3. **`/source replace`** — the file itself replaced. `tracking.version: 3`, `source.data-version: 2`.

`tracking.version` and `source.data-version` are deliberately independent counters: the former versions the *metadata record*, the latter versions the *artefact* the record describes. They move together only when a revision changes the file; a metadata-only revision (like step 2) advances `tracking.version` without advancing `data-version`. This record is a real example of that divergence, not an error — included here because it's a case worth the TC seeing, since nothing in the current spec text calls out that the two are expected to diverge under normal operation.
