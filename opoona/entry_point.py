# -*- coding: utf-8 -*-

"""
Opoona, the thicket opener.

usage:
    opoona setup
    opoona <issue>

options:
    -h, --help  show this help message and exit
    --version   show this version and exit
"""

import sys

import docopt
import six

from .config import Config
from .opener import Opener

def main():
    args = docopt.docopt(__doc__, version='0.0.7')

    if args['setup']:
        try:
            Config.setup()
        except Exception as e:
            print(e)
            sys.exit(1)
        sys.exit(0)

    config = Config()
    try:
        config.load()
    except Exception as e:
        print(e)
        sys.exit(1)

    issue = six.u(args['<issue>'])
    if issue is not None:
        try:
            opoona = Opener(config)
            opoona.open(issue = issue)
        except Exception as e:
            print(e)
            sys.exit(1)

