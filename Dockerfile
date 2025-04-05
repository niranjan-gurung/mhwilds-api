FROM python:3.13

WORKDIR /api

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .