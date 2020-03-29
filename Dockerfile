FROM bde2020/spark-submit:2.4.5-hadoop2.7

LABEL maintainer="Carlos Rodriguez crodriguez1a@gmail.com>"

COPY app /app
COPY test /app/test/
COPY requirements.txt /app/

COPY app-start.sh /
RUN chmod +x /app-start.sh

RUN cd /app/ \
    && pip3 install --upgrade pip \
    && pip3 install -r requirements.txt \
    && apk --no-cache add py3-numpy \
    && apk add neovim

# /usr/bin/python3
ENV PYSPARK_PYTHON python3
ENV PYSPARK_DRIVER_PYTHON python3

# CMD ["/app-start.sh"]
