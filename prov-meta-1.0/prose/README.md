# DPS prov-meta-1.0 Prose

This folder holds the editorial sources and versioned delivery items for the
DPS Data Provenance Metadata Version 1.0 specification.

| Subfolder | Purpose                                                                               |
|:----------|:--------------------------------------------------------------------------------------|
| `edit/`   | Authoring workspace — sources, configuration, and build tooling; see `edit/README.md` |
| `share/`  | Versioned delivery items built from `edit/`; see `share/README.md`                    |
| `media/`  | Shared media for the build, such as the OASIS logo; see `media/README.md`             |

## Where the model lives

The JSON schema `../json/data-provenance.json` is the single normative definition of the format and the only
source of the model. The prose shows the model through views generated from it by `make derive` in `edit/`:

| View                                | Generated from     | Where                                                       |
|:------------------------------------|:-------------------|:------------------------------------------------------------|
| JADN encoding                       | JSON schema        | `../jadn/data-provenance.jadn`                              |
| YAML serialization                  | JSON schema        | `../yaml/data-provenance.yaml`                              |
| YAML outlines of the member sections | JSON schema       | `edit/src/data-model-*.md` (section Provenance Data Model Encoding) |
| Property tables                     | JADN encoding      | `edit/src/schema-*.md` (section Provenance Schema)          |
| Overview figure                     | JSON schema        | `edit/src/images/metadata.{dot,svg}`                        |

The example instances of Annex C are in `../examples/`; each one validates against the JSON schema.
To change the model, edit the JSON schema, never a view; `edit/README.md` describes the generators and their rules.

## Delivery formats

We build four delivery channels from the same source:

- **GFM+** (`prov-meta-v1.0-draft.md`) — optimised for reading on version-control web interfaces
  (Codeberg, GitHub, GitLab, SourceHut, …)
- **HTML** (`prov-meta-v1.0-draft.html`) — standalone file for any browser,
  with images inlined as data URLs
- **PDF** (`prov-meta-v1.0-draft.pdf`) — compiled via typst; with its typst source (`.typ`) and checksums (`.sha256`, `.blake3`)
- **IR** (`prov-meta-v1.0-draft.ir.json`) — nide's channel-neutral internal representation;
  useful for tooling and diffing

`make release` also writes the manifest (`prov-meta-v1.0-draft.manifest.json`) over all of them and verifies it.

To build what you hand over (a PR or a release) from scratch, with every gate, run from `edit/`:

    make release

To build incrementally:

    make gfm-plus   # GFM+ and IR
    make html       # HTML (implies gfm-plus)
    make pdf        # PDF + typst source + checksums
    make render     # HTML and PDF together, no cleaning, no gates

After a change of the JSON schema, regenerate the views first:

    make derive     # JADN, property tables, outlines, figure, YAML serialization

To check document completeness against the editorial rules:

    make quality    # drift check of all generated views, then per-rule PASS/FAIL/NA report (etc/rules/spec.rules.yaml)

Execution of any target that uses non-standard tools will verify the tools are available.
If an essential tool is missing, make aborts with a message describing what is needed and how to install it.
