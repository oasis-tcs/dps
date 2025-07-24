# Explorations of a Data Provenance Schema

This contribution licensed under MIT explores a possible schema evolution of the
contributed JSON Schema from the Data and trust Alliance.

The main goals are:

1. Do not fight the schema language (use $defs etc.)
2. Tighten value types
3. Move the keys closer to English language
4. Amend with versioning and selective strictness (prefix marked extensions)

Work in progress ...

## Transforms Tool

We can use the `muuntuu` transforms tool to map between JSON and YAML,
as well as ensure an opinionated file structure of these formats is given locally.

To install the `muuntuu` tool into your local python environment:

```bash
❯ python -m pip install --upgrade muuntuu
```

### Usage

```bash
❯ muuntuu
usage: muuntuu [-h] [--source FILE] [--target FILE] [--debug] [--quiet] [--version] [SOURCE_FILE] [TARGET_FILE]

Transforms (Finnish: muuntuu) helper tool.

positional arguments:
  SOURCE_FILE           JSON or YAML source as positional argument
  TARGET_FILE           JSON or YAML target as positional argument

options:
  -h, --help            show this help message and exit
  --source FILE, -s FILE
                        JSON or YAML source
  --target FILE, -t FILE
                        JSON or YAML target
  --debug, -d           work in debug mode (default: False), overwrites any environment variable TRANSFORMS_DEBUG value
  --quiet, -q           work in quiet mode (default: False)
  --version, -V         display version and exit
```
