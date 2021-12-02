FROM jupyter/pyspark-notebook:latest

ARG HADOOP_VERSION=3.3.1
ARG AWS_SDK_VERSION=1.11.901
ARG GOOGLE_APPLICATION_CREDENTIALS
ARG JSON_KEYFILE_NAME

USER root

RUN wget -q "https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/${HADOOP_VERSION}/hadoop-aws-${HADOOP_VERSION}.jar" -P /usr/local/jars/ && \
    wget -q "https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/${AWS_SDK_VERSION}/aws-java-sdk-bundle-${AWS_SDK_VERSION}.jar" -P /usr/local/jars/ && \
    wget -q "https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-hadoop3-latest.jar" -P /usr/local/jars/

RUN echo 'spark.driver.extraClassPath /usr/local/jars/*' >> "${SPARK_HOME}/conf/spark-defaults.conf" && \
    echo 'spark.serializer org.apache.spark.serializer.KryoSerializer' >> "${SPARK_HOME}/conf/spark-defaults.conf" && \
    echo 'spark.hadoop.fs.s3a.fast.upload True' >> "${SPARK_HOME}/conf/spark-defaults.conf" && \
    echo 'spark.hadoop.fs.s3a.impl org.apache.hadoop.fs.s3a.S3AFileSystem' >> "${SPARK_HOME}/conf/spark-defaults.conf" && \
    echo 'fs.gs.impl com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem' >> "${SPARK_HOME}/conf/spark-defaults.conf" && \
    echo 'fs.AbstractFileSystem.gs.impl com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS' >> "${SPARK_HOME}/conf/spark-defaults.conf" && \
    echo 'fs.gs.auth.service.account.enable True' >> "${SPARK_HOME}/conf/spark-defaults.conf"

COPY requirements.txt requirements.txt
COPY ${GOOGLE_APPLICATION_CREDENTIALS} /usr/local/conf/

ENV GOOGLE_APPLICATION_CREDENTIALS=/usr/local/conf/${JSON_KEYFILE_NAME}

RUN pip install -r requirements.txt && \
    pip install "jupyterlab>=3" "ipywidgets>=7.6"