from dataclasses import dataclass

from pyspark import SparkConf, SparkContext, rdd
from pyspark.sql import SparkSession
from pyspark.mllib.linalg.distributed import IndexedRow, DenseMatrix

from methods.pca import gramian_matrix


def init_session(app_name: str = "mxfs") -> SparkSession:
    spark: SparkSession = SparkSession \
                            .builder \
                            .appName(app_name) \
                            .getOrCreate()
    spark.sparkContext.getConf().getAll()
    return spark

if __name__ == "__main__":
    spark: SparkSession = init_session()
    sc: SparkContext = spark.sparkContext

    # TEMP
    rows: rdd.RDD = sc.parallelize([
        IndexedRow(0, [1,2,3]),
        IndexedRow(1, [4,5,6])
    ])
    gm: DenseMatrix = gramian_matrix(rows)
    print(gm.values)
