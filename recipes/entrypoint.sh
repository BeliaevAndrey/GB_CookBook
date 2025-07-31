#!/bin/sh

mkdir -p /app/static
mkdir -p /app/media

echo "I start migrations"
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py createcachetable
python manage.py compilemessages

exec "$@"