from os import environ as env, path
import json
import logging
from environment.constants import EnvironmentVariables
import pandas as pd

def configure_environment_from_file(file_path = './appsettings.json'):
    if(path.exists(file_path)):
        logging.info('Configurating environment from file...\n')
        with open(file_path) as file:
            configurations = json.load(file)
            env[EnvironmentVariables.data_repository_type] = configurations[EnvironmentVariables.data_repository_type]            
            env[EnvironmentVariables.cache_expiration] = configurations[EnvironmentVariables.cache_expiration]
            env[EnvironmentVariables.local_storage_path] = configurations[EnvironmentVariables.local_storage_path]

def configurate_logging():
    logging.basicConfig(format="%(asctime)s: %(message)s",
                        level=logging.INFO, 
                        datefmt="%H:%M:%S")
    logging.info('Logging configurated')

def configure_pandas():
    pd.set_option('mode.chained_assignment', None)

def prepare_environment():
    configurate_logging()    
    configure_environment_from_file()    
    configure_pandas()