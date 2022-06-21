from environment.env_configuration import prepare_environment
from ingestion.stack_questions_ingestor import StackOverflowQuestionsIngestor

prepare_environment()

ingestor = StackOverflowQuestionsIngestor()
ingestor.ingest()