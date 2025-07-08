import pandas as pd

class DataLoader:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.df = None

    def load_data(self):
        """
        Load data from CSV and cache it in memory.
        """
        try:
            self.df = pd.read_csv(self.filepath)
            return self.df

        except Exception as e:
            print(f"File failed to load:{e}")


    def get_data(self):
        """
        Return the loaded DataFrame.
        """
        return self.load_data()


