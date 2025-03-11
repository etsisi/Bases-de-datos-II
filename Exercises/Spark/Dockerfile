FROM bitnami/spark:latest

USER root

RUN install_packages curl

RUN mkdir -p /app/jars

RUN curl -L -o /app/jars/spark-cassandra-connector.jar \
    https://repo1.maven.org/maven2/com/datastax/spark/spark-cassandra-connector_2.12/3.3.0/spark-cassandra-connector_2.12-3.3.0.jar

ENV SPARK_EXTRA_CLASSPATH=/app/jars/spark-cassandra-connector.jar
