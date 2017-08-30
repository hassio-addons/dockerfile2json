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

from setuptools import setup, find_packages

from dockerfile2json import (
    __author__, __email__, __license__, __url__, __download__,
    APP_NAME, APP_VERSION, APP_DESCRIPTION
)

setup(
    name=APP_NAME,
    version=APP_VERSION,
    author=__author__,
    author_email=__email__,
    description=APP_DESCRIPTION.split('\n')[0],
    long_description=APP_DESCRIPTION,
    license=__license__,
    url=__url__,
    download_url=__download__,
    keywords=['docker', 'dockerfile', 'json'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Build Tools',
        'Topic :: System',
        'Topic :: Utilities'
    ],
    packages=find_packages(),
    requires=["simplejson", "dockerfile"],
    install_requires=["simplejson>=3.11", "dockerfile>=1.0.0"],
    tests_require=['tox'],
    entry_points={'console_scripts': [
        'dockerfile2json=dockerfile2json.cli:run'
    ]}
)