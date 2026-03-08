# Mini-Bioinformatics Pipeline & QC Reporting

This project provides an automated, reproducible Quality Control (QC) pipeline for long-read sequencing data, developed for Professor Kılıç's laboratory. 

## Workflow Logic & Tools
The pipeline takes raw FASTQ files as input and performs the following operations:
1. **Snakemake:** Acts as the workflow manager, ensuring reproducibility and sequential execution of tasks.
2. **Python (`calculate_stats.py`):** Parses raw reads to calculate Read Length, GC Content, and Mean Quality (Phred Scores) per read.
3. **Data Visualization (`plot_results.py`):** Uses Pandas and Seaborn to calculate summary statistics (mean, median) and generate distribution plots, strictly filtering out extreme outliers to ensure readability.
4. **Conda (`environment.yml`):** Isolates all dependencies to ensure the pipeline runs identically on any machine.

## How to Run the Pipeline
Execute the following commands in your terminal:

`# 1. Create and activate the environment`
`conda env create -f environment.yml`
`conda activate bio_pipeline`

`# 2. Run the automated pipeline via Snakemake`
`snakemake -c1`

---

## Communication: Email Draft to Professor Kılıç

**To:** Prof. Dr. Kılıç
**Subject:** QC Analysis Report and Recommendations for Long-Read Sequencing Data (Barcode77)

Dear Professor Kılıç,

I have successfully completed the initial Quality Control (QC) analysis on the raw long-read sequencing data (`barcode77.fastq`) you provided. I built an automated and reproducible pipeline to evaluate the health of the run before proceeding with the full alignment. 

You can find the visual distributions and the detailed summary matrix in the generated `results` directory. 

**Data Quality Summary:**
* **Mean Read Quality:** The overall mean Phred quality score is **17.90** (Median: 17.31). Since Q15 and above are generally considered successful for long-read technologies, the accuracy of our reads is highly satisfactory.
* **GC Content:** The mean GC content is **53.00%**. This closely aligns with expected genomic signatures, indicating no obvious signs of contamination.
* **Read Length Distribution:** While there are a few extreme outliers (which I filtered out in the visualization for clarity), the vast majority of the reads exhibit a distribution that perfectly captures the advantage of long-read sequencing.

**Recommendation:**
The data quality is robust, and there are no critical anomalies that would require us to discard the run. I strongly recommend that we proceed to the next step: Alignment to the reference genome.

Best regards,

Sahre Hilal Sezer