# JADN CLI applications

## Convert Schemas

* Losslessly convert a JADN schema to the same schema in an equivalent data format.
* Translate a JADN schema to/from a different abstract or concrete schema language.
* Transform a JADN schema to a different JADN schema for reasons such as
simplifying shortcuts into core definitions or resolving external references
between schema packages.

Formats and operations are defined in the [JADN software package](jadn).

**Usage:**
```
usage: jadn-convert.py [-h] [-f format] [-r] [--style STYLE]
                       schema [output_dir]

Convert JADN schemas to a specified format.

positional arguments:
  schema
  output_dir

options:
  -h, --help     show this help message and exit
  -f format      output format (default: jadn)
  -r             recursive directory search (default: False)
  --style STYLE  serialization style options (default: )
```
Examples:
* `jadn-convert.py -f erd --style "detail: information, attributes: True" jadn/data/jadn_v2.0_schema.jadn Out`
* `jadn-convert.py -f atree --style "detail:logical" jadn/data/jadn_v2.0_schema.jadn`

If output_dir is not specified, output goes to stdout.

Read a JADN `schema` package in the format indicated by its file extension (`.jadn`), convert it to the `erd`
(entity relationship diagram) format, overriding the default style options `detail` and `attributes`.

CLI style options are key:value pairs separated by commas and must be enclosed in double quotes.
Specifying invalid style options (e.g., `--style ?`) will print out all options applicable to the
`format` including default values from the format definition and the user's configuration file.

Example user-defined configuration file `jadn_config.json`:
```json
{
  "style": {
    "jidl": {
      "name": 20,
      "desc": 55
    },
    "erd": {
      "graph": "graphviz"
    }
  }
}
```
The top level of the configuration file is a section.
Under the style section are output formats and the option values specified for each format.
Only the style section is defined at this time, but additional sections may added later.

This example sets column widths for JIDL output and the graph format for ERDs. The data format class file
defines all possible options and their default values.  The configuration file overrides some of those
values, and the CLI `--style` argument supersedes both.

## Serialize and Validate Data
tbsl