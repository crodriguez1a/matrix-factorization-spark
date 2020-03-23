# @paper Principal Component Analysis
# PCA for its ubiquity

from pyspark import rdd
from pyspark.mllib.linalg.distributed import IndexedRowMatrix, DenseMatrix

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


def multiply_gramian(mat: IndexedRowMatrix) -> DenseMatrix:
    """Computes the Gramian matrix `A^T A`."""
    return mat.computeGramianMatrix() # -> Vk

"""
@paper
then in step 2 a distributed matrix-matrix product followed
by a collect is used to bring AVk to the driver.
"""

def matrices_product(mat: IndexedRowMatrix, Vk: DenseMatrix) -> IndexedRowMatrix:
    return mat.multiply(Vk) # -> AVk or Y

"""
@paper
Step 3 occurs on the driver, and computes a final SVD on AVk
to extract the top left singular vectors Uk and the corresponding eigenvalues Σk.
Here QR and SVD compute the “thin” versions of the QR and SVD decompositions [16].
(Algorithm 1 calls MultiplyGramian, which is summarized in Algorithm 2).
"""

def compute_final_svd(Y: IndexedRowMatrix, k:int) -> list:
    svd_model = Y.computeSVD(k=k, computeU=True)
    # svd_model.s
    # svd_model.V
    return svd_model.U.rows.collect()


def pca(mat: IndexedRowMatrix, k: int) -> list:
    Vk: DenseMatrix = multiply_gramian(mat)
    Y: IndexedRowMatrix = matrices_product(mat, Vk)
    final_svd: list = compute_final_svd(Y, k)

    return final_svd
