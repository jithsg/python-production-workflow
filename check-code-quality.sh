#!/bin/bash

set -e
echo "hi"

black --exclude=venv --line-length=120 .
pylint --rcfile .pylintrc *.py
flake8 --config .flake8 *.py
mypy *.py
ruff *.py --config ruff.toml --fix
isort . --settings .isort.cfg
