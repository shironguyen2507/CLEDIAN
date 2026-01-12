import pandas as pd
import joblib
from sklearn.metrics import classification_report
from preprocess import clean_text

MODEL_PATH = "../models/cledian_nb_model.pkl"
VEC_PATH = "../models/vectorizer.pkl"
DATA_PATH = "../datasets/split/test.csv"

def main():
    df = pd.read_csv(DATA_PATH)
    df["text"] = df["text"].astype(str).apply(clean_text)

    model = joblib.load(MODEL_PATH)
    vec = joblib.load(VEC_PATH)

    X = vec.transform(df["text"])
    y = df["label"]

    preds = model.predict(X)
    print(classification_report(y, preds))

if __name__ == "__main__":
    main()
