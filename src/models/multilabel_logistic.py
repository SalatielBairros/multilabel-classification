import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import hamming_loss
import joblib
from ingestion.stack_questions_ingestor import StackOverflowQuestionsIngestor
from os import path
import logging
from data_processing.data_processing_executor import execute_feature_engineering

class MultilabelLogisticRegression:
    def __init__(self, train_data: pd.DataFrame = None, text_column: str = 'Perguntas', labels_column: str = 'all_tags', labels_names: list[str] = None):
        if(train_data is None):
            self.train_data = self.__load_data__()
        self.train_data = train_data
        self.text_column = text_column
        self.labels_column = labels_column
        self.model = None
        self.model_file_path = './data/models/multilabel_logistic_regression.joblib'
        if(labels_names is None):
            self.labels_names = ['node.js', 'jquery', 'html', 'angular']
        else:
            self.labels_names = labels_names

    def __load_data__(self) -> pd.DataFrame:
        ingestor = StackOverflowQuestionsIngestor()
        ingestor.ingest()        
        execute_feature_engineering()

    def __get_vectorizer__(self) -> TfidfVectorizer:
        vet = TfidfVectorizer(max_features=5000, max_df=0.85)
        vet.fit(self.train_data[self.text_column])
        return vet

    def __get_model__(self) -> OneVsRestClassifier:
        lr = LogisticRegression()
        model = OneVsRestClassifier(lr)
        return model

    def __get_labels__(self, label_data) -> list[list[int]]:
        if(len(label_data) == 0):
            raise Exception('Empty label column')

        first = label_data.iloc[0]
        if(type(first) is tuple):
            return [list(y) for y in label_data]
        elif(type(first) is str):
            return [list(eval(y)) for y in label_data]

        raise Exception('Invalid label column')

    def __train__(self) -> OneVsRestClassifier:
        labels = self.__get_labels__(self.train_data[self.labels_column])
        vectorizer = self.__get_vectorizer__()
        model = self.__get_model__()
        model.fit(vectorizer.transform(self.train_data[self.text_column]), labels)
        self.model = model
        return model
    
    def __save_model__(self):
        if(self.model is not None):
            joblib.dump(self.model, self.model_file_path)

    def load_model(self):
        if(path.exists(self.model_file_path)):
            self.model = joblib.load(self.model_file_path)
            logging.info('Using model from file')
        else:
            logging.info('Training model')
            self.__train__()
            self.__save_model__()
        return self

    def predict(self, text: str) -> dict:
        if(self.model is None):
            raise Exception('Model not trained')

        vectorizer = self.__get_vectorizer__()
        vector = vectorizer.transform([text])
        predictions = self.model.predict(vector)
        return [{self.labels_names[i]: prediction[i] for i in range(len(self.labels_names))} for prediction in predictions]

    def evaluate_model(self):
        x_train, x_test, y_train, y_test = train_test_split(
            self.train_data[self.text_column], self.train_data[self.labels_column], test_size=0.2, random_state=42)    

        vectorizer = self.__get_vectorizer__()
        x_train_tfidf = vectorizer.transform(x_train)
        x_test_tfidf = vectorizer.transform(x_test)

        y_train = self.__get_labels__(y_train)
        y_test = self.__get_labels__(y_test)

        model = self.__get_model__()
        model.fit(x_train_tfidf, y_train)
        predictions = model.predict(x_test_tfidf)

        dummy_score = 1 / len(self.train_data[self.labels_column].unique())
        exact_match_accuracy = model.score(x_test_tfidf, y_test)
        hamming_loss_score = hamming_loss(y_test, predictions)
        return {
            'exact_match_accuracy': exact_match_accuracy,
            'dummy_score': dummy_score,
            'hamming_loss': hamming_loss_score,
        }