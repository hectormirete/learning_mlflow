#!/usr/bin/env bash

echo "Buidling docker for diabetes detection model in stage: production"

export MLFLOW_TRACKING_URI=http://0.0.0.0:5000

mlflow models build-docker -m models:/diabetes_detection/Production -n "diabetes_detection_image"

echo "Deploying on local, port 5001"

docker run -p "5001:8080" diabetes_detection_image