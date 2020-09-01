#!/usr/bin/env bash

echo "Deploying diabetes detection model in stage: production"

export MLFLOW_TRACKING_URI=http://0.0.0.0:5000

mlflow models serve -m models:/diabetes_detection/Production --no-conda
