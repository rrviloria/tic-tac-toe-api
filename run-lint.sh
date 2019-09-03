#!/bin/sh
# run-lint.sh

# Shell script for running tests inside a container

# This is it make sure that the code follows PEP8 standard

>&2 echo "\n\n\n*** Running lint ***\n\n\n"
docker exec -it raymundtictactoe_web_1 pipenv run flake8 --statistic --exclude='migrations/' --extend-ignore=F401 --ignore=E501,E402