#! /bin/bash

docker compose down -v
docker rmi $(docker images -q)
docker system prune -af

echo "Clear postgres_data dir"
chmod -R 755 /cookbook_https/postgres_data
rm -r /cookbook_https/postgres_data/*

echo "Clear logs, static, media"
rm /cookbook_https/log/django.log
rm -r /cookbook_https/static/*
rm -r /cookbook_https/media/*

echo
echo "Finished..."

