FROM alpine:latest

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "/app/manage.py", "runserver"]

EXPOSE 8000
