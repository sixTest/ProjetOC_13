FROM python:3.8.12-slim-bullseye

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver"]