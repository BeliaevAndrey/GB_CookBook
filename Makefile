# Django Cookbook Project Makefile

# Config constants
PROJECT = recipes_book
MANAGE = docker compose exec -T web python manage.py
STATIC_DIR = /large/data4/cookbook/static
MEDIA_DIR = /large/data4/cookbook/media
DB_DATA_DIR = /large/data4/cookbook/postgres_data

.PHONY: help build up down restart logs clean\
 		full-clean migrate makemigrations \
		createsuperuser shell dbshell

help:
	@echo "Recipes book Project Makefile"
	@echo "Usage: make [target]"
	@echo ""
	@echo "Basic targets:"
	@echo "  build      - Build docker images and run containers"
	@echo "  up         - Run containers"
	@echo "  down       - Down containers"
	@echo "  restart    - Restart containers"
	@echo "  logs       - Show containers logs"
	@echo "  clean      - Down containers and clean images"
	@echo "  full-clean - Full clean (containers, images, volumes)"
	@echo ""
	@echo "Django:"
	@echo "  migrate         - Apply migrations"
	@echo "  makemigrations  - Create new migrations"
	@echo "  createsuperuser - Create superuser"
	@echo "  shell           - Run Django shell"
	@echo ""
	@echo "  dbshell - Run DB shell"

build:
	@echo "Build Docker-images and set them up..."
	docker compose up -d --build
#	./scripts/bash/initial_migrations.sh
#	./scripts/bash/create_admin.sh


up:
	@echo "Start containers..."
	docker compose up -d

down:
	@echo "Stop and remove containers..."
	docker compose down

restart: down up

logs:
	@echo "Containers logs..."
	docker compose logs -f

clean:
	@echo "Stop and remove containers and remove volumes..."
	docker compose down --volumes

full-clean: clean
	@@echo "Removing Docker-images..."
	docker rmi $$(docker images -q "${PROJECT}*")

migrate:
	@echo "Applying migrations..."
	$(MANAGE) migrate --noinput

makemigrations:
	@echo "Create migrations..."
	$(MANAGE) makemigrations

createsuperuser:
	@echo "Create superuser..."
	$(MANAGE) createsuperuser

shell:
	@echo "Start Django shell..."
	docker compose exec web python manage.py shell

dbshell:
	@echo "Start DB shell..."
	docker compose exec web python manage.py dbshell

test:
	@echo "Run tests..."
	$(MANAGE) test --noinput
