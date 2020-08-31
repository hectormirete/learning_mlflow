# Learning MLflow

This is a repo to try out and learn about the usage of [mlflow](www.mlflow.org)

# Running MLflow server
First you have to setup the env vars so run the next command and setup your own values

`` cp .env.example .env``

This setup logs the artifacts of MLflow on s3, so it requires and aws account an s3 bucket 
where to write the artifcats and an IAM user able to manage that bucket

MLflow server is dockerized, so to run it on your local you have to start the containers

``docker-compose up -d --build``

Now you will find the mlflow ui on <htttp://0.0.0.0:5000>

# Local setup

For the local setup, this repo is manage with pipenv, checkout how to install it [here](https://github.com/pypa/pipenv/blob/master/docs/install.rst)

Once installed, you can setup your local env with ``pipenv install --dev``

And later activate it with ``pipenv shell``

# Running experiments

Now you can start running the experiments and evaluate them on the webserver

```
python experiments/examples/train_diabetes.py
python experiments/examples/sklearn_elasticnet_wine.py
```
