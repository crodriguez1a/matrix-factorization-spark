from app.methods.pca import gramian_matrix
from pyspark import rdd, SparkContext
from pyspark.mllib.linalg.distributed import IndexedRow, DenseMatrix

def test_gramian_matrix(spark_context: SparkContext):
    rows: rdd.RDD = spark_context.parallelize([
        IndexedRow(0, [1, 2, 3]),
        IndexedRow(1, [4, 5, 6])
    ],)
    gm: DenseMatrix = gramian_matrix(rows)
    assert gm is not None
