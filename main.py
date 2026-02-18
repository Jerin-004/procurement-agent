from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = InferenceClient(
    provider="hf-inference",
    api_key=os.getenv("HF_TOKEN"),
)


suppliers = [
    {
        "name": "ElectroMax Pvt Ltd",
        "description": "low cost electronic components microcontrollers sensors fast delivery",
        "price": 95,
        "rating": 4.4
    },
    {
        "name": "IndustrialPro Suppliers",
        "description": "premium industrial hardware heavy duty tools durable materials",
        "price": 160,
        "rating": 4.8
    },
    {
        "name": "BulkTech Distributors",
        "description": "bulk electronics distributor affordable wholesale pricing",
        "price": 85,
        "rating": 4.3
    }
]


class Request(BaseModel):
    query: str


@app.post("/recommend")
def recommend_supplier(request: Request):

    descriptions = [s["description"] for s in suppliers]

    result = client.sentence_similarity(
        request.query,
        descriptions,
        model="sentence-transformers/all-MiniLM-L6-v2",
    )

    best_index = result.index(max(result))

    return suppliers[best_index]
