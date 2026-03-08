import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_results(csv_file, output_prefix):
    print("Reading data and calculating statistics...\n")
    df = pd.read_csv(csv_file)

    print("--- SUMMARY STATISTICS ---")
    for col in ["length", "gc_content", "mean_quality"]:
        mean_val = df[col].mean()       
        median_val = df[col].median()   
        print(f"{col.upper()} (Column):")
        print(f"  - Mean   : {mean_val:.2f}")
        print(f"  - Median : {median_val:.2f}\n")
    print("--------------------------\n")

    print("Generating plots, please wait...")
    sns.set_theme(style="whitegrid")
    
    # ---------------------------------------------------------
    # Plot A: Read Length Distribution 
    # ---------------------------------------------------------
    plt.figure(figsize=(10, 6))
    
    # Trim the top 1% extreme outliers to focus on the main distribution
    upper_limit = df["length"].quantile(0.99) 
    clean_data = df[df["length"] <= upper_limit]
    
    sns.histplot(clean_data["length"], bins=50, kde=True, color="blue")
    plt.title("Read Length Distribution")
    plt.xlabel("Read Length (Base Pairs)")
    plt.ylabel("Frequency (Number of Reads)")
    plt.savefig(f"{output_prefix}_length_dist.png") 
    plt.close() 

    # Plot B: GC Content (%)
    plt.figure(figsize=(10, 6))
    sns.histplot(df["gc_content"], bins=30, kde=True, color="green")
    plt.title("GC Content Distribution")
    plt.xlabel("GC Content (%)")
    plt.ylabel("Frequency (Number of Reads)")
    plt.savefig(f"{output_prefix}_gc_dist.png")
    plt.close()

    # Plot C: Mean Read Quality Score
    plt.figure(figsize=(8, 6))
    sns.violinplot(y=df["mean_quality"], color="orange")
    plt.title("Mean Read Quality Score Distribution")
    plt.ylabel("Phred Quality Score (Q)")
    plt.savefig(f"{output_prefix}_quality_dist.png")
    plt.close()

    print(f"Process finished! Plots have been saved to the results directory with the prefix '{output_prefix}'.")

if __name__ == "__main__":
    input_csv = "results/barcode77_summary.csv"
    output_images = "results/plot"
    visualize_results(input_csv, output_images)