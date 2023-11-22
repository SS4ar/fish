FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir flask gunicorn

CMD [ "gunicorn","-c","conf.py","app:app" ]