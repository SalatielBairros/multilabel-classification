from fastapi import APIRouter
from api.request.prediction_request import PredictionRequest
from models.multilabel_logistic import MultilabelLogisticRegression

router = APIRouter(prefix="/logistic")
model = MultilabelLogisticRegression()

@router.post("/predict")
def predict_text(request: PredictionRequest):
    return model.load_model().predict(request.text)

@router.get("/evaluation")
def predict_text():
    return model.evaluate_model()    
