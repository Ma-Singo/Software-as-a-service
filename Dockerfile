FROM python:3.13-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /src/app
COPY requirements.txt manage.py .
RUN pip install -r requirements.txt 
COPY . .
EXPOSE 8000