#!/bin/sh
cd src
echo "Создаю миграции..."
python manage.py makemigrations
echo "Отправляю миграции..."
python manage.py migrate
echo "Собираю статику..."
python manage.py collectstatic --no-input
echo "Запускаю сервер..."
gunicorn justauth.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4 --reload