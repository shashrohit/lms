FROM python:3.6-alpine

COPY . /app
WORKDIR app

RUN pip install -r requirements.txt

RUN chmod +x start

EXPOSE 8000

CMD ["sh", "start"]
