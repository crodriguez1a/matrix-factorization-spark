#!/bin/bash

echo 'Spark Up!'

docker-compose up
docker exec -it spark-app /bin/sh
