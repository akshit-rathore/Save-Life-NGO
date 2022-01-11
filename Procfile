release: python manage.py migrate
release: python manage.py createsuperuser_if_none_exists --user=admin --password=change
web: gunicorn SaveLife.wsgi --log-file=-