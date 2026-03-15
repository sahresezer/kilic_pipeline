import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

def config_plot(title, xlabel, ylabel):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

def draw_histplot(df, column, color, title, xlabel, ylabel, output_path, bins=50):
    plt.figure(figsize=(12, 7))
    
    if column == "length":
        upper_limit = df[column].quantile(0.99)
        data_to_plot = df[df[column] <= upper_limit][column]
        plt.xlim(0, upper_limit)
    else:
        data_to_plot = df[column]

    sns.histplot(data_to_plot, bins=bins, kde=True, color=color, edgecolor='black', alpha=0.7)
    config_plot(title, xlabel, ylabel)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300) 
    plt.close()

def draw_violinplot(df, column, color, title, xlabel, ylabel, output_path):
    plt.figure(figsize=(12, 5))
    sns.violinplot(x=df[column], color=color, inner="quartile") 
    config_plot(title, xlabel, ylabel)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()

def visualize_results(input_csv, output_prefix):

    try:
        df = pd.read_csv(input_csv)
    except FileNotFoundError:
        print(f"Error: Could not find {input_csv}")
        sys.exit(1)

 
    print("\n--- SUMMARY STATISTICS ---")
    for col in ["length", "gc_content", "mean_quality"]:
        if col in df.columns:
            print(f"{col.upper()} (Column):")
            print(f"  - Mean   : {df[col].mean():.2f}")
            print(f"  - Median : {df[col].median():.2f}\n")
    print("--------------------------\n")

    print("Generating plots, please wait...")
    
    draw_histplot(df, "length", "blue", "Read Length Distribution", "Read Length (bp)", "Frequency (Number of Reads)", f"{output_prefix}_length_dist.png")
    
    draw_histplot(df, "gc_content", "green", "GC Content Distribution", "GC Content (%)", "Frequency (Number of Reads)", f"{output_prefix}_gc_dist.png")
    
    draw_violinplot(df, "mean_quality", "orange", "Mean Quality Score Distribution", "Mean Phred Quality Score", "Density", f"{output_prefix}_quality_dist.png")

    print(f"Process finished! Plots have been saved with the prefix '{output_prefix}'.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/plot_results.py <input.csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_prefix = input_file.replace("_summary.csv", "")

    visualize_results(input_file, output_prefix)

if __name__ == "__main__":
    main()