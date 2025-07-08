import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional

class ComplaintAnalyzer:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def plot_complaints_by_product(self) -> plt.Figure:
        """
        Plot number of complaints by product.
        """
        product_counts = self.df['Product'].value_counts()
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x=product_counts.index, y=product_counts.values, ax=ax)
        ax.set_title("Complaint Count by Product")
        ax.set_xlabel("Product")
        ax.set_ylabel("Number of Complaints")
        plt.xticks(rotation=45)
        plt.tight_layout()
        return fig

    def plot_narrative_lengths(self) -> plt.Figure:
        """
        Plot distribution of word counts in complaint narratives.
        """
        word_counts = self.df['Consumer complaint narrative'].dropna().str.split().str.len()
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(word_counts, bins=50, kde=True, ax=ax)
        ax.set_title("Distribution of Complaint Narrative Lengths")
        ax.set_xlabel("Word Count")
        ax.set_ylabel("Number of Complaints")
        plt.tight_layout()
        return fig

    def count_missing_narratives(self) -> int:
        """
        Return the number of complaints with missing or empty narratives.
        """
        return self.df['Consumer complaint narrative'].isna().sum()


    def get_summary_stats(self) -> pd.DataFrame:
        """
        Return a summary table (e.g., narrative length min/max/avg).
        """
        word_counts = self.df['Consumer complaint narrative'].dropna().str.split().str.len()
        summary = {
            "min_words": word_counts.min(),
            "max_words": word_counts.max(),
            "mean_words": word_counts.mean(),
            "median_words": word_counts.median(),
            "std_words": word_counts.std()
        }
        return pd.DataFrame([summary])