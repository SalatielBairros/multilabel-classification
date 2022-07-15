from environment.env_configuration import prepare_environment
from ingestion.stack_questions_ingestor import StackOverflowQuestionsIngestor
from data_processing.data_processing_executor import execute_feature_engineering
from models.classifier_chain import MultilabelClassifierChain
from models.multilabel_logistic import MultilabelLogisticRegression
from models.mlknn_model import MlKnnModel

prepare_environment()

ingestor = StackOverflowQuestionsIngestor()
ingestor.ingest()

df = execute_feature_engineering()

# model = MultilabelLogisticRegression(train_data=df)
# predictions = model.load_model().predict("I don't know how to use angular with jquery")
# print(predictions)

# score = model.evaluate_model()
# print(score)

# model = MultilabelClassifierChain(train_data=df)
# predictions = model.load_model().predict("I don't know how to use angular with jquery")
# print(predictions)

# score = model.evaluate_model()
# print(score)

model = MlKnnModel(train_data=df)
predictions = model.load_model().predict("I don't know how to use angular with jquery")
print(predictions)

score = model.evaluate_model()
print(score)