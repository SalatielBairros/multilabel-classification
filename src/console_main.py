from environment.env_configuration import prepare_environment
from ingestion.stack_questions_ingestor import StackOverflowQuestionsIngestor
from data_processing.data_processing_executor import execute_feature_engineering
from models.multilabel_logistic import MultilabelLogisticRegression

prepare_environment()

ingestor = StackOverflowQuestionsIngestor()
ingestor.ingest()

df = execute_feature_engineering()

model = MultilabelLogisticRegression(train_data=df)
model.load_model().predict("I don't know how to use angular with jquery")
