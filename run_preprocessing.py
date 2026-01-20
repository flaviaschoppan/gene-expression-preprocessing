from pipeline.io import load_counts
from pipeline.normalization import cpm 
from pipeline.transform import log2_transform


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

    print("CPM-normalized matrix (preview):")
    print(cpm_matrix)

    print("Log2-transformed matrix (preview):")
    print(log_matrix)


if __name__ == "__main__":
    main()
