# `cffconvert`

[![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1162057.svg)](https://doi.org/10.5281/zenodo.1162057)
[![Travis build status](https://travis-ci.org/citation-file-format/cff-converter-python.svg?branch=master)](https://travis-ci.org/citation-file-format/cff-converter-python)
[![SonarCloud Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=citation-file-format_cff-converter-python&metric=alert_status)](https://sonarcloud.io/dashboard?id=citation-file-format_cff-converter-python)
[![PyPi Badge](https://img.shields.io/pypi/v/cffconvert.svg?colorB=blue)](https://pypi.python.org/pypi/cffconvert/)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/1811/badge)](https://bestpractices.coreinfrastructure.org/projects/1811)
[![Research Software Directory](https://img.shields.io/badge/rsd-cffconvert-00a3e3.svg)](https://www.research-software.nl/software/cff-converter-python)
[![fair-software.eu](https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F-green)](https://fair-software.eu)

Command line program to validate and convert [`CITATION.cff`](https://github.com/citation-file-format/citation-file-format) files.

Supported input versions of the Citation File Format:

| Citation File Format schema version | Link to Zenodo release |
| --- | --- |
| `1.2.0` | [![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5171937.svg)](https://doi.org/10.5281/zenodo.5171937) |
| `1.1.0` | [![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4813122.svg)](https://doi.org/10.5281/zenodo.4813122) |
| `1.0.3` | [![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1222163.svg)](https://doi.org/10.5281/zenodo.1222163) |
| `1.0.2` | [![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1120256.svg)](https://doi.org/10.5281/zenodo.1120256) |
| `1.0.1` | [![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1117789.svg)](https://doi.org/10.5281/zenodo.1117789) |

Supported output formats:

1.  BibTeX
1.  CodeMeta
1.  EndNote
1.  JSON
1.  plaintext APA
1.  RIS
1.  schema.org JSON
1.  Zenodo JSON

Besides local files, `cffconvert` can fetch `CITATION.cff` file contents from the following GitHub URLs:

1.  `https://github.com/<org>/<repo>`
2.  `https://github.com/<org>/<repo>/tree/<sha>`
3.  `https://github.com/<org>/<repo>/tree/<tagname>`
4.  `https://github.com/<org>/<repo>/tree/<branchname>`

`cffconvert` does not aim to support the full Citation File Format specification.

## Installing

To install in user space, 

```shell
python3 -m pip install --user cffconvert
```
Ensure that the user space directory `~/.local/bin/` is on the `PATH`.

```shell
which cffconvert
```
should now return the location of the program.

See [docs/alternative-install-options.md](docs/alternative-install-options.md) for alternative install options.

## Command line interface

See `cffconvert`'s options:

```shell
cffconvert --help
```

Shows:

```shell
Usage: cffconvert [OPTIONS]

Options:
  -i TEXT                         Path to the CITATION.cff input file. Use '-i -' to read from STDIN.
  -o TEXT                         Path to the output file.
  -f [bibtex|cff|codemeta|endnote|ris|schema.org|zenodo|apalike]
                                  Output format.
  -u, --url TEXT                  URL of the repo containing the CITATION.cff (currently only github.com is supported;
                                  may include branch name, commit sha, tag name). For example:
                                  'https://github.com/citation-file-format/cff-converter-python' or
                                  'https://github.com/citation-file-format/cff-converter-python/tree/main'
  -h, --help                      Show help and exit.
  --show-trace                    Show error trace.
  --validate                      Validate the CITATION.cff found at the URL or supplied through '-i'.
  --ignore-suspect-keys           Ignore any keys from CITATION.cff that are likely out of date, such as 'commit',
                                  'date-released', 'doi', and 'version'.
  --verbose                       Provide feedback on what was entered.
  --version                       Print version and exit.
```

## Example usage

The following examples assume a `CITATION.cff` file with the following contents is present in the current working directory:

```yaml
authors:
  - family-names: Spaaks
    given-names: "Jurriaan H."
cff-version: 1.1.0
date-released: 2019-11-12
doi: 10.5281/zenodo.1162057
message: "If you use this software, please cite it using these metadata."
repository-code: "https://github.com/citation-file-format/cff-converter-python"
title: cffconvert
version: 1.3.3
```

### Converting to BibTeX

```shell
cffconvert -f bibtex
```

(see [result](docs/example-result-bibtex.md))

### Converting to CodeMeta

```shell
cffconvert -f codemeta
```

(see [result](docs/example-result-codemeta.md))

### Converting to EndNote

```shell
cffconvert -f endnote
```

(see [result](docs/example-result-endnote.md))

### Converting to RIS

```shell
cffconvert -f ris
```

(see [result](docs/example-result-ris.md))

### Converting to schema.org JSON

(schema.org is used in websites to improve ranking by search engines)

```shell
cffconvert -f schema.org
```

(see [result](docs/example-result-schema-org.md))

### Converting to Zenodo JSON

Convert the contents of a local file `CITATION.cff` into the format used by `.zenodo.json` files (see [Zenodo's API
docs](http://developers.zenodo.org/#representation)):

```shell
cffconvert -f zenodo
```

(see [result](docs/example-result-zenodo.md))

### Converting to APA-like

```shell
cffconvert -f apalike
```

(see [result](docs/example-result-apalike.md))