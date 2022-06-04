#!/bin/bash

STACK_VERSION=8.0.0

docker pull elasticsearch:$STACK_VERSION
docker pull kibana:$STACK_VERSION
docker pull logstash:$STACK_VERSION
docker pull debian:11

python3 manage.py runserver $1

