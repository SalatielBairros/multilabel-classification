import pandas as pd
from utils.data_transformation_command_handler import DataTransformationCommandHandler
from data_processing.labels_to_columns import LabelsToColumns
from data_processing.tags_whitespace_strip import TagsWhitespaceStrip

def execute_feature_engineering() -> pd.DataFrame:
    return DataTransformationCommandHandler() \
        .add_command(TagsWhitespaceStrip) \
        .add_command(LabelsToColumns) \
        .execute()