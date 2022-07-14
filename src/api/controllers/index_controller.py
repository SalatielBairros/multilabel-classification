from fastapi import APIRouter

router = APIRouter(prefix="")

@router.get("/")
def get_index():
    return {"message": "Welcome to StackOverflow multilabel classification API"}
