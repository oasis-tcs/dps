# DPS prov-meta-1.0 Prose

This folder holds the editorial sources and versioned delivery items for the
DPS Data Provenance Metadata Version 1.0 specification.

| Subfolder | Purpose                                                                               |
|:----------|:--------------------------------------------------------------------------------------|
| `edit/`   | Authoring workspace — sources, configuration, and build tooling; see `edit/README.md` |
| `share/`  | Versioned delivery items built from `edit/`; see `share/README.md`                    |

## Delivery formats

We build four delivery channels from the same source:

- **GFM+** (`prov-meta-v1.0-draft.md`) — optimised for reading on version-control web interfaces
  (Codeberg, GitHub, GitLab, SourceHut, …)
- **HTML** (`prov-meta-v1.0-draft.html`) — standalone file for any browser,
  with images inlined as data URLs
- **PDF** (`prov-meta-v1.0-draft.pdf`) — compiled via typst
- **IR** (`prov-meta-v1.0-draft.ir.json`) — nide's channel-neutral internal representation;
  useful for tooling and diffing

To build all channels and verify the manifest, run from `edit/`:

    make release

To build incrementally:

    make gfm-plus   # GFM+ and IR
    make html       # HTML (implies gfm-plus)
    make pdf        # PDF + typst source + checksums

To check document completeness against the editorial rules:

    make quality    # per-rule PASS/FAIL/NA report (reads etc/rules/spec.rules.yaml)

Execution of any target that uses non-standard tools will verify the tools are available.
If an essential tool is missing, make aborts with a message describing what is needed and how to install it.
