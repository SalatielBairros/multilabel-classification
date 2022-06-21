import logging
from os import environ as env, path
from environment.constants import EnvironmentVariables
import wget

class StackOverflowQuestionsIngestor:
    def __init__(self):
        self.base_path = env[EnvironmentVariables.local_storage_path]
        self.original_path = f'{self.base_path}/original'

    def ingest(self) -> str:
        filename = 'stackoverflow_perguntas.csv'
        if(self.__has_ingested_file__(filename)):
            return

        logging.info("Ingesting questions from Stack Overflow...")
        return wget.download(f'https://raw.githubusercontent.com/alura-cursos/alura_classificacao_multilabel/master/dataset/{filename}', self.original_path)        

    def __has_ingested_file__(self, filename: str):
        return path.exists(f'{self.original_path}/{filename}')   
