FROM elasticsearch:2.4.6-alpine

COPY ./compose/production/elasticsearch/elasticsearch-analysis-ik-1.10.6.zip /usr/share/elasticsearch/plugins/
RUN cd /usr/share/elasticsearch/plugins/ && mkdir ik && unzip elasticsearch-analysis-ik-1.10.6.zip -d ik/
RUN rm /usr/share/elasticsearch/plugins/elasticsearch-analysis-ik-1.10.6.zip

USER root
COPY ./compose/production/elasticsearch/elasticsearch.yml /usr/share/elasticsearch/config/
RUN chown elasticsearch:elasticsearch /usr/share/elasticsearch/config/elasticsearch.yml

USER elasticsearch

