import pandas as pd
from Bio import SeqIO

def analyze_fastq(input_file, output_file):
    results = []
    print(f"Good news: File '{input_file}' found successfully. Starting analysis...\n")
    
    # Initialize a counter for the number of processed reads
    read_count = 0

    # Parse the FASTQ file line by line using SeqIO
    for record in SeqIO.parse(input_file, "fastq"):
        
        # 1. Read Length
        length = len(record.seq)
        
        # 2. GC Content (%)
        g_count = record.seq.count("G")
        c_count = record.seq.count("C")
        gc_content = (g_count + c_count) / length * 100
        
        # 3. Mean Quality Score
        qualities = record.letter_annotations["phred_quality"]
        mean_quality = sum(qualities) / len(qualities)
        
        results.append({
            "read_id": record.id,
            "length": length,
            "gc_content": round(gc_content, 2),
            "mean_quality": round(mean_quality, 2)
        })
        
        read_count += 1

    # Convert the data into a tabular format (CSV) and save it
    df = pd.DataFrame(results)
    df.to_csv(output_file, index=False)
    
    print(f"Analysis complete! Processed a total of {read_count} DNA reads.")
    print(f"The report prepared for Professor Kılıç has been saved to: {output_file}")

if __name__ == "__main__":
    # ATTENTION: Reading the new real data instead of the old test file
    input_fastq = "data/barcode77.fastq"
    output_csv = "results/barcode77_summary.csv"
    
    analyze_fastq(input_fastq, output_csv)