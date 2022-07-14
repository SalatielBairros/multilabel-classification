from pydantic import BaseModel

class PredictionRequest(BaseModel):
    """
    Prediction request model
    """
    text: str