#Siga os comandos abaixo no terminal:

python -m venv venv

cd venv/Scripts

activate


cd ..
cd ..

pip install mysqlclient

pip install django

pip install djangorestframework

pip install drf-yasg



python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
