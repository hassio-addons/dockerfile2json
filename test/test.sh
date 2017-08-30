#!/usr/bin/env bash
# ==============================================================================
#
# Dockerfile2JSON
#
# Small script for testing the inner working of Dockerfile2JSON
#
# ==============================================================================
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
# ==============================================================================
set -o errexit  # Exit script when a command exits with non-zero status
set -o nounset  # Exit script on use of an undefined variable
set -o pipefail # Return exit status of the last command in the pipe that failed

RES=$(dockerfile2json ./test/Dockerfile)
TST=$(<./test/expected_result.txt)

if [[ "$RES" == "$TST" ]]; then
    echo "Expected result: OK"
else
    echo "Unexpected results!"
    echo "EXPECTED:"
    echo "-------------"
    echo "$TST"
    echo "-------------"
    echo "GOT:"
    echo "-------------"
    echo "$RES"    
    exit 1
fi