#!/bin/bash
python manage.py makemigrations
python manage.py migrate

USER="admin@myproject.com"
PASS="password"
MAIL="admin@myproject.com"
script="
from django.contrib.auth.models import User;

username = '$USER';
password = '$PASS';
email = '$MAIL';

if User.objects.filter(username=username).count()==0:
    User.objects.create_superuser(username, email, password);
    print('Superuser created.');
else:
    print('Superuser creation skipped.');
"
printf "$script" | python manage.py shell

exec gunicorn -c gconfig.py gsm.wsgi:application