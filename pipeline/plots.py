import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Global aesthetic style for all diagnostic figures
# These plots are meant for exploratory QC, not final publication figures
sns.set_theme(style="whitegrid", context="talk")



def plot_histogram(matrix: pd.DataFrame, title: str, output_path: str):
    """
    Plot and save a histogram of all values in an expression matrix.

    This function is used for global distribution inspection to detect:
    - scale issues
    - extreme skewness
    - heavy tails or compression of values

    Expected input:
    - rows = genes
    - columns = samples
    """

    # Flatten matrix values into a single vector for global distribution
    values = matrix.values.flatten()

    plt.figure(figsize=(7, 5))
    plt.hist(values, bins=30)
    plt.title(title)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()




def plot_sample_boxplots(matrix: pd.DataFrame, outpath: str, title: str):
    """
    Generate one boxplot per sample to inspect distribution and scale differences.

    This plot is used to detect:
    - library size effects
    - scale inconsistencies
    - outliers and abnormal samples

    Expected input:
    - rows = genes
    - columns = samples
    """

    plt.figure(figsize=(9, 5))

    # Convert matrix from wide format (genes x samples)
    # to long format for seaborn plotting
    melted = (
        matrix.reset_index()
        .melt(id_vars="gene", var_name="Sample", value_name="Expression")
    )

    sns.boxplot(
        data=melted,
        x="Sample",
        y="Expression"
    )

    plt.title(title)
    plt.ylabel("Expression value")
    plt.xlabel("Sample")

    plt.tight_layout()
    plt.savefig(outpath, dpi=150)
    plt.close()