#!/bin/bash

# echo username $DJANGO_SUPERUSER_USERNAME
# echo password $DJANGO_SUPERUSER_PASSWORD
# echo email $DJANGO_SUPERUSER_EMAIL

python3 manage.py makemigrations
python3 manage.py migrate
python manage.py createsuperuser --noinput

exec "$@"
