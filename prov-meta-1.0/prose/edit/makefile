.POSIX:
.SILENT:
.DEFAULT_GOAL = build

pyversion = py311
linelength = 120
black = black -S -l $(linelength) --target-version $(pyversion) --quiet bin
lint = ruff check bin
types = mypy bin
build_root = build/
build_pdf = $(build_root)render/pdf/
liitos_templates = etc/liitos/
optimize_pdf = qpdf --linearize --replace-input

target_gfm_plus = gfm-plus
target_html = html
target_pdf = pdf

out_html = ../share/prov-meta-v1.0-draft.html
out_gfm_plus = ../share/prov-meta-v1.0-draft.md
out_pdf = ../share/prov-meta-v1.0-draft.pdf

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
	-unmake makefile

.PHONY: types
types:
	command -v mypy >/dev/null 2>&1 || { echo >&2 "make types requires mypy but it's not installed - you can install with: 'pip install mypy'.  Aborting."; exit 1; }
	$(types)

.PHONY: sections
sections:
	koota harvest

.PHONY: render
render: render-html

.PHONY: render-markdown
render-markdown: sections
	koota assemble -t $(target_gfm_plus) && \
	  cp -a build/tmp.md $(out_gfm_plus) && \
	  printf "Rendered user facing delivery item in markdown format:\n" && \
	  ls -l $(out_gfm_plus)

.PHONY: render-html
render-html: render-markdown
	mkdir -p build/data-url/ && cd src/images && for source in image*.png; do printf "%s" "data:image/png;base64,$$(cat "$${source}" | base64 | tr -d '\r\n')" > "../../build/data-url/$${source}.txt"; done && cd -
	command -v pandoc >/dev/null 2>&1 || { echo >&2 "make render-html requires pandoc but it's not installed - you can get help on installing at https://pandoc.org.  Aborting."; exit 1; }
	command -v tidy >/dev/null 2>&1 || { echo >&2 "make render-html requires tidy but it's not installed - you can get help on installing by searching for it on the wild internets.  Aborting."; exit 1; }
	koota assemble -t $(target_html) && \
	  pandoc -f gfm+definition_lists -t html build/tmp.md --columns=345 \
	  --css style/base.css --css style/skin.css --standalone -o build/tmp.html && \
	  koota inject && \
	  timeout 2 tidy -config etc/tidy-config.txt build/injected.html -ashtml 2>/dev/null | \
	  sed 's/<!\[CDATA\[//g; s/\]\]>//g;' > $(out_html) && \
	  printf "Rendered user facing delivery item in html format:\n" && \
	  ls -l $(out_html)

.PHONY: render-pdf
render-pdf: sections
	command -v liitos >/dev/null 2>&1 || { echo >&2 "make render-pdf requires liitos but it's not installed - you can install per pip install liitos.  Aborting."; exit 1; }
	command -v etiketti >/dev/null 2>&1 || { echo >&2 "make render-pdf requires etiketti but it's not installed - you can install per pip install etiketti.  Aborting."; exit 1; }
	command -v qpdf >/dev/null 2>&1 || { echo >&2 "make render-pdf requires qpdf but it's not installed - you can search the internets on how to install qpdf.  Aborting."; exit 1; }
	koota assemble -t $(target_pdf) && \
	  mkdir -p $(build_pdf)images/ $(build_root)images/ && \
	  printf "pdf.md\n" > $(build_root)bind.txt && \
	  cp -a ../media/OASISLogo-v3.0.png $(build_root)images/ && \
	  cp -a src/images/*.png $(build_root)images/ && \
	  cp -a ../media/OASISLogo-v3.0.png $(build_pdf)images/ && \
	  cp -a $(liitos_templates)approvals.yml $(build_root) && \
	  cp -a $(liitos_templates)bookmatter.tex.in $(build_root) && \
	  cp -a $(liitos_templates)changes.yml $(build_root) && \
	  cp -a $(liitos_templates)driver.tex.in $(build_pdf) && \
	  cp -a $(liitos_templates)meta.yml $(build_root) && \
	  cp -a $(liitos_templates)metadata.tex.in $(build_pdf) && \
	  cp -a $(liitos_templates)patch.yml $(build_root) && \
	  cp -a $(liitos_templates)publisher.tex.in $(build_root) && \
	  cp -a $(liitos_templates)setup.tex.in $(build_pdf) && \
	  cp -a $(liitos_templates)structure.yml $(build_root) && \
	  cp -a etc/etiketti/etiketti.yml $(build_pdf) && \
	  cd $(build_pdf) && \
	  max_print_line=10000 liitos render ../../ --target prov-meta --facet pdf --patch-tables --filters ' ' --label "etiketti --config etiketti.yml --enforce"  && \
	  $(optimize_pdf) -- this.pdf && \
	  cp -a this.pdf ../../../$(out_pdf) && \
	  open ../../../$(out_pdf)

.PHONY: build
build: render status

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
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -rf .cache .*_cache
	rm -f .DS_Store
	rm -fr $(build_root)
	mkdir -p $(build_root)

.PHONY: distclean
distclean: clean
	rm -fr $(build_root)

.PHONY: context
context:
	printf "Context:\n"
	printf "%s configuration.control.by(): '%s'\n" "-" "$$({ fossil status --brief > /dev/null 2>&1 && printf "fossil"; } || printf 'n/a')"
	printf "%s name.is(): '%s'\n" "-" "$$({ fossil info > /dev/null 2>&1 && fossil info | head -1 | cut -f2 -d' '; } || printf 'n/a')"
	printf "%s branch.is(): '%s'\n" "-" "$$({ fossil branch > /dev/null 2>&1 && fossil branch | cut -f3 -d' '; } || printf 'n/a')"
	printf "%s status.is(): '%s'\n" "-" "$$({ fossil status > /dev/null 2>&1 && fossil status --brief; } || printf 'n/a')"
	printf "%s revision.is(): 'sha256:%s'\n" "-" "$$({ fossil describe > /dev/null 2>&1 && fossil describe --digits 64; } || printf 'n/a')"
	printf "%s location.is(): %s\n" "-" "$$(python -c "(lambda _Y: (lambda _mod: (lambda Path: (lambda g: [(lambda x: [(lambda c, p: (lambda _loop1: _loop1(c, p))(_Y(lambda _loop1: (lambda c, p: ([_loop1(c, p) for (p, c) in [x(p, c, g)]][0]) if (c != p) and (str(c) != '/') else print((f\"(orga/repo='{c.parent.name}/{c.name}', rel-path='{o.relative_to(c)}')\" if (c == p) else \"(orga/repo='?/?', rel-path='?')\"))))))(c if 'c' in dir() else None, p if 'p' in dir() else None) for (_, c) in [x(p, c, g)]][0])(lambda p, c, g: (c, c.parent if not (c / g).is_file() else c)) for o, p, c in [[Path().resolve()] * 3]][0])('.fslckout'))(_mod.Path))(__import__('pathlib', {}, {}, ['Path'])))((lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args)))))")"
	printf "%s tools.info(): (fossil|git='%s'|'%s', pip='%s', python='%s', cmake='%s', npm='%s', bun|deno|node='%s'|'%s'|'%s')\n" "-" \
		"$$({ command -v fossil > /dev/null 2>&1 && fossil version | cut -f5 -d' '; } || printf 'n/a')" \
		"$$({ command -v git > /dev/null 2>&1 && git --version | cut -f3 -d' '; } || printf 'n/a')" \
		"$$({ command -v python -m pip > /dev/null 2>&1 && python -m pip --version | cut -f2 -d' '; } || printf 'n/a')" \
		"$$({ command -v python > /dev/null 2>&1 && python -V | cut -f2 -d' '; } || printf 'n/a')" \
		"$$({ command -v cmake > /dev/null 2>&1 && cmake --version | head -1 | cut -f3 -d' '; } || printf 'n/a')" \
		"$$({ command -v npm > /dev/null 2>&1 && npm --version; } || printf 'n/a')" \
		"$$({ command -v bun > /dev/null 2>&1 && bun --version | tr -d 'v'; } || printf 'n/a')" \
		"$$({ command -v deno > /dev/null 2>&1 && deno --version | grep -i deno | cut -f2 -d' '; } || printf 'n/a')" \
		"$$({ command -v node > /dev/null 2>&1 && node --version | tr -d 'v'; } || printf 'n/a')"
	printf "%s node.info(): (id='%s', disk.free.megabytes()=%s, cpu.core.count()=%s, os='%s', shell='%s:%s', make='%s')\n" "-" \
		"$$(python -c 'import platform; import uuid; print(str(uuid.uuid3(uuid.NAMESPACE_DNS, platform.node())).replace("-",""))')" \
		"$$(python -c 'import shutil; f=shutil.disk_usage(".").free; print(round(f / (2 << 19), 3))')" \
		"$$(python -c 'import os; c=os.cpu_count() or "'n/a'"; print(c)')" \
		"$$({ command -v os > /dev/null 2>&1 && os; } || printf 'n/a')" \
		"$$(basename $(SHELL))" \
		"$$({ $(SHELL) --version > /dev/null 2>&1 && $(SHELL) --version | head -1 | grep -i version | tr -d "a-zA-Z ," | cut -f1-3 -d. | tr '(' '\n' | head -1; } || printf 'n/a')" \
		"$$(make --version | grep -i make)"


.PHONY: name
name: context

.PHONY: whoami
whoami: context
