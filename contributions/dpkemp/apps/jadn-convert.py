import argparse
import sys
import os
from jadn.config import style_args, style_fname
from jadn.convert import JADN, JIDL, XASD, MD, ATREE, ERD
from jadn.translate import JSCHEMA, XSD, CDDL, PROTO, XETO

CONFIG = 'jadn_config.json'


def convert_file(format: str, style_cmd: str, path: str, infile: str, outdir: str) -> None:
    klass = {
        'jadn': JADN,
        'jidl': JIDL,
        'xasd': XASD,
        'md': MD,
        'erd': ERD,
        'atree': ATREE,
        'json': JSCHEMA,
        'xsd': XSD,
        'cddl': CDDL,
        'proto': PROTO,
        'xeto': XETO,
    }

    if outdir:
        print(infile)  # Don't print if destination is stdout

    fn, ext = os.path.splitext(infile)
    ext = ext.lstrip('.')
    if (k := klass.get(ext)) and k.schema_loads != k.__bases__[0].schema_loads: # input format has a read method

        # Read schema literal into information value
        pkg = k()
        with open(os.path.join(path, infile), 'r') as fp:
            pkg.schema_load(fp)

        # Validate JADN information value against JADN metaschema
        pkg.validate()

        # Serialize information value to schema literal in output format
        if format in klass:
            style = style_args(klass[format](), format, style_cmd, CONFIG)    # style from format, config, args
            if outdir:
                with open(os.path.join(outdir, style_fname(fn, format, style)), 'w', encoding='utf8') as fp:
                    klass[format]().schema_dump(fp, pkg, style)
            else:
                klass[format]().schema_dump(sys.stdout, pkg, style)
        else:
            print(f'Unknown output format "{format}"')
            sys.exit(2)
    else:
        print(f'Unknown input format "{ext}" -- ignored')


def main(input: str, output_dir: str, format: str, style: str, recursive: bool) -> None:
    """
    Convert JADN schema among multiple formats

    Convert to or from equivalent formats
    Convert to presentation formats
    Translate JADN abstract schema to or from concrete schema languages
    """

    # print(f'Installed JADN version: {jadn.__version__}\n')

    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    if os.path.isdir(input):
        # If input is directory, process all files, including contained directories if recursive=True
        for path, dirs, files in os.walk(input):
            if not recursive:
                dirs.clear()
            for file in files:
                convert_file(format, style, path, file, output_dir)
    else:
        # Otherwise process the named input file
        path, file = os.path.split(input)
        try:
            convert_file(format, style, path, file, output_dir)
        except (FileNotFoundError, AssertionError) as e:
            print(e, file=sys.stderr)
            sys.exit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Convert JADN schemas to a specified format.')
    parser.add_argument('-f', metavar='format', default='jadn',
                        help='output format')
    parser.add_argument('-r', action='store_true', help='recursive directory search')
    parser.add_argument('--style', default='', help='serialization style options')
    parser.add_argument('schema')
    parser.add_argument('output_dir', nargs='?', default=None)
    args = parser.parse_args()
    if args.output_dir:
        print(args)     # Don't print info if output on stdout
    main(args.schema, args.output_dir, args.f, args.style, args.r)
