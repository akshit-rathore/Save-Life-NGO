release: python manage.py migrate
release: python manage.py createsuperuser --user=admin --password=admin 
web: gunicorn SaveLife.wsgi --log-file=-