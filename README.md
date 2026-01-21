# Gene Expression Preprocessing Pipeline

## Overview

This repository implements a minimal, explicit, and reproducible preprocessing workflow for gene expression matrices before any multivariate analysis (e.g. PCA, clustering).

The goal of this project is to formalize the numerical conditioning and quality inspection steps of expression data, making them explicit instead of implicit or ad-hoc. The focus is not on biological interpretation, but on making the numerical structure of the data stable, inspectable, and suitable for downstream analyses.

This project represents a real and unavoidable stage of any serious transcriptomics pipeline.

---

## What this pipeline does

1. Loads a raw gene expression count matrix  
2. Normalizes counts to CPM (Counts Per Million)  
3. Applies log2(x + 1) transformation  
4. Saves processed matrices as pipeline artifacts  
5. Generates global diagnostic histograms  
6. Generates per-sample QC boxplots  
7. Applies a simple low-variance gene filter  

---

## Why this matters

Raw gene expression matrices are numerically ill-conditioned and unsuitable for distance-based or variance-based analyses:

- They are highly skewed  
- A few highly expressed genes dominate scale and variance  
- Most values are compressed near zero  
- Distances and variances become mathematically unstable  

This preprocessing step exists in virtually every serious transcriptomics workflow, but is often implicit, manual, or poorly documented.

This project formalizes this stage as an explicit, reproducible, and inspectable pipeline.

---

## What this project is NOT

- This is not a differential expression analysis  
- This is not a biological interpretation pipeline  
- This is not a PCA or clustering workflow  

It is strictly a numerical conditioning, normalization, transformation, and quality inspection stage.

---

## Conceptual focus

> "Raw results are not scientific results. They must be structured, conditioned, and inspected before interpretation."

This project focuses on the geometry and numerical structure of the data, not on biological conclusions.

---

## Project structure

```text
gene-expression-preprocessing/
├── data/
│   └── raw/
│       └── counts.csv
├── pipeline/
│   ├── __init__.py
│   ├── io.py
│   ├── normalization.py
│   ├── transform.py
│   └── plots.py
├── outputs/
│   ├── matrices/
│   └── figures/
├── run_preprocessing.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Outputs

The pipeline produces the following versionable artifacts:

```text
outputs/matrices/cpm_matrix.csv
outputs/matrices/log2_cpm_matrix.csv
outputs/matrices/log2_cpm_filtered_matrix.csv

outputs/figures/cpm_histogram.png
outputs/figures/log2_cpm_histogram.png
outputs/figures/boxplot_log2cpm_per_sample.png
```

---

## How to run

1. Install dependencies:

```text pip install -r requirements.txt```

2. Run the pipeline:

```text python run_preprocessing.py```

All outputs will be written to the ```text outputs/``` folder.

---

## Reproducibility

All steps in this pipeline are:
- Explicit
- Deterministic
- Scripted
- And produce versionable artifacts

This repository is designed as a didactic and structural example of a real preprocessing stage in gene expression analysis pipelines.

---

## Data note

The data used in this repository are synthetic and intended solely to demonstrate the numerical behavior of the pipeline and the structure of the workflow.

---

## License

This project is released under the MIT License.