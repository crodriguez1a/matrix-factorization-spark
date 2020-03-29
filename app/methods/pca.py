# @paper Principal Component Analysis
# PCA for its ubiquity
from typing import List
from pyspark import rdd, SparkContext
from pyspark.ml.linalg import DenseVector
from pyspark.mllib.linalg.distributed import RowMatrix, DenseMatrix, SingularValueDecomposition
import numpy as np

"""
@paper
Direct algorithms for computing the PCA decomposition
scale as O(mn2), so are not feasible for the scale of the
problems we consider. Instead, we use the iterative algorithm
presented in Algorithm 1
"""

"""
@paper
in step 1, a series of distributed matrix-vector products
against `A^T A` (MultiplyGramian) are used to extract Vk by
applying the implicitly restarted Arnoldi method (IRAM) [33],
"""


def multiply_gramian(mat: RowMatrix) -> DenseMatrix:
    """Computes the Gramian matrix `A^T A`."""
    return mat.computeGramianMatrix() # -> Vk

"""
@paper
then in step 2 a distributed matrix-matrix product followed
by a collect is used to bring AVk to the driver.
"""

def matrices_product(mat: RowMatrix, Vk: DenseMatrix) -> list:
    return mat.multiply(Vk).rows.collect() # -> AVk or Y to driver

"""
@paper
Step 3 occurs on the driver, and computes a final SVD on AVk
to extract the top left singular vectors Uk and the corresponding eigenvalues Σk.
Here QR and SVD compute the “thin” versions of the QR and SVD decompositions [16].
(Algorithm 1 calls MultiplyGramian, which is summarized in Algorithm 2).
"""

def compute_final_svd(sc: SparkContext, y: List[DenseVector], k:int) -> SingularValueDecomposition:
    Y: RowMatrix = RowMatrix(sc.parallelize(y))
    svd_model = Y.computeSVD(k=k, computeU=True)
    return svd_model


def pca(sc: SparkContext, mat: RowMatrix, k: int) -> np.ndarray:
    Vk: DenseMatrix = multiply_gramian(mat)
    Y: list = matrices_product(mat, Vk)
    final_svd: SingularValueDecomposition = compute_final_svd(Y, k)

    # U -> a distributed matrix whose columns are the left singular vectors
    # of the SingularValueDecomposition if computeU was set to be True.
    return final_svd.U
