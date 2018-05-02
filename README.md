# Python 3 Boilerplate

[![Build Status](https://travis-ci.org/seungjaeryanlee/python3-boilerplate.svg?branch=master)](https://travis-ci.org/seungjaeryanlee/python3-boilerplate)

This is a simple boilerplate (project template) for Python 3.

## Packages

[**Pytest**](https://docs.pytest.org/en/latest/) is a test framework for Python. It is arguably better than unittest that is included in Python standard library due to its conciseness and flexibility.

[**Pylint**](https://www.pylint.org/) is a linter for Python 3 that adheres to PEP 8, the Python style guide. It helps enforce coding style throughout your package.

[**Sphinx**](http://www.sphinx-doc.org/en/master/) is a documentation generator that generates HTML pages from the docstrings in the code. We use [numpydoc](https://numpydoc.readthedocs.io/en/latest/) format for docstrings.

[**TravisCI**](https://travis-ci.org/) is a continuous integration(CI) service that is free for open source projects. TravisCI allows you to automate Quality Assurance (QA) and have confidence on deployed code.

## Setup

Install necessary packages from PyPI using `pip`.

```
pip install -r requirements.txt
```

## Using Packages

### Pytest

Run the following command:

```
pytest
```

### Pylint

Run the following command:

```
pylint *
```

### Sphinx

To automatically generate documentation from your code, go to `/docs` and run

```
make autodocs
make html
```

## Using Boilerplate

1. Fork this repository by pressing the 'Fork' button.

2. Find all instances of `package_name` in your forked repository and replace them with your own package name.

3. Change the copyright and author information in `docs/source/conf.py`.

4. Connect your repository with Travis CI by visiting [travis-ci.org](https://travis-ci.org). Change status image in `README.md`.
