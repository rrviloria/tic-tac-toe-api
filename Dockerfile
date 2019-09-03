FROM python:3.7.3-alpine3.9
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache bash

#this is required by 'init-app.sh' (psql):
RUN apk add postgresql-client

#We need to add some additional postgreSQL libs because Alphine doesn't have them:
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev

RUN mkdir /code
WORKDIR /code

RUN pip install --upgrade pip
RUN pip install pipenv

COPY Pipfile /code/

RUN apk add --no-cache make python3-dev libffi-dev libressl-dev libxslt-dev

RUN apk add --no-cache jpeg-dev zlib-dev

#--system uses system's (Dockerfile's) python
#--deploy fails if packages are outdated
#--dev installs all main + dev dependencies
RUN pipenv install --dev --skip-lock

RUN apk --purge del .build-deps

COPY . /code/

CMD ["chmod", "+x", "/code/init-app.sh"]
