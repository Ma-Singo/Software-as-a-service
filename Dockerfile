FROM python:3.13-alpine

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

WORKDIR /src/app

COPY requirements.txt /src/app/requirements.txt

RUN pip install -r requirements.txt 


COPY . .

EXPOSE 8000

ENTRYPOINT ["/src/app/entrypoint.sh"]

CMD ["python3", "manage.py", "runserver"]



