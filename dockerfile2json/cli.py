
# -*- coding: utf-8 -*-
#
# MIT License
#
# Copyright (c) 2017 Franck Nijhof
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""CLI Handler for Dockerfile2JSON

This file handles the parsing of the CLI input
"""

import argparse
import os.path
import sys

from dockerfile2json import APP_DESCRIPTION, APP_NAME, APP_VERSION
from dockerfile2json.converter import Converter


def run(argv=None):
    """Run Dockerfile2JSON."""
    parser = argparse.ArgumentParser(
        prog=APP_NAME,
        description=APP_DESCRIPTION,
        epilog=("Example: cat ~/Dockerfile | "
                "docker-context-streamer . | docker build -")
    )
    parser.add_argument(
        'dockerfile',
        type=str,
        default='.',
        help='Dockerfile to convert to JSON'
    )
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%s %s' % (APP_NAME, APP_VERSION)
    )

    parsed = parser.parse_args()

    if not os.path.isfile(parsed.dockerfile) and parsed.dockerfile != '-':
        parser.error('Dockerfile is expected to be a plain file')

    if sys.stdin.isatty() and parsed.dockerfile == '-':
        parser.error("Missing Dockerfile on STDIN")

    if parsed.dockerfile == '-':
         dockerfile = sys.stdin.read()
    else:
        with open(parsed.dockerfile, 'r') as f:
            dockerfile = f.read()

    converter = Converter(dockerfile)
    converter.convert()
