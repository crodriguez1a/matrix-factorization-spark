#!/bin/bash

echo 'Spark Up!'

cd app/ && python3 -m pytest -x -rf
