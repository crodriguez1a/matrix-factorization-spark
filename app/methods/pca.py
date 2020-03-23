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


def gramian_matrix(rows: rdd.RDD) -> DenseMatrix:
    """Computes the Gramian matrix `A^T A`."""
    mat = IndexedRowMatrix(rows)
    return mat.computeGramianMatrix()

"""
@paper
then in step 2 a distributed matrix-matrix product followed
by a collect is used to bring AVk to the driver.
"""

# TODO: mat.multiply(DenseMatrix(2, 2, [0, 2, 1, 3])).rows.collect()

"""
@paper
Step 3 occurs on the driver, and computes a final SVD on AVk
to extract the top left singular vectors Uk and the corresponding eigenvalues Σk.
Here QR and SVD compute the “thin” versions of the QR and SVD decompositions [16].
(Algorithm 1 calls MultiplyGramian, which is summarized in Algorithm 2).
"""
