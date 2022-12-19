# Extract base image
FROM python:3.8-slim-buster

# Directory where instructions are
# executed
WORKDIR /usr/src/app
ADD requirements.txt .

# Port
EXPOSE 5000/tcp

# Install required packages
# Command to launch
CMD apt-get update && apt-get upgrade -y && apt-get install -y git && \
    pip install -r /usr/src/app/requirements.txt && \
    mlflow server \
    --backend-store-uri sqlite:///mlflow.db \
    --default-artifact-root s3://mlflow/ \
    --host 0.0.0.0