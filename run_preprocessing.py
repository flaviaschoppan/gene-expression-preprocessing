from pipeline.io import load_counts
from pipeline.normalization import cpm 
from pipeline.transform import log2_transform
from pipeline.plots import plot_histogram


def main():
    print("Loading raw counts...")
    counts = load_counts("data/raw/counts.csv")
    print("✓ Step 1: Raw counts loaded\n")

    print("Applying CPM normalization...")
    cpm_matrix = cpm(counts)
    print("✓ Step 2 finished: CPM normalization applied\n")

    print("Applying log2 transformation...")
    log_matrix = log2_transform(cpm_matrix)
    print("✓ Step 3 finished: log2 transformation applied\n")    

    print ("Saving processed matrices...")
    cpm_matrix.to_csv("outputs/matrices/cpm_matrix.csv")
    log_matrix.to_csv("outputs/matrices/log2_cpm_matrix.csv")
    print("✓ Step 4 finished: matrices saved to outputs/matrices/\n")  


    print("CPM-normalized matrix (preview):")
    print(cpm_matrix)

    print("Log2-transformed matrix (preview):")
    print(log_matrix)

    print("Generating diagnostic plots...")

    plot_histogram(
        cpm_matrix,
        title="Distribution of CPM values",
        output_path="outputs/figures/cpm_histogram.png"
    )

    plot_histogram(
        log_matrix,
        title="Distribuition of log2(COM + 1) values",
        output_path="outputs/figures/log2_cpm_histogram.png"
    )
    

    print("✓ Step 5 finished: diagnostic plots saved to outputs/figures/\n")


if __name__ == "__main__":
    main()
