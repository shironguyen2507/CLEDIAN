import os
import sys
from pathlib import Path
import joblib

from ml.preprocess import clean_text

BASE_DIR = Path(__file__).resolve().parent.parent

# Ưu tiên ENV, nếu không có thì fallback về local path
MODEL_PATH = os.getenv(
    "MODEL_PATH",
    str(BASE_DIR / "models" / "cledian_nb_model.pkl")
)

VECTORIZER_PATH = os.getenv(
    "VECTORIZER_PATH",
    str(BASE_DIR / "models" / "vectorizer.pkl")
)

print("📦 MODEL_PATH =", MODEL_PATH)
print("📦 VECTORIZER_PATH =", VECTORIZER_PATH)

_model = None
_vectorizer = None


def load_model():
    global _model, _vectorizer
    if _model is None or _vectorizer is None:
        print("🔄 Loading model...")
        
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
        if not os.path.exists(VECTORIZER_PATH):
            raise FileNotFoundError(f"Vectorizer file not found: {VECTORIZER_PATH}")

        _model = joblib.load(MODEL_PATH)
        _vectorizer = joblib.load(VECTORIZER_PATH)
        print("✅ Model loaded")


def predict(text: str):
    load_model()
    clean = clean_text(text)
    X = _vectorizer.transform([clean])
    probs = _model.predict_proba(X)[0]
    idx = probs.argmax()
    label = _model.classes_[idx]
    confidence = float(probs[idx])
    return label, confidence
