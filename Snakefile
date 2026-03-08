rule all:
    input:
        "results/barcode77_summary.csv",
        "results/plot_length_dist.png"

rule calculate_qc:
    input:
        "data/barcode77.fastq"
    output:
        "results/barcode77_summary.csv"
    shell:
        "python scripts/calculate_stats.py"

rule plot_qc:
    input:
        "results/barcode77_summary.csv"
    output:
        "results/plot_length_dist.png",
        "results/plot_gc_dist.png",
        "results/plot_quality_dist.png"
    shell:
        "python scripts/plot_results.py"