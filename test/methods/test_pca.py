from app.methods.pca import multiply_gramian, matrices_product, compute_final_svd, pca
from pyspark import rdd, SparkContext
from pyspark.mllib.linalg.distributed import RowMatrix, DenseMatrix, RowMatrix, SingularValueDecomposition
import numpy as np
import pytest

@pytest.fixture
def rows(spark_context: SparkContext) -> rdd.RDD:
    return spark_context.parallelize([[1, 2, 3],[4, 5, 6]])

@pytest.fixture
def mat(rows: rdd.RDD) -> RowMatrix:
    # TODO: RowMatrix vs RowMatrix
    return RowMatrix(rows)

def test_multiply_gramian(spark_context: SparkContext, mat: RowMatrix):
    Vk: DenseMatrix = multiply_gramian(mat)
    assert Vk is not None

def test_matrices_product(spark_context: SparkContext, mat: RowMatrix):
    Vk: DenseMatrix = multiply_gramian(mat)
    Y: RowMatrix = matrices_product(mat, Vk)
    assert Y is not None

def test_compute_final_svd(spark_context: SparkContext, mat: RowMatrix, rows: rdd.RDD):
    k: int = 2
    Vk: DenseMatrix = multiply_gramian(mat)
    Y: RowMatrix = matrices_product(mat, Vk)
    svd: SingularValueDecomposition = compute_final_svd(spark_context, Y, k)

    assert svd is not None
