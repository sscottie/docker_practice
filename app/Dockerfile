FROM ubuntu:18.04
FROM python:3
MAINTAINER Andrei Titov

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY main.py ./
RUN apt-get install -y python3
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]