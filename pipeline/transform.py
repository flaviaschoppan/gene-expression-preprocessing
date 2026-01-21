import pandas as pd 
import numpy as np 


def log2_transform(matrix: pd.DataFrame) -> pd.DataFrame:
    """
    Apply log2(x + 1) transformation to stabilize variance.
    """
    log_matrix = np.log2(matrix + 1)
    return log_matrix 

def filter_low_variance_genes(
    matrix: pd.DataFrame,
    min_variance: float = 0.01
) -> pd.DataFrame:
    """
    Remove genes with variance below a given threshold.

    Rows = genes
    Columns = samples

    Genes with (near) zero variance across samples do not contribute
    to multivariate analyses such as PCA or clustering.
    """

    # Compute variance per gene (row-wise)
    variances = matrix.var(axis=1)

    # Select genes that pass the variance threshold
    keep_mask = variances >= min_variance

    # Filter matrix
    filtered_matrix = matrix.loc[keep_mask]

    return filtered_matrix