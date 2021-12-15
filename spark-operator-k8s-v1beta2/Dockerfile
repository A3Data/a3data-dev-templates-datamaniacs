FROM gcr.io/spark-operator/spark-py:v3.0.0
MAINTAINER Carlos Barbosa <carlos.barbosa@a3data.com.br>

#using root
USER root:root

#create directory for applications
RUN mkdir -p /app 

#copy application files
COPY ./src/ /app

#copy jars files
COPY ./jars/ /opt/spark/jars

#set main work directory
WORKDIR /app

#user
USER root
