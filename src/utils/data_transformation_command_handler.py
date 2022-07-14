import logging
from repository.local_storage_repository import LocalStorageRepository
import pandas as pd

class DataTransformationCommandHandler:
    def __init__(self) -> None:
        self.commands = []
        self.data_repository = LocalStorageRepository()

    def add_command(self, command):
        self.commands.append(command)
        return self

    def execute(self) -> pd.DataFrame:
        dataset = self.__load_data__()
        for command in self.commands:
            command_instance = command(dataset)
            command_instance_should_execute = getattr(command_instance, "should_execute", None)
            if callable(command_instance_should_execute) and not command_instance_should_execute():
                continue
            logging.info(f"Executing command {command.__name__}")
            dataset = command_instance.execute()
        self.__save_data__(dataset)
        logging.info("Feature engineering finished")
        return dataset

    def __load_data__(self):
        dataset = self.data_repository.get_original_data()        
        return dataset

    def __save_data__(self, dataset: pd.DataFrame):
        self.data_repository.save_processed_data(dataset)        