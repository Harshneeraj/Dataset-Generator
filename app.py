from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
import os
import random
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

app = FastAPI()

# Authentication dependency
def authenticate(api_key: str):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return True

# Define a data model (modify this for your dataset structure)
class DataItem(BaseModel):
    id: int
    name: str
    value: float

class DatasetResponse(BaseModel):
    dataset: list[DataItem]

@app.get("/generate-dataset", response_model=DatasetResponse)
def generate_dataset(api_key: str = Depends(authenticate), size: int = 10):
    """Endpoint that generates a dataset with `size` records."""
    dataset = [
        {
            "id": i,
            "name": f"Item-{i}",
            "value": round(random.uniform(10, 100), 2)
        }
        for i in range(1, size + 1)
    ]
    return {"dataset": dataset}
