#!/bin/sh

mkdir -p /app/static
mkdir -p /app/media

python manage.py migrate --noinput
python manage.py createcachetable
python manage.py compilemessages

exec "$@"