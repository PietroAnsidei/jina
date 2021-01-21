from jina.parsers.helper import add_arg_group
from jina.enums import RemoteAccessType


def mixin_distributed_feature_parser(parser):
    """Mixing in arguments required by :class:`BasePod` into the given parser. """
    gp = add_arg_group(parser, title='Distributed')

    gp.add_argument('--remote-manager',
                    choices=list(RemoteAccessType),
                    default=RemoteAccessType.JINAD,
                    type=RemoteAccessType.from_string,
                    help=f'the manager of remote Jina')

    gp.add_argument('--silent-remote-logs', action='store_true', default=False,
                    help=f'do not display the streaming of remote logs on local console')

    gp.add_argument('--upload-files', type=str, nargs='*', metavar='FILE',
                    help='the files on the host to be uploaded to the remote workspace. This can be useful when your '
                         'Pod has more file dependencies beyond a single YAML file, e.g. Python files, data files. '
                         'Note (1) currently only flatten structure is supported, which means if you upload '
                         '`[./foo/a.py, ./foo/b.pp, ./bar/c.yml]`, then they will be put under the _same_ workspace on '
                         'the remote, losing all hierarchies. (2) By default, `--uses` YAML file is always uploaded. '
                         '(3) Uploaded files are by default isolated across the runs. To ensure files are submitted '
                         'to the same workspace across different runs, use `--workspace-id`.')

    gp.add_argument('--workspace-id', type=str,
                    help='the UUID for identifying the workspace on remote. When not given then remote will assign a '
                         'random one. Multiple Pea/Pod/Flow will work under the same workspace if they share the same '
                         '`workspace-id`.')
