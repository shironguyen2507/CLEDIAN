from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.schemas import PredictRequest, PredictResponse
from api.service import predict
import logging


app = FastAPI(title="CLEDIAN API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictResponse)
def predict_api(req: PredictRequest):
    label, conf = predict(req.text)
    return {"label": label, "confidence": conf}

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)