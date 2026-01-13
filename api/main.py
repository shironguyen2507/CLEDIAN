from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from api.schemas import PredictRequest, PredictResponse
from api.service import predict
import traceback
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

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
    try:
        logger.info("🔎 Predict request received")
        label, conf = predict(req.text)
        return {"label": label, "confidence": conf}

    except Exception as e:
        logger.error("❌ ERROR in /predict: %s", e)
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Internal Server Error")
