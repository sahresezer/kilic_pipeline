import sys
import os
import pandas as pd
from Bio import SeqIO

class FastqAnalyzer:
    def __init__(self, input_path):
        self.input_path = input_path
        self.results = []

    @staticmethod
    def get_gc_content(sequence):
        """Calculates the GC content percentage."""
        if not sequence:
            return 0.0
        g_count = sequence.count("G")
        c_count = sequence.count("C")
        return (g_count + c_count) / len(sequence) * 100.0

    @staticmethod
    def get_mean_quality(quality_scores):
        """Calculates the mean quality score."""
        if not quality_scores:
            return 0.0
        return sum(quality_scores) / len(quality_scores)

    def analyze(self):
        """Parses the FASTQ file and calculates metrics."""
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f"Error: {self.input_path} not found.")
        
        if os.path.getsize(self.input_path) == 0:
            raise ValueError("Error: Input FASTQ file is completely empty!")

        parsed_reads = list(SeqIO.parse(self.input_path, "fastq"))
        
        if not parsed_reads:
            raise ValueError("Error: No valid FASTQ data found in the file.")

        for record in parsed_reads:
            seq_len = len(record.seq)
            gc_val = self.get_gc_content(record.seq)
            q_scores = record.letter_annotations["phred_quality"]
            avg_q = self.get_mean_quality(q_scores)

            self.results.append({
                "read_id": record.id,
                "length": seq_len,
                "gc_content": gc_val,
                "mean_quality": avg_q
            })
        
        return pd.DataFrame(self.results)

def main():
    if len(sys.argv) < 3:
        print("Usage: python scripts/calculate_stats.py <input.fastq> <output.csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        analyzer = FastqAnalyzer(input_file)
        df = analyzer.analyze()
        
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        df.to_csv(output_file, index=False)
        print(f"Analysis successful. Output saved to: {output_file}")
    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()