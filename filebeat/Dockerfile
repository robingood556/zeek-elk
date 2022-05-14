FROM debian:stable

USER root
RUN apt-get update \
  && apt-get install -y cmake make gcc g++ git flex bison libpcap-dev libssl-dev python3 python3-dev swig zlib1g-dev \
  && rm -rf /var/lib/apt/lists/*

RUN git clone --recursive https://github.com/zeek/zeek \
  && cd zeek \
  && ./configure \
  && make \
  && make install

ENV PATH $PATH:/usr/local/zeek/bin

RUN apt-get update \
  && apt-get -y install gnupg wget \ 
  && wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add - \
  && apt-get -y install apt-transport-https \
  && echo "deb https://artifacts.elastic.co/packages/8.x/apt stable main" | tee /etc/apt/sources.list.d/elastic-8.x.list \
  && apt-get update \
  && apt-get install filebeat \
  && apt-get install net-tools \
  && rm -rf /var/lib/apt/lists/*

COPY filebeat.yml /etc/filebeat/filebeat.yml
COPY local.zeek /usr/local/zeek/share/zeek/site/local.zeek

RUN zeekctl deploy 
COPY net.pcap ./
RUN zeek -r net.pcap LogAscii::use_json=T LogAscii::logdir=/usr/local/zeek/logs/current/
