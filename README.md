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

# Deployment with mlflow

To deploy the model with mlflow locally run the next command

```
sh scripts/deploy_diabetes_detection_prod.sh
```

Note: this requires one of the registered models to be move to *Production* stage

# Deployment with docker

To deploy de model using docker run:

```
sh scripts/docker_deployment_diabetes_detection.sh
```

Note: same as the other, requires a diabetes detection model with Production stage

# Model invocation
To invoke the model run

```
python scripts/invoke_diabetes_detection.py
```

Note: checkout the port matches with the deployed model

# Alternative

If you want to load the model into an application you can load the model in memory
as it´s done in example of ``scripts/make_predictions.py``. This way you can have 
together the inference, the preprocessing and postprocessing of the model.