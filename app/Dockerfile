# tirer l'image de base officielle
FROM python:3.10.8-slim-buster

# définir le répertoire de travail
ENV DockerHOME=/home/ing/wprojects/django-tdd-docker/app
RUN mkdir -p $DockerHOME  
WORKDIR $DockerHOME  

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . $DockerHOME 

# installer dépendances system
RUN apt-get update \
  && apt-get -y install gcc postgresql \
  && apt-get clean

# installer les dépendances
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt


# copier entrypoint.sh
COPY ./entrypoint.sh ${DockerHOME}/entrypoint.sh
RUN chmod +x ${DockerHOME}entrypoint.sh

# ajouter l'application
COPY . .

ENTRYPOINT ["${DockerHOME}/entrypoint.sh"]