#!/bin/sh
set -e

echo "Preparing users migrations..."
python manage.py makemigrations users --noinput

echo "Applying users migrations..."
python manage.py migrate users --noinput

#echo "Creating core tables with SQL..."
#psql $DATABASE_URL <<EOF
#CREATE TABLE IF NOT EXISTS cookbook_category (
#    id BIGSERIAL PRIMARY KEY,
#    title VARCHAR(100) NOT NULL,
#    description TEXT NOT NULL
#);

#echo "Collecting static files..."
#python manage.py collectstatic --clear --noinput
#
#echo "Copying custom styles and images..."
#cp -r ./custom_data_css_img/* ./static/

echo "Creating cache table..."
python manage.py createcachetable

echo "Preparing cookbook  migrations..."
python manage.py makemigrations cookbook --noinput
echo "Applying cookbook migrations..."
python manage.py migrate cookbook --noinput

echo "Preparing migrations..."
python manage.py makemigrations --noinput
echo "Applying migrations..."
python manage.py migrate --noinput

echo "Creating categories..."
python manage.py fill_categories

#echo "Creating superuser..."
#if [[ -z $(python manage.py shell -c \
#    "from django.contrib.auth import get_user_model; User = get_user_model(); print(User.objects.filter(username='$ADMIN_USERNAME').exists())" ]];
#then
#  python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('$ADMIN_USERNAME', '$ADMIN_EMAIL', '$ADMIN_PASSWORD')"
#  echo "Superuser created"
#else
#   echo "Superuser already exists"
#fi

exec "$@"