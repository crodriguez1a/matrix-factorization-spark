#!/bin/bash

# Run Master
docker run --name spark-master -h spark-master -e ENABLE_INIT_DAEMON=false -d bde2020/spark-master:2.4.5-hadoop2.7

# Run Worker
docker run --name spark-worker-1 --link spark-master:spark-master -e ENABLE_INIT_DAEMON=false -d bde2020/spark-worker:2.4.5-hadoop2.7

# Run App
docker build --rm -t bde/spark-app .
docker run --name spark-app -e ENABLE_INIT_DAEMON=true --link spark-master:spark-master -d bde/spark-app

# Docker Reference
# run:
#   --rm | Automatically remove the container when it exits
#   -- name | Assign a name to the container
#   --link | Add link to another container
#   -e | Set environment variables
#   -d, --detach | Run container in background and print container ID

# build:
#   --rm | Remove intermediate containers after a successful build (default true)
#   -t, --tag | Name and optionally a tag in the 'name:tag' format

# Start App Shell
docker exec -it spark-app /bin/sh
