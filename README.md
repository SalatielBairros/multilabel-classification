# Multilabel classification

This material is based on this [Alura course](https://cursos.alura.com.br/course/classificacao-multilabel-nlp).

The material from course is implemented using Jupyter Notebooks, but here I implement a variation using only python and a different project structure. The goal is to classificate Stack Overflow questions using a multilabel classification model.

The data-source can be obtained [here](https://raw.githubusercontent.com/alura-cursos/alura_classificacao_multilabel/master/dataset/stackoverflow_perguntas.csv). 

## Dependencies

```    
pip install pandas 
pip install numpy 
pip install fastapi
pip install requests
pip install sklearn
pip install joblib
pip install pydantic
pip install "uvicorn[standard]"
pip install scikit-multilearn
```

## Running de Code

There is two ways to run the code: (1) running the recommendations on the console and (2) using a FastAPI server.

(1)
```bash
python console_main.py
```

(2)
```bash
uvicorn main:app --reload
```

> The `reload` option is used to reload the code when it changes and should be used only when developing.

For te API, the Documentation can be found at [http://localhost:8000/docs](http://localhost:8000/docs).

## Controllers and endpoints

All controllers have two endpoints:
1. `/predict`: used to predict the labels of a question.
2. `/evaluation`: used to evaluate the model.

### logistic
Classification using Binary Relevante (`OneVsRestClassifier`) with Logistic Regression.

### mlknn
Classification using the Multilabel K-Nearest Neighbors (`MLKNN`). This algorithm is from the [scikit-multilearn](https://scikit-multilearn.readthedocs.io/en/latest/index.html) library, but because the last release is out of date with the last version of scikit-learn, the code from scikit-multilearn repository is copied here.

### classifier-chain
Classification using the Classifier Chain (`ClassifierChain`) with Logistic Regression.