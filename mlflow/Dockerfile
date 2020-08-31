FROM python:3.8.5-slim-buster

WORKDIR /usr/local/mlflow
COPY . /usr/local/mlflow
RUN pip install pipenv
RUN pipenv install  --system --deploy
