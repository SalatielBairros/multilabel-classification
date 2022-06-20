# Multilabel classification

This material is based on this [Alura course](https://cursos.alura.com.br/course/classificacao-multilabel-nlp).

The material from course is implemented using Jupyter Notebooks, but here I implement a variation using only python and a different project structure. The goal is to classificate Stack Overflow questions using a multilabel classification model.

The data-source can be obtained [here](https://raw.githubusercontent.com/alura-cursos/alura_classificacao_multilabel/master/dataset/stackoverflow_perguntas.csv). 

## Dependencies

- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [requests](https://requests.readthedocs.io/)
- [fastAPI](https://fastapi.tiangolo.com/)

    ```bash
    pip install pandas 
    pip install numpy 
    pip install fastapi
    pip install requests
    pip install "uvicorn[standard]"
    ```

## Running de Code

There is two ways to run the code: (1) running the recommendations on the console and (2) using a FastAPI server.

(1)
```bash
python main.py
```

(2)
```bash
uvicorn main:app --reload
```

> The `reload` option is used to reload the code when it changes and should be used only when developing.

For te API, the Documentation can be found at [http://localhost:8000/docs](http://localhost:8000/docs).