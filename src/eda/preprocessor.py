import pandas as pd
import re
from typing import List

class ComplaintPreprocessor:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
    def map_product(product: str) -> str:
        product = product.lower()

        # CREDIT CARD
        if product in [
            "credit card",
            "credit card or prepaid card",
            "prepaid card"
        ]:
            return "Credit Card"

        # PERSONAL LOAN
        elif product in [
            "consumer loan",
            "payday loan, title loan, or personal loan",
            "payday loan, title loan, personal loan, or advance loan",
            "payday loan"
        ]:
            return "Personal Loan"

        # BNPL
        elif "buy now" in product:
            return "BNPL"

        # SAVINGS ACCOUNT
        elif product in [
            "checking or savings account",
            "bank account or service"
        ]:
            return "Savings Account"

        # MONEY TRANSFERS
        elif product in [
            "money transfers",
            "money transfer, virtual currency, or money service"
        ]:
            return "Money Transfers"

        # All others: discard
        else:
            return None

    def filter_by_product(self, allowed_patterns: List[str]) -> None:
        self.df["Product_Mapped"] = self.df["Product"].apply(self.map_product)
        self.df = self.df[self.df["Product_Mapped"].notna()]

    def remove_empty_narratives(self, min_words: int = 3) -> None:
        self.df = self.df[self.df['Consumer complaint narrative'].notna()]
        self.df = self.df[self.df['Consumer complaint narrative'].str.split().str.len() >= min_words]

    def clean_text(self, text: str) -> str:
        text = text.lower()
        text = re.sub(r"i am writing to (file|submit) a complaint", "", text)
        text = re.sub(r"[^a-zA-Z0-9\s\.\?]", " ", text)
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    def apply_cleaning(self) -> None:
        self.df['Consumer complaint narrative'] = self.df['Consumer complaint narrative'].apply(self.clean_text)

    def get_clean_data(self) -> pd.DataFrame:
        return self.df.copy()
