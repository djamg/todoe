FROM python:3.9-slim-bullseye

RUN mkdir /app

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN flask db migrate

CMD ["python3", "run.py"]
