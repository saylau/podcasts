#!/bin/sh

container_type=${CONTAINER_TYPE-DJANGO};
celery_loglevel=${CELERY_LOGLEVEL-INFO};

if [ $container_type = "CELERY" ]; then
  celery -A config.celery_app worker --loglevel=$celery_loglevel

else

  python manage.py migrate --noinput
  gunicorn --bind 0.0.0.0:8000 --access-logfile - config.wsgi:application
fi;
