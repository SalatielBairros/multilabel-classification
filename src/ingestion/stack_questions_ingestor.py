import requests
import logging
from os import environ as env, path
from environment.constants import EnvironmentVariables

class StackOverflowQuestionsIngestor:
    def __init__(self):
        self.base_path = env[EnvironmentVariables.local_storage_path]
        self.original_path = f'{self.base_path}/original'

    def ingest(self) -> str:
        filename = 'stackoverflow_perguntas.csv'
        if(self.__has_ingested_file__(filename)):
            return

        logging.info("Ingesting questions from Stack Overflow...")
        request = requests.get(f'https://raw.githubusercontent.com/alura-cursos/alura_classificacao_multilabel/master/dataset/{filename}')
        if(request.status_code == 200):
            content = request.text
            self.__save_file__(filename, content)
            del content
            logging.info("Questions from Stack Overflow were successfully ingested.")
        else:
            logging.error(f"An error occurred while ingesting questions: {request.status_code}")

        return f'{self.original_path}/{filename}'

    def __has_ingested_file__(self, filename: str):
        return path.exists(f'{self.original_path}/{filename}')

    def __save_file__(self, filename: str, content: str):
        with open(f'{self.original_path}/{filename}', 'w') as file:
            file.write(content)            
