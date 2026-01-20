import pandas as pd 

def load_counts(path: str) -> pd.DataFrame:
    """
    Load raw gene expression count matrix.
    Rows = genes, columns = samples.
    """
    df = pd.read_csv(path, index_col="gene")
    return df 