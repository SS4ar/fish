FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -y flask, gunicorn

CMD [ "gunicorn","-c","conf.py","app:app" ]