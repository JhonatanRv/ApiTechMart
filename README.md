#Siga os comandos abaixo no terminal:

python -m venv venv

cd venv/Scripts

activate



pip install mysqlclient

cd api-main

pip install django

pip install djangorestframework



python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
