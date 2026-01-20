from pipeline.io import load_counts

def main():
    print("Loading raw counts...")

    counts = load_counts("data/raw/counts.csv")

    print("✓ Step 1: Raw counts loaded\n")
    print("Counts matrix:")
    print(counts)


if __name__ == "__main__":
    main()
