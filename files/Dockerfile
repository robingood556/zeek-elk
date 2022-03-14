FROM docker.elastic.co/beats/filebeat:8.0.0

USER root
RUN apt-get update -y
RUN apt-get install nano cmake make gcc g++ flex bison libpcap-dev libssl-dev python3 python3-dev swig zlib1g-dev -y

RUN apt-get install python3-git python3-semantic-version -y && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp/build
RUN git clone --recursive https://github.com/zeek/zeek

WORKDIR /tmp/build/zeek
RUN ./configure
RUN make
RUN make install

ENV PATH /usr/local/zeek/bin:$PATH

RUN apt-get update \
    && apt-get -y install --no-install-recommends libpcap0.8 libssl1.1 libmaxminddb0 python2.7-minimal python3-minimal python3-pip inotify-tools git \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip3 install setuptools
RUN pip3 install zkg

RUN echo y | zkg autoconfig
RUN zkg install --force ja3 hassh
 
COPY local.zeek /usr/local/zeek/share/zeek/site/local.zeek 
COPY node.cfg /usr/local/zeek/etc/node.cfg
COPY filebeat.yml /usr/share/filebeat/filebeat.yml

RUN zeekctl deploy
