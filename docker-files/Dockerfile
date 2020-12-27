FROM python:3.6-alpine

COPY . /app
WORKDIR app

RUN pip install -r requirements.txt

RUN chmod +x docker-files/start
RUN chmod +x docker-files/unit_test

EXPOSE 8000
