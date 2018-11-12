# dad-joke-bot

## Table of Contents

- [Install](#install)
- [Develop](#develop)
  - [How to run](#how-to-run)
  - [Code style and formatting](#code-style-and-formatting)
  - [Tests](#tests)

## Install

```bash
# create virtual env
python3 -m venv env

# activate the virtual env
source env/bin/activate

# Get a Dad joke via CLI
python ./manage.py [-j | --joke]

# install dependencies
poetry install
```

## Develop

### How to

```bash
# activate the virtual env
source env/bin/activate

# Use 'deactivate' to exit the virtual env
```

### Code style and formatting

Python code is styled per flake8 and formatted using [yapf](https://github.com/google/yapf).

### Tests

Ensure the source env/bin/activate is activated with `source env/bin/activate`.

To run tests:

`py.test` or with verbosity `py.test -vv`.

Test coverage:

On the command line run `py.test --cov`

To generate html coverage report run

```bash
py.test --cov-report html --cov --verbose
```

and then `open htmlcov/index.html` to open in the browser.
