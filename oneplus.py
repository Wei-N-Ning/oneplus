"""

"""

import subprocess
import shlex
import sys
import textwrap


def fatal(msg: str, exitcode: int = 1) -> None:
    print(msg)
    sys.exit(exitcode)


def find_1password_cli() -> str:
    try:
        help_blob = subprocess.check_output(shlex.split('op --help')).decode().strip()
        for line in help_blob.split('\n'):
            if line.startswith('The 1Password command-line tool'):
                return 'op'
    except (subprocess.CalledProcessError, FileNotFoundError, PermissionError, Exception):
        pass
    fatal(textwrap.dedent('''
        Can not find 1password cli.
        Please follow this page to install it properly on your operating system:
        https://support.1password.com/command-line-getting-started/
        Then verify the installation by running:
        op --version
        op --help
    '''))


def signin(op_cli: str = 'op', flavor: str = 'default') -> None:
    pass


if __name__ == '__main__':
    op_cli = find_1password_cli()
    signin(op_cli)
