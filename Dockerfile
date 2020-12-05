FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1

# Allows docker to cache installed dependencies between builds
COPY ./requirements requirements
RUN pip install -r requirements/production.txt

# Set volume for database and static files.
RUN mkdir -p /static /media

# Set docker-entrypoint
# COPY ./docker-entrypoint.sh /docker-entrypoint.sh
# RUN chmod +x /docker-entrypoint.sh

# Adds our application code to the image
COPY . /app
WORKDIR /app

ENV STATIC_ROOT /static
ENV MEDIA_ROOT /media

EXPOSE 8000

# Collect static
RUN python manage.py collectstatic --noinput


#CMD gunicorn --bind 0.0.0.0:8000 --access-logfile - apps.wsgi:application
# CMD ["/docker-entrypoint.sh"]
