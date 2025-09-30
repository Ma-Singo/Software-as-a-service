FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt 


COPY . .

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]

CMD [ "runserver" ]



