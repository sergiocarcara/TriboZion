
release: python3 manage.py migrate
release: python3 manage.py makemigrations
web: gunicorn triboZion.wsgi --preload --log-file
