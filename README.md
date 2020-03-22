# matrix-factorization-spark
A minimal PySpark implementation of Matrix Factorizations at Scale (Gittens et.al)

## Running the Cluster

To start cluster consisting of:

1. Run Spark Master
1. Run Spark Worker
1. Run Python Application
1. Start Application Shell

Run the following:

```
source docker-start.sh
```

To install dependencies:

```
# spark-app
source app-start.sh
```

<!-- TODO: Run Github action locally:

```
act
``` -->

<!-- ### TODO: Additional Notes

**Numpy and Alpine**

This project depends on `bde2020/spark-base` which uses `alpine:3.0` and is only compatible with `numpy<=1.14.4` -->
