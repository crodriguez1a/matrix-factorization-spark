FROM bde2020/spark-submit:2.4.5-hadoop2.7

LABEL maintainer="Carlos Rodriguez crodriguez1a@gmail.com>"

COPY app-start.sh /
COPY app /app
COPY requirements.txt /app
RUN chmod +x /app-start.sh

# /usr/bin/python3
ENV PYSPARK_PYTHON python3
ENV PYSPARK_DRIVER_PYTHON python3

# CMD ["/app-start.sh"]
