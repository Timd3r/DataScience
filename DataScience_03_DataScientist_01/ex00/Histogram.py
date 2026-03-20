import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

def load_numeric_data(path):
    """Loads CSV and returns only numeric columns."""
    try:
        data = pd.read_csv(path)
        return data.select_dtypes(include=['number'])
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def setup_grid(n_features, n_cols=5):
    """Calculates rows and creates the figure and axes."""
    n_rows = math.ceil(n_features / n_cols)
    fig, axs = plt.subplots(n_rows, n_cols, figsize=(20, n_rows * 3.5))
    return fig, axs.flatten(), n_rows

def plot_histograms(data, axs_flat, bins=40):
    """Plots a histogram on each axis with specific styling."""
    cols = data.columns
    for i, column in enumerate(cols):
        sns.histplot(
            data[column], 
            bins=bins,
            color='#7dbf7d',     
            edgecolor='white',   
            linewidth=0.5,
            label='Knight',      
            ax=axs_flat[i]
        )
        
        axs_flat[i].set_title(column, fontsize=12, fontweight='bold')
        axs_flat[i].set_xlabel('')
        axs_flat[i].set_ylabel('')
        axs_flat[i].legend(loc='upper right', fontsize=8)
    
    for j in range(i + 1, len(axs_flat)):
        axs_flat[j].axis('off')

def save_and_close(fig, filename='knight_stats_histograms.png'):
    """Finalizes layout, saves the image, and closes the figure."""
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close(fig)
    print(f"Success! Plot saved as {filename}")

def main():
    FILE_PATH = 'DataScience_03_DataScientist_01/Test_knight.csv'
    OUTPUT_NAME = 'knight_stats_histograms.png'
    BINS = 40
    
    data = load_numeric_data(FILE_PATH)
    if data is not None:
        fig, axs_flat, _ = setup_grid(len(data.columns))
        plot_histograms(data, axs_flat, bins=BINS)
        save_and_close(fig, OUTPUT_NAME)

if __name__ == "__main__":
    main()