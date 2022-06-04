#!/bin/bash

STACK_VERSION=8.0.0

docker pull docker.elastic.co/elasticsearch/elasticsearch:$STACK_VERSION
docker pull docker.elastic.co/kibana/kibana:$STACK_VERSION
docker pull docker.elastic.co/logstash/logstash:$STACK_VERSION
docker pull docker.elastic.co/beats/metricbeat:$STACK_VERSION
docker pull debian:11

python3 manage.py runserver $1

