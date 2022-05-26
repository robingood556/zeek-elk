#!/bin/bash

VERSION="8.0.0"

docker pull elasticsearch:$VERSION
docker pull kibana:$VERSION  
docker pull logstash:$VERSION

python manage.py runserver $1

