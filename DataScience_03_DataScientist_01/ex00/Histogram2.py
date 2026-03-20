import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

def load_data(path):
    """Loads CSV and keeps the 'knight' label for filtering."""
    try:
        return pd.read_csv(path)
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def setup_grid(n_features, n_cols=5):
    """Calculates rows and creates the figure and axes."""
    n_rows = math.ceil(n_features / n_cols)
    fig, axs = plt.subplots(n_rows, n_cols, figsize=(20, n_rows * 3.5))
    return fig, axs.flatten()

def plot_dual_histograms(jedi_data, sith_data, axs_flat, bins=20):
    """Plots overlapping histograms for Jedi and Sith."""
    # We only plot columns that are numeric in both
    cols = jedi_data.select_dtypes(include=['number']).columns
    
    for i, column in enumerate(cols):
        # Plot Jedi (Green)
        sns.histplot(
            jedi_data[column], bins=bins, color='#7dbf7d', label='Jedi',
            alpha=0.6, edgecolor='white', linewidth=0.5, ax=axs_flat[i]
        )
        
        # Plot Sith (Red/Crimson)
        sns.histplot(
            sith_data[column], bins=bins, color='#e63946', label='Sith',
            alpha=0.6, edgecolor='white', linewidth=0.5, ax=axs_flat[i]
        )
        
        # Styling
        axs_flat[i].set_title(column, fontsize=12, fontweight='bold')
        axs_flat[i].set_xlabel('')
        axs_flat[i].set_ylabel('')
        axs_flat[i].legend(loc='upper right', fontsize=8)
    
    # Hide empty subplots
    for j in range(i + 1, len(axs_flat)):
        axs_flat[j].axis('off')

def save_and_close(fig, filename):
    """Finalizes layout, saves the image, and closes the figure."""
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close(fig)
    print(f"Success! Comparison plot saved as {filename}")

def main():
    FILE_PATH = 'DataScience_03_DataScientist_01/Train_knight.csv'
    OUTPUT_NAME = 'jedi_vs_sith_histograms.png'
    
    full_data = load_data(FILE_PATH)
    
    if full_data is not None:
        # Separate the groups
        jedi = full_data[full_data['knight'] == 'Jedi']
        sith = full_data[full_data['knight'] == 'Sith']
        
        # Get numeric columns (excluding the 'knight' label itself)
        numeric_cols = full_data.select_dtypes(include=['number']).columns
        
        fig, axs_flat = setup_grid(len(numeric_cols))
        plot_dual_histograms(jedi, sith, axs_flat, bins=35)
        save_and_close(fig, OUTPUT_NAME)

if __name__ == "__main__":
    main()