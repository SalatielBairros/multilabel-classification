import pandas as pd

class LocalStorageRepository:
    def __init__(self):
        pass

    def get_original_data(self):
        return pd.read_csv('data/original/stackoverflow_perguntas.csv')

    def save_processed_data(self, dataset: pd.DataFrame):
        dataset.to_csv('data/processed/stackoverflow_perguntas_processed.csv', index=False)

    def load_processed_data(self):
        return pd.read_csv('data/processed/stackoverflow_perguntas_processed.csv')