# Dockerfile2JSON

![Project Stage][project-stage-shield]
![Maintenance][maintenance-shield]
![Awesome][awesome-shield]
[![License][license-shield]](LICENSE.md)

This little tool allows you convert any Dockerfile to JSON, using the actual
Dockerfile parser from Docker.

## Examples

```bash
$ export DOCKERFILE="FROM alpine"
$ echo $DOCKERFILE | dockerfile2json -
```

```bash
$ dockerfile2json ./Dockerfile
```

## Installation

Using pip, the Python package manager:

```bash
pip install dockerfile2json
```

## Contributing

This is an active open-source project. We are always open to people who want to
use the code or contribute to it.

We've set up a separate document for our [contribution guidelines](CONTRIBUTING.md).

Thank you for being involved! :heart_eyes:

## Authors & contributors

The original setup of this repository is by [Franck Nijhof][frenck].

For a full list of all authors and contributors,
check [the contributor's page][contributors].

## Credits

A big shout out to [Anthony Sottile][asottile] for creating
the [dockerfile library][dockerfile], which this project uses.

Thank you!

## License

MIT License

Copyright (c) 2017 Franck Nijhof

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[awesome-shield]: https://img.shields.io/badge/awesome%3F-yes-brightgreen.svg
[contributors]: https://github.com/hassio-addons/dockerfile2json/graphs/contributors
[frenck]: https://github.com/frenck
[license-shield]: https://img.shields.io/github/license/hassio-addons/dockerfile2json.svg
[maintenance-shield]: https://img.shields.io/maintenance/yes/2017.svg
[project-stage-shield]: https://img.shields.io/badge/Project%20Stage-Experimental-yellow.svg
[dockerfile]: https://github.com/asottile/dockerfile
[asottile]: https://github.com/asottile
