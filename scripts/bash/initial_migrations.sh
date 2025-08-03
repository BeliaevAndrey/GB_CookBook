#! /bin/bash

echo "Collect static"
docker compose exec web python manage.py collectstatic --noinput

echo "Copy service files to static"
docker compose exec web cp -r ./custom_data_css_img/* ./static


echo "Applying basic authentication migrations..."
docker exec cookbook-web python manage.py migrate auth

echo "Applying basic users migrations..."
docker exec cookbook-web python manage.py migrate users

echo "Applying basic admin migrations..."
docker exec cookbook-web python manage.py migrate admin

echo "Applying fake cookbook migrations (relations already created by DB initial script)..."
docker exec cookbook-web python manage.py migrate --fake sessions zero

echo "Applying fake cookbook migrations 0001..."
docker exec cookbook-web python manage.py migrate --fake cookbook 0001

echo "Applying fake cookbook migrations 0002..."
docker exec cookbook-web python manage.py migrate --fake cookbook 0002

echo "Filling DB with basic categories..."
docker exec cookbook-web python manage.py fill_categories

echo "Add the constraint foreign key on table cookbook_recipes"
docker exec -it cookbook-web python manage.py dbshell \
    -- -c "ALTER TABLE cookbook_recipe ADD CONSTRAINT cookbook_recipe_author_id_8a2bc8a4_fk_users_customuser_id FOREIGN KEY (author_id) REFERENCES users_customuser (id) DEFERRABLE INITIALLY DEFERRED;"

echo "Create index by new constraint"
docker exec -it cookbook-web python manage.py dbshell \
    -- -c "CREATE INDEX "cookbook_recipe_author_id_8a2bc8a4" ON "cookbook_recipe" ("author_id");"

echo "Applying the rest migrations..."
docker exec cookbook-web python manage.py migrate

echo "Checklist of migrations applied."
docker exec cookbook-web python manage.py showmigrations

echo
echo "Don't forget to create superuser (interactive)"
echo
