import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
from ingestion.stack_questions_ingestor import StackOverflowQuestionsIngestor
from os import path

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

    def __get_vectorizer__(self) -> TfidfVectorizer:
        vet = TfidfVectorizer(max_features=5000, max_df=0.85)
        vet.fit(self.train_data[self.text_column])
        return vet

    def __get_model__(self) -> OneVsRestClassifier:
        lr = LogisticRegression()
        model = OneVsRestClassifier(lr)
        return model

    def __get_labels__(self, label_column) -> list[list[int]]:
        return [list(eval(y)) for y in label_column]

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
        else:
            self.__train__()
            self.__save_model__()
        return self

    def predict(self, text: str) -> dict:
        if(self.model is None):
            raise Exception('Model not trained')

        vectorizer = self.__get_vectorizer__()
        vector = vectorizer.transform([text])
        predictions = self.model.predict(vector)
        return {self.labels_names[i]: predictions[i] for i in range(len(self.labels_names))}

    def evaluate_model(self):
        x_train, x_test, y_train, y_test = train_test_split(
            self.train_data[self.text_column], self.train_data[self.labels_column], test_size=0.2, random_state=42)    

        vectorizer = self.__get_vectorizer__()
        x_train_tfidf = vectorizer.transform(x_train)
        x_test_tfidf = vectorizer.transform(x_test)

        y_train = [list(eval(y)) for y in y_train]
        y_test = [list(eval(y)) for y in y_test]

        model = self.__get_model__()
        model.fit(x_train_tfidf, y_train)
        return model.score(x_test_tfidf, y_test)