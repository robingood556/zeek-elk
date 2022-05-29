FROM debian:11

USER root

RUN apt-get update \
  && apt-get install -y cmake make gcc g++ flex bison libpcap-dev libssl-dev python3 python3-dev swig zlib1g-dev \
  && apt-get install -y python3-git python3-semantic-version \
  && apt-get -y install curl gnupg wget \
  && apt-get -y install net-tools \
  && echo 'deb http://download.opensuse.org/repositories/security:/zeek/Debian_11/ /' > /etc/apt/sources.list.d/zeek.list \
  && curl -fsSL https://download.opensuse.org/repositories/security:zeek/Debian_11/Release.key | gpg --dearmor | tee /etc/apt/trusted.gpg.d/security_zeek.gpg > /dev/null \
  && apt update \
  && apt-get -y install zeek \
  && rm -rf /var/lib/apt/lists/*


RUN curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-8.0.0-amd64.deb \
  && dpkg -i filebeat-8.0.0-amd64.deb

ENV PATH $PATH:/opt/zeek/bin

COPY filebeat.yml /etc/filebeat/filebeat.yml
COPY local.zeek /usr/local/zeek/share/zeek/site/local.zeek

RUN zeekctl install \
  && zeekctl start \
  && zeekctl deploy
 
COPY net.pcap ./
RUN zeek -r net.pcap LogAscii::use_json=T LogAscii::logdir=/opt/zeek/logs/current/
