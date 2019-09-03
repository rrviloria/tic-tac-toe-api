#!/bin/sh
# run-seed.sh

>&2 echo "\n\n\n*** Clearing database ***\n\n\n"
docker exec -it raymundtictactoe_web_1 pipenv run python manage.py flush --no-input
>&2 echo "\n\n\n*** Database cleared! ***\n\n\n"

>&2 echo "\n\n\n*** Seeding initial data ***\n\n\n"
docker exec -it raymundtictactoe_web_1 pipenv run python seed.py
>&2 echo "\n\n\n*** Seeding complete! ***\n\n\n"