import matplotlib.pyplot as plt 
import pandas as pd 


def plot_histogram(matrix: pd.DataFrame, title: str, output_path: str):
    """
    Plot and save a histogram of all values in a matrix.
    """

    values = matrix.values.flatten()

    plt.figure(figsize=(7, 5))
    plt.hist(values, bins=30)
    plt.title(title)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
