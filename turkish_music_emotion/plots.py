from pathlib import Path
from loguru import logger
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from turkish_music_emotion.config import FIGURES_DIR

class PlotHandler:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def save_plot(self, filename: str, show: bool = False):
        if not filename.endswith('.png'):
            filename += '.png'
        output_path = FIGURES_DIR / filename
        
        plt.savefig(output_path, bbox_inches='tight')
        logger.success(f"Plot saved successfully to {output_path}")
        if show:
            plt.show()
        plt.close()

    def plot_hist(self, column: str, bins: int = 30, save: bool = False, filename: str = "histogram.png"):
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data[column], bins=bins, kde=True)
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        
        if save:
            self.save_plot(filename)

    def plot_corr_matrix(self, save: bool = False, filename: str = "correlation_matrix.png"):
        plt.figure(figsize=(12, 8))
        numeric_data = self.data.select_dtypes(include='number')
        correlation_matrix = numeric_data.corr()
        sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', square=True)
        plt.title('Correlation Matrix')
        
        if save:
            self.save_plot(filename)

    def plot_boxplot(self, column: str, save: bool = False, filename: str = "boxplot.png"):
        plt.figure(figsize=(10, 6))
        sns.boxplot(y=self.data[column])
        plt.title(f'Boxplot of {column}')
        
        if save:
            self.save_plot(filename)
