#!/bin/sh
# run-test.sh

# Shell script for running tests inside a container

>&2 echo "\n\n\n*** Running tests ***\n\n\n"
docker exec -it raymundtictactoe_web_1 pipenv run python manage.py test -v 2