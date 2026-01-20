import pandas as pd 
import numpy as np 


def log2_transform(matrix: pd.DataFrame) -> pd.DataFrame:
    """
    Apply log2(x + 1) transformation to stabilize variance.
    """
    log_matrix = np.log2(matrix + 1)
    return log_matrix 
    