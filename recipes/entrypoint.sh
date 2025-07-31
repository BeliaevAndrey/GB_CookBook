#!/bin/sh
set -e
#
#echo "Waiting for PostgreSQL..."
#while ! nc -z $DB_HOST $DB_PORT; do sleep 0.5; done
#echo "PostgreSQL started"

#echo "Applying auth migrations..."
#python manage.py migrate auth

#echo "Applying users migrations..."
#python manage.py migrate users
#
#echo "Creating core tables with SQL..."
#psql $DATABASE_URL <<EOF
#CREATE TABLE IF NOT EXISTS cookbook_category (
#    id BIGSERIAL PRIMARY KEY,
#    title VARCHAR(100) NOT NULL,
#    description TEXT NOT NULL
#);
#
#CREATE TABLE IF NOT EXISTS cookbook_recipe (
#    id BIGSERIAL PRIMARY KEY,
#    name VARCHAR(100) NOT NULL,
#    description TEXT NOT NULL,
#    ingredients VARCHAR(2000) DEFAULT '...' NOT NULL,
#    steps TEXT NOT NULL,
#    duration INTEGER NOT NULL CHECK (duration >= 0),
#    image VARCHAR(255),
#    add_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#    author_id INTEGER NOT NULL REFERENCES users_customuser(id) ON DELETE CASCADE,
#    category_id BIGINT REFERENCES cookbook_category(id) ON DELETE SET NULL
#);
#EOF

#echo "Applying cookbook migrations..."
#python manage.py migrate cookbook
python manage.py migrate

echo "Creating superuser..."
if [ -z "$(python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); print(User.objects.filter(username='$ADMIN_USERNAME').exists()")" ]; then
    python manage.py shell -c "\
    from django.contrib.auth import get_user_model; \
    User = get_user_model(); \
    User.objects.create_superuser('$ADMIN_USERNAME', '$ADMIN_EMAIL', '$ADMIN_PASSWORD')"
    echo "Superuser created"
else
    echo "Superuser already exists"
fi

echo "Collecting static files..."
python manage.py collectstatic --clear

echo "Creating cache table..."
python manage.py createcachetable

#echo "Compiling messages..."
#python manage.py compilemessages

exec "$@"