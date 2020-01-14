#!/bin/bash

cd "$(dirname "$0")"
PYTHON_VENV=$(pipenv --venv)
uwsgi --socket :8081 --home $PYTHON_VENV -w main:app
