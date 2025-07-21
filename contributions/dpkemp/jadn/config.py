import json
import os


def style_args(self, format: str, args: str, config: str = '') -> dict:
    """
    Combine style options from command line options, user defaults file, and format-defined defaults

    :param pkg: JADN schema package instance
    :param format: name of serialized (lexical) format
    :param args: arguments from command line in a double-quoted string
    :param config: name of JSON configuration file containing default arguments per format
    """

    def _fixbool(v: str) -> str | bool:
        return False if v.lower() == 'false' else True if v.lower() == 'true' else v

    format_opts = self.style()
    config_opts = {}
    if os.path.isfile(config):
        with open(config) as fp:
            config_opts = json.load(fp).get('style', {}).get(format, {})    # get args from "style" section
    assert not (x := set(config_opts) - set(format_opts)), f'Invalid style options {x} from {fp.name}'
    try:
        cli_opts = {(x := arg.split(':'))[0].strip(): _fixbool(x[1].strip()) for arg in args.split(',') if arg}
    except IndexError:
        err = f'Can\'t parse args "{args}"\n'
        err += f'Style options for "{format}" format:\n'
        err += f'  Class: {json.dumps(format_opts, indent=4)}\n'
        err += f'  Configuration file "{config}": {json.dumps(config_opts, indent=4)}' if config_opts else ''
        print(err)
        exit(-2)
    assert not (x := set(cli_opts) - set(format_opts)), f'Invalid style options {x}'
    return format_opts | config_opts | cli_opts


def style_fname(fname: str, format: str, style: dict) -> str:
    """
    Generate output filename based on style options for output format
    """
    if format == 'erd':
        fname += f'_{style["detail"][0]}{"a" if style["attributes"] else ""}'
        format = {'plantuml': 'puml', 'graphviz': 'dot'}[style['graph']]
    return f'{fname}.{format}'
