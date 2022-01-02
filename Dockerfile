FROM python:3.8.12-slim-bullseye

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT