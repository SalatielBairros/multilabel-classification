import pandas as pd

class TagsWhitespaceStrip:
    """
    Class to strip tags and whitespace from the tag column
    """
    def __init__(self, dataset: pd.DataFrame):
        self.dataset = dataset

    def execute(self) -> pd.DataFrame:
        self.dataset['Tags'] = self.dataset['Tags'].str.strip()
        self.dataset['Tags'] = self.dataset['Tags'].str.replace('  ', ' ')
        return self.dataset
