FROM docker.elastic.co/logstash/logstash:8.0.0
COPY ./logstash.conf /usr/share/logstash/pipeline/
COPY ./logstash.yml /usr/share/logstash/config/
RUN mkdir -p /usr/share/logstash/config/certs
RUN chown -R logstash:root /usr/share/logstash/config/certs 
