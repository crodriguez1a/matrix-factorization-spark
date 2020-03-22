#!/bin/bash

echo 'Hello?'

cd /app/ \
   && pip3 install --upgrade pip \
   && pip3 install -r requirements.txt

python3 -m pytest -x -rf
python3 -m app
