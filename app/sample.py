from pyspark import SparkConf, SparkContext, rdd

def create_spark_context(name: str) -> SparkContext:
    conf: SparkConf = SparkConf().setAppName(name)
    return SparkContext.getOrCreate(conf)

def spark_up(sc: SparkContext) -> rdd.RDD:
    sample: list = [1, 2, 3]
    # resilient distributed dataset
    distributed_sample: rdd.RDD = sc.parallelize(sample)
    # apply transformation, collect to master node
    return distributed_sample.map(lambda x: x+1).collect()


if __name__ == "__main__":
    sc: SparkContext = create_spark_context("lazy_eval")
    print(f"Parallelism across {sc.defaultParallelism} nodes")

    y: rdd.RDD = spark_up(sc)
    print(y)
