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

"""Dockerfile2JSON

File containing the converter
"""

import dockerfile
import simplejson
import sys


class Converter(object):
    """Dockerfile2JSON

    This provides the actual converter
    It will in take the given Dockerfile (via STDIN) or path, and will
    output a JSON file.
    """

    def __init__(self, dockerfile_contents):
        """Class init."""
        self.dockerfile = dockerfile_contents

    def convert(self):
        """Parse the Dockerfile and output JSON to STDOUT."""
        parsed_dockerfile = dockerfile.parse_string(self.dockerfile)
        json = simplejson.dumps(parsed_dockerfile)
        print(json)
