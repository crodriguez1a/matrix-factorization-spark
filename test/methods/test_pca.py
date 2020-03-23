from app.methods.pca import multiply_gramian
from pyspark import rdd, SparkContext
from pyspark.mllib.linalg.distributed import IndexedRow, IndexedRowMatrix, DenseMatrix

def test_multiply_gramian(spark_context: SparkContext):
    rows: rdd.RDD = spark_context.parallelize([
        IndexedRow(0, [1, 2, 3]),
        IndexedRow(1, [4, 5, 6])
    ],)
    mat: IndexedRowMatrix = IndexedRowMatrix(rows)
    Vk: DenseMatrix = multiply_gramian(mat)
    assert Vk is not None
