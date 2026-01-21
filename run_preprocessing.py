"""
Gene expression preprocessing pipeline.

This script implements a minimal and explicit preprocessing workflow for
gene expression matrices before any multivariate analysis (e.g. PCA, clustering).

Pipeline steps:
1. Load raw count matrix
2. Normalize to CPM (Counts Per Million)
3. Apply log2(x + 1) transformation
4. Save processed matrices as artifacts
5. Generate diagnostic distribution plots
6. Generate per-sample QC boxplots

The goal is numerical conditioning and quality inspection of the data before 
downstream analyses.
"""

from pipeline.io import load_counts
from pipeline.normalization import cpm
from pipeline.transform import log2_transform, filter_low_variance_genes
from pipeline.plots import plot_histogram, plot_sample_boxplots


def main():
    # ------------------------------------------------------------------
    # Step 1 — Load raw expression matrix
    # ------------------------------------------------------------------
    print("Loading raw counts...")
    counts = load_counts("data/raw/counts.csv")
    print("✓ Step 1 finished: Raw counts loaded\n")

    # ------------------------------------------------------------------
    # Step 2 — Raw counts QC (before any transformation)
    # ------------------------------------------------------------------
    print("Generating raw counts QC plots...")

    plot_histogram(
        counts,
        title="Distribution of raw counts",
        output_path="outputs/figures/raw_counts_histogram.png"
    )

    plot_sample_boxplots(
        counts,
        "outputs/figures/boxplot_raw_counts_per_sample.png",
        "Raw counts distribution per sample"
    )

    print("✓ Step 2 finished: raw counts QC plots generated\n")

    # ------------------------------------------------------------------
    # Step 3 — CPM normalization
    # ------------------------------------------------------------------
    print("Applying CPM normalization...")
    cpm_matrix = cpm(counts)
    print("✓ Step 3 finished: CPM normalization applied\n")

    # ------------------------------------------------------------------
    # Step 4 — Log2 transformation
    # ------------------------------------------------------------------
    print("Applying log2 transformation...")
    log_matrix = log2_transform(cpm_matrix)
    print("✓ Step 4 finished: log2 transformation applied\n")

    # ------------------------------------------------------------------
    # Step 5 — Save processed matrices as pipeline artifacts
    # ------------------------------------------------------------------
    print("Saving processed matrices...")
    cpm_matrix.to_csv("outputs/matrices/cpm_matrix.csv")
    log_matrix.to_csv("outputs/matrices/log2_cpm_matrix.csv")
    print("✓ Step 5 finished: matrices saved to outputs/matrices/\n")

    # ------------------------------------------------------------------
    # Step 6 — Generate global distribution diagnostics
    # ------------------------------------------------------------------
    print("Generating diagnostic histograms...")

    plot_histogram(
        cpm_matrix,
        title="Distribution of CPM values",
        output_path="outputs/figures/cpm_histogram.png"
    )

    plot_histogram(
        log_matrix,
        title="Distribution of log2(CPM + 1) values",
        output_path="outputs/figures/log2_cpm_histogram.png"
    )

    print("✓ Step 6 finished: diagnostic histograms saved to outputs/figures/\n")

    # ------------------------------------------------------------------
    # Step 7 — Generate per-sample QC boxplots
    # ------------------------------------------------------------------
    print("Generating per-sample QC boxplots...")

    plot_sample_boxplots(
        log_matrix,
        "outputs/figures/boxplot_log2cpm_per_sample.png",
        "log2(CPM) distribution per sample"
    )

    print("✓ Step 7 finished: QC boxplots generated\n")

    # ------------------------------------------------------------------
    # Step 8 — Remove Low-variance genes
    # ------------------------------------------------------------------
    print("Filtering low-variance genes...")
    filtered_matrix = filter_low_variance_genes(log_matrix, min_variance=0.01)
    print("✓ Step 8 finished: low-variance genes removed\n")
    filtered_matrix.to_csv("outputs/matrices/log2_cpm_filtered_matrix.csv")

    # ------------------------------------------------------------------
    # Final preview (sanity check)
    # ------------------------------------------------------------------
    print("CPM-normalized matrix (preview):")
    print(cpm_matrix)

    print("\nLog2-transformed matrix (preview):")
    print(log_matrix)

if __name__ == "__main__":
    main()
