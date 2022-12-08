# tirer l'image de base officielle
FROM python:3.10.8-slim-buster

# définir le répertoire de travail
ENV DockerHOME=/home/ing/wprojects/django-tdd-docker/app
RUN mkdir -p $DockerHOME  
WORKDIR $DockerHOME  

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# installer les dépendances
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# ajouter l'application
COPY . .
