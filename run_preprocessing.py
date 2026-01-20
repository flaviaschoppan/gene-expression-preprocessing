from pipeline.io import load_counts
from pipeline.normalization import cpm 

def main():
    print("Loading raw counts...")
    counts = load_counts("data/raw/counts.csv")
    print("✓ Step 1: Raw counts loaded\n")

    print("Applying CPM normalization...")
    cpm_matrix = cpm(counts)
    print("✓ Step 2 finished: CPM normalization applied\n")

    print("CPM-normalized matrix (preview):")
    print(cpm_matrix)


if __name__ == "__main__":
    main()
