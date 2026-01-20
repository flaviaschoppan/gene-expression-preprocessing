import pandas as pd 


def cpm(counts: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize raw counts to CPM (Counts Per Million).

    Each column (sample) is divided by its total counts and multiplied by 1e6.
    """

    # Sum all reads per sample (per column)
    library_sizes = counts.sum(axis=0)

    # Divide each column by its total and multiply by 1e6
    cpm_matrix = counts.div(library_sizes, axis=1) * 1e6

    return cpm_matrix
