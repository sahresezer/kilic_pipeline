rule all:
    input:
        "results/barcode77_summary.csv",
        "results/barcode77_length_dist.png",
        "results/barcode77_gc_dist.png",
        "results/barcode77_quality_dist.png"

rule analyze_fastq:
    input:
        "data/barcode77.fastq"
    output:
        "results/barcode77_summary.csv"
    shell:
        "python scripts/calculate_stats.py {input} {output}"

rule generate_plots:
    input:
        "results/barcode77_summary.csv"
    output:
       "results/barcode77_length_dist.png",
        "results/barcode77_gc_dist.png",
        "results/barcode77_quality_dist.png"
    shell:
        "python scripts/plot_results.py {input}"