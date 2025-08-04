#! /bin/bash

echo "Building service directories..."
mkdir -p /cookbook_https/{log,media,static,postgres_data}
chown -R www-data:www-data /cookbook_https