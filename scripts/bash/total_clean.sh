#! /bin/bash

docker compose down -v
docker rmi $(docker images -q)
docker system prune -af

echo "Clear postgres_data dir"
chmod -R 755 /cookbook/postgres_data
rm -r /cookbook/postgres_data/*

echo "Clear logs, static, media"
rm /cookbook/log/django.log
rm -r /cookbook/static/*
rm -r /cookbook/media/*

echo
echo "Finished..."

