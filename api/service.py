from pathlib import Path
import sys
import joblib
import os

MODEL_PATH = os.getenv("MODEL_PATH")
VECTORIZER_PATH = os.getenv("VECTORIZER_PATH")

BASE_DIR = Path(__file__).resolve().parent.parent

if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))

from ml.preprocess import clean_text

MODEL_PATH = BASE_DIR / "models" / "cledian_nb_model.pkl"
VEC_PATH = BASE_DIR / "models" / "vectorizer.pkl"

_model = None
_vectorizer = None

def load_model():
    global _model, _vectorizer
    if _model is None or _vectorizer is None:
        print("🔄 Loading model...")
        _model = joblib.load(MODEL_PATH)
        _vectorizer = joblib.load(VEC_PATH)
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
