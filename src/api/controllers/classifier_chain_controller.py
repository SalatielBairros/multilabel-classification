from fastapi import APIRouter
from api.request.prediction_request import PredictionRequest
from models.classifier_chain import MultilabelClassifierChain

router = APIRouter(prefix="/classifier-chain")
model = MultilabelClassifierChain()

@router.post("/predict")
def predict_text(request: PredictionRequest):
    return model.load_model().predict(request.text)

@router.get("/evaluation")
def predict_text():
    return model.evaluate_model()    
