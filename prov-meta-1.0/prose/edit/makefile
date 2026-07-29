.POSIX:
.SILENT:
.DEFAULT_GOAL = build

pyversion = py311
linelength = 120
black = black -S -l $(linelength) --target-version $(pyversion) --quiet bin
lint = ruff check bin
types = mypy bin
build_root = build/
OPEN ?= open

target_gfm_plus = gfm-plus

shared = ../share/
artifact_stem = prov-meta-v1.0-draft

out_gfm_plus      = $(shared)$(artifact_stem).md
out_html          = $(shared)$(artifact_stem).html
out_ir            = $(shared)$(artifact_stem).ir.json
out_manifest      = $(shared)$(artifact_stem).manifest.json
out_pdf           = $(shared)$(artifact_stem).pdf
out_pdf_sha256    = $(shared)$(artifact_stem).pdf.sha256
out_pdf_blake3    = $(shared)$(artifact_stem).pdf.blake3
out_typst         = $(shared)$(artifact_stem).typ

.PHONY: all
all: lint types build

.PHONY: format
format:
	command -v ruff >/dev/null 2>&1 || { echo >&2 "make format requires ruff but it's not installed - you can install with: 'pip install ruff'.  Aborting."; exit 1; }
	$(lint) --fix
	command -v black >/dev/null 2>&1 || { echo >&2 "make format requires black but it's not installed - you can install with: 'pip install black'.  Aborting."; exit 1; }
	$(black)

.PHONY: lint
lint:
	$(lint) --diff
	$(black) --check --diff
	command -v unmake >/dev/null 2>&1 || { echo >&2 "make lint requires unmake but it's not installed - you can install with: 'cargo install unmake'.  Aborting."; exit 1; }
	unmake makefile

.PHONY: types
types:
	command -v mypy >/dev/null 2>&1 || { echo >&2 "make types requires mypy but it's not installed - you can install with: 'pip install mypy'.  Aborting."; exit 1; }
	$(types)

.PHONY: render
render: html

.PHONY: sections
sections:
	nide harvest

.PHONY: gfm-plus
gfm-plus: sections
	nide assemble && \
	  cp -p build/ir.json $(out_ir) && \
	  nide render -t $(target_gfm_plus) && \
	  cp -p build/gfm-plus.md $(out_gfm_plus) && \
	  printf "Rendered user facing delivery item in markdown format:\n" && \
	  ls -l $(out_gfm_plus) $(out_ir)

.PHONY: html
html: gfm-plus
	command -v pandoc >/dev/null 2>&1 || { echo >&2 "make html requires pandoc but it's not installed - you can get help on installing at https://pandoc.org.  Aborting."; exit 1; }
	# mkdir -p build/data-url/ && cd src/images && for source in image*.png; do printf "%s" "data:image/png;base64,$$(cat "$${source}" | base64 | tr -d '\r\n')" > "../../build/data-url/$${source}.txt"; done && cd -
	nide render -t html && \
	  pandoc -f gfm+definition_lists -t html build/html.md --columns=345 \
	  --css style/base.css --css style/skin.css --standalone -o build/pandoc.html && \
	  nide inject && \
	  cp -p build/injected.html $(out_html) && \
	  printf "Rendered user facing delivery item in html format:\n" && \
	  ls -l $(out_html)

.PHONY: pdf
pdf:
	command -v pandoc >/dev/null 2>&1 || { echo >&2 "make pdf requires pandoc but it's not installed - you can get help on installing at https://pandoc.org.  Aborting."; exit 1; }
	command -v typst >/dev/null 2>&1 || { echo >&2 "make pdf requires typst but it's not installed - you can get help on installing at https://typst.app.  Aborting."; exit 1; }
	nide assemble
	nide render -t typst
	mkdir -p build/images
	cp -p ../media/OASISLogo-v3.0.png build/images/
	cp -p src/images/*.png src/images/*.svg build/images/
	pandoc -f markdown+definition_lists -t typst --standalone --template etc/dps.typ --lua-filter build/nide-columns.lua build/typst.md -o build/typst.typ
	typst compile --root . build/typst.typ build/prov-meta-typst.pdf
	cp -p build/prov-meta-typst.pdf $(out_pdf)
	cp -p build/typst.typ $(out_typst)
	shasum -a 256 $(out_pdf) > $(out_pdf_sha256)
	{ command -v b3sum >/dev/null 2>&1 && b3sum $(out_pdf) > $(out_pdf_blake3); } || \
	  { [ -f $(out_pdf_blake3) ] && printf "WARNING: b3sum not installed — $(out_pdf_blake3) is stale.\n" || true; }
	$(OPEN) $(out_pdf)

.PHONY: release
release: html pdf
	nide manifest
	nide validate
	printf "Release complete. Manifest verified.\n"
	cp -p build/manifest.json $(out_manifest)
	ls -l $(shared)$(artifact_stem).*

.PHONY: build
build: render status

.PHONY: quality
quality:
	nide quality

.PHONY: validate
validate:
	nide validate

.PHONY: diff
diff:
	nide diff --mode prose $(out_html) || true

.PHONY: diff-repro
diff-repro:
	nide diff --mode repro $(out_pdf) || true

.PHONY: status
status:
	printf "Current version control status:\n"; \
	git status || true

.PHONY: diff-pdf
diff-pdf:
	printf "Current PDF version control diff:\n"; \
	command -v iconv >/dev/null 2>&1 || { echo >&2 "make diff-pdf requires iconv but it's not installed - you can search the internets on how to install iconf.  Aborting."; exit 1; }
	git diff -a $(out_pdf) | iconv --from-code=UTF-8 -c

.PHONY: clean
clean:
	rm -f build/*.md build/*.html build/*.json build/*.lua build/*.typ \
	  build/prov-meta-typst.pdf
	rm -fr build/images/ build/data-url/ build/render/

.PHONY: distclean
distclean: clean
	rm -fr $(build_root)

.PHONY: context
context:
	printf "Clone-info:\n"
	printf "%s name.is(): '%s'\n" "-" "$$(basename `git rev-parse --show-toplevel`)"
	printf "%s branch.is(): '%s'\n" "-" "$$(git branch --show-current)"
	printf "%s revision.is(): sha1:%s\n" "-" "$$(git rev-parse HEAD)"
	printf "%s location.is(): %s\n" "-" "$$(python -c "(lambda _Y: (lambda _mod: (lambda Path: (lambda g: [(lambda x: [(lambda c, p: (lambda _loop1: _loop1(c, p))(_Y(lambda _loop1: (lambda c, p: ([_loop1(c, p) for (p, c) in [x(p, c, g)]][0]) if (c != p) and (str(c) != '/') else print((f\"(orga/repo='{c.parent.name}/{c.name}', rel-path='{o.relative_to(c)}')\" if (c == p) else \"(orga/repo='?/?', rel-path='?')\"))))))(c if 'c' in dir() else None, p if 'p' in dir() else None) for (_, c) in [x(p, c, g)]][0])(lambda p, c, g: (c, c.parent if not (c / g).is_dir() else c)) for o, p, c in [[Path().resolve()] * 3]][0])('.git'))(_mod.Path))(__import__('pathlib', {}, {}, ['Path'])))((lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args)))))")"
	printf "%s node.id(): '%s'\n" "-" "$$(python -c 'import platform; import uuid; print(str(uuid.uuid3(uuid.NAMESPACE_DNS, platform.node())))')"

PHONY: name  # Deprecated - backwards compatibility target
name: context

.PHONY: whoami  # Deprecated - backwards compatibility target
whoami: context

.PHONY: typst  # Deprecated - use pdf
typst: pdf

.PHONY: diff-pdf  # Deprecated - use diff-repro
diff-pdf: diff-repro

.PHONY: render-html  # Deprecated - backwards compatibility target
render-html: html

.PHONY: render-markdown  # Deprecated - backwards compatibility target
render-markdown: gfm-plus

.PHONY: render-pdf  # Deprecated - backwards compatibility target
render-pdf: pdf
