# PDFmerger

config: django configurations
core: application source code

python3 -m venv .venv

python3 -m pip install django

djando --version

python manage.py migrate

python manage.py runserver

docker build -t the-merger .

docker run -d -e DJANGO_SETTINGS_MODULE='config.settings.prod' -p 8000:8000 the-merger:latest