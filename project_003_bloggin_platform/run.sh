#!/bin/bash

# echo username $DJANGO_SUPERUSER_USERNAME
# echo password $DJANGO_SUPERUSER_PASSWORD
# echo email $DJANGO_SUPERUSER_EMAIL

python3 manage.py makemigrations
python3 manage.py migrate
python manage.py createsuperuser --noinput

# gunicorn --bind 0.0.0.0:8000 todo_webapp.wsgi:application
python3 manage.py runserver "0.0.0.0:8000"
