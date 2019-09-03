#!/bin/sh
# init-app.sh


set -e

cmd="$@"

until PGPASSWORD=postgres psql -h db -U postgres -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

#Caution sleeping:
sleep 5

#Running migrations:
>&2 echo "\n\n\n*** Running migrations ***\n\n\n"
#Use pipenv's Python (which is Dockerfile's Python):
pipenv run python manage.py migrate

>&2 echo "\n\n\n*** Running collectstatic ***\n\n\n"
#Auto-collect static files and do not push static files on git
pipenv run python manage.py collectstatic --noinput

#Running main command "runserver":
>&2 echo "\n\n\n***  Database is up - executing Docker container entrypoint (startup) command ***\n\n\n"
exec $cmd
