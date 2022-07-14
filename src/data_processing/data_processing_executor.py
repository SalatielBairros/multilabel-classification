import pandas as pd
from repository.local_storage_repository import LocalStorageRepository
from utils.data_transformation_command_handler import DataTransformationCommandHandler
from data_processing.labels_to_columns import LabelsToColumns
from data_processing.tags_whitespace_strip import TagsWhitespaceStrip
from os import path
import logging

def execute_feature_engineering(force:bool=False) -> pd.DataFrame:
    if(force or not path.exists('./data/processed/stackoverflow_perguntas_processed.csv')):
        return DataTransformationCommandHandler() \
            .add_command(TagsWhitespaceStrip) \
            .add_command(LabelsToColumns) \
            .execute()
    else:
        logging.info('Loading prepared data from local storage')
        return LocalStorageRepository().load_processed_data()