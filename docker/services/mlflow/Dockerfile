FROM python:3.10-slim

RUN apt-get update && apt-get install -y curl
RUN pip install mlflow[extras] psycopg2-binary boto3 cryptography pymysql
RUN apt-get update && apt-get install -y iputils-ping curl
RUN apt-get update && apt-get install -y curl unzip
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install \
    && rm -rf aws awscliv2.zip
EXPOSE 5001
