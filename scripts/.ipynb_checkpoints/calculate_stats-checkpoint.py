import pandas as pd
from Bio import SeqIO

def analyze_fastq(input_file, output_file):
    results = []

    # SeqIO library automatically parses the FASTQ file line by line
    for record in SeqIO.parse(input_file, "fastq"):
        
        # 1. Read Length: Total number of bases in the DNA sequence
        length = len(record.seq)
        
        # 2. GC Content: Count G and C bases, divide by total length, and multiply by 100 (%)
        g_count = record.seq.count("G")
        c_count = record.seq.count("C")
        gc_content = (g_count + c_count) / length * 100
        
        # 3. Mean Quality Score: Convert quality symbols to numerical values and calculate the average
        qualities = record.letter_annotations["phred_quality"]
        mean_quality = sum(qualities) / len(qualities)
        
        # Append all calculated values to our list
        results.append({
            "read_id": record.id,
            "length": length,
            "gc_content": round(gc_content, 2),
            "mean_quality": round(mean_quality, 2)
        })

    # Convert the collected data into an organized tabular format (CSV) using Pandas and save it
    df = pd.DataFrame(results)
    df.to_csv(output_file, index=False)
    print("Analysis complete! Results have been saved.")

# This block runs when the script is executed directly
if __name__ == "__main__":
    analyze_fastq("data/barcode77.fastq", "results/stats_summary.csv")