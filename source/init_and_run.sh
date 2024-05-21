#!/bin/sh

# Создаем миграции и применяем их
python manage.py makemigrations
python manage.py migrate
if [ ! -d 'static' ]; then
    python  manage.py collectstatic
fi

# Создаем суперпользователя, если его не существует
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from accounts.account_type_choices import AccoutTypeChoices
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
user = authenticate(username="admin", password="admin")
user.role = AccoutTypeChoices.TEACHER
user.save()
EOF

# Запускаем Django сервер
exec gunicorn main_config.wsgi:application --bind 0.0.0.0:8000 --workers 4
