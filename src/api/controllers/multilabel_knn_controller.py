from fastapi import APIRouter
from api.request.prediction_request import PredictionRequest
from models.mlknn_model import MlKnnModel

router = APIRouter(prefix="/mlknn")
model = MlKnnModel()

@router.post("/predict")
def predict_text(request: PredictionRequest):
    return model.load_model().predict(request.text)

@router.get("/evaluation")
def predict_text():
    return model.evaluate_model()    
