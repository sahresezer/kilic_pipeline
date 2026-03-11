# KILIÇ BIOINFORMATICS ANALYSIS PIPELINE

> **Quality Control Pipeline for Long-Read Sequencing Developed for Prof. Dr. Kılıç's Laboratory**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Snakemake](https://img.shields.io/badge/Snakemake-7.0+-green.svg)](https://snakemake.readthedocs.io/)
[![BioPython](https://img.shields.io/badge/BioPython-1.79+-orange.svg)](https://biopython.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Project Summary

This project is an automated and reproducible bioinformatics pipeline developed for quality control (QC) of long-read sequencing data. It analyzes raw data in FASTQ format to calculate and visualize basic metrics such as read length, GC content, and quality scores.

**Key Features:**
- ✅ Fully automated workflow management (Snakemake)
- ✅ FASTQ file analysis (length, GC content, quality scores)
- ✅ Statistical summary and visualization
- ✅ Outlier filtering
- ✅ Reproducible conda environment

## Project Structure

kilic_pipeline/
├── data/                          # Raw data files
│   └── barcode77.fastq           # FASTQ file to be analyzed
├── results/                       # Analysis results
│   ├── barcode77_summary.csv     # Detailed statistics
│   ├── plot_length_dist.png      # Length distribution plot
│   ├── plot_gc_dist.png          # GC content distribution plot
│   ├── plot_quality_dist.png     # Quality score distribution plot
│   └── stats_summary.csv         # Summary statistics
├── scripts/                       # Python analysis scripts
│   ├── calculate_stats.py        # FASTQ analysis
│   └── plot_results.py           # Visualization
├── Snakefile                      # Snakemake workflow definition
├── environment.yml               # Conda environment definition
├── .gitignore                    # Git ignore rules
└── README.md                     # This file


##  Technologies Used

### Core Technologies
- **Python 3.8+**: Main programming language
- **Snakemake**: Workflow management and automation
- **Conda**: Package management and environment isolation

### Scientific Libraries
- **BioPython**: FASTQ file processing and biological data analysis
- **Pandas**: Data manipulation and CSV operations
- **NumPy**: Numerical computations
- **Matplotlib**: Graph creation
- **Seaborn**: Statistical visualization


## Analysis Metrics

The pipeline calculates the following metrics:

### 1. Read Length
- Length of each read in base pairs
- Distribution plot with outlier filtering

### 2. GC Content
- Percentage of Guanine and Cytosine nucleotides
- Critical metric for genomic signature analysis

### 3. Quality Score
- Phred quality score (Q = -10log₁₀(P))
- Q15+: Acceptable for long-read technologies
- Q20+: High-quality reads

## Installation and Running

### 1. Prerequisites
```bash
# Make sure conda is installed
conda --version

# If conda is not installed:
# macOS: brew install miniconda
# Linux: wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

### 2. Clone the Project
```bash
git clone https://github.com/sahresezer/kilic_pipeline.git
cd kilic_pipeline
```

### 3. Create Conda Environment
```bash
# Create the environment
conda env create -f environment.yml

# Activate the environment
conda activate bio_pipeline
```

### 4. Run the Pipeline
```bash
# Run the entire pipeline
snakemake --cores 1

# Or run specific rules
snakemake analyze_fastq
snakemake generate_plots
```

## Output Files

### barcode77_summary.csv
Detailed metrics for each read:
```csv
read_id,length,gc_content,mean_quality
ccd3b527-ffe8-49d5-b305-8899d5d3f2ba,206,54.85,20.63
f4713e2e-9e5b-4652-9d95-1ba4a4165c85,246,49.59,24.85
...
```

### Statistical Summary
```
--- SUMMARY STATISTICS ---
LENGTH (Column):
  - Mean   : 1038.24
  - Median : 547.00

GC_CONTENT (Column):
  - Mean   : 53.00
  - Median : 53.53

MEAN_QUALITY (Column):
  - Mean   : 17.90
  - Median : 17.31
```

### Visualizations
1. **Read Length Distribution**: Histogram of read lengths
2. **GC Content Distribution**: GC content distribution
3. **Quality Score Distribution**: Violin plot of quality scores


### Adding New Data
1. Place FASTQ file in the `data/` folder
2. Update input/output paths in `Snakefile`
3. Re-run the pipeline

## Workflow Description

### Snakemake Rules

1. **analyze_fastq**: Analyzes FASTQ file
   - Input: `data/barcode77.fastq`
   - Output: `results/barcode77_summary.csv`

2. **generate_plots**: Visualizes statistics
   - Input: `results/barcode77_summary.csv`
   - Output: PNG plot files

3. **all**: Produces all target files

## Troubleshooting

### Common Errors

**"ModuleNotFoundError"**
```bash
# Make sure conda environment is active
conda activate bio_pipeline

# Reinstall packages
conda env update -f environment.yml
```

**"FileNotFoundError"**
- Ensure data files are in correct locations
- Check relative paths

**Snakemake Error**
```bash
# Clear cache
snakemake --cleanup-metadata results/

# Run again
snakemake --forceall
```

## Quality Assessment

### Sample Results (Barcode77)
- **Total Read Count**: 81,012
- **Average Length**: 487.23 bp
- **GC Content**: 53.00% (average)
- **Quality Score**: 17.90 (average Phred)

### Quality Interpretation
**High Quality**: Q17.90, excellent for long-read technologies
**GC Balance**: 53%, aligned with genomic signatures
**Length Distribution**: Wide range, long-read advantage preserved

## Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Contact

**Developer**: Sahre Hilal Sezer
**Supervisor**: Prof. Dr. Kılıç
**Email**: [sahrehilalsezer@gmail.com](mailto:sahrehilalsezer@gmail.com)

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

**Last Updated**: March 2026
**Version**: 1.0.0