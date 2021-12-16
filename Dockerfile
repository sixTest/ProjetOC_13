FROM python:3.8.12-slim-bullseye

WORKDIR /app

COPY . /app

EXPOSE 8000

RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

CMD ["python", "manage.py", "runserver"]