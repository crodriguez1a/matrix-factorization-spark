from dataclasses import dataclass

from pyspark import SparkConf, SparkContext, rdd
from pyspark.sql import SparkSession
from pyspark.mllib.linalg.distributed import RowMatrix

from methods.pca import pca


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
    rows: rdd.RDD = sc.parallelize([[1,2,3], [4,5,6]])
    mat: RowMatrix = RowMatrix(rows)
    svd: list = pca(sc, mat, rows.count())
    print(svd)
