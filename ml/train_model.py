import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
from pathlib import Path
from preprocess import clean_text

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "datasets" / "processed" / "cledian_dataset_v1.csv"
MODEL_DIR = BASE_DIR / "models"

def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    if df.empty:
        raise ValueError("Dataset is empty. Please rebuild dataset first.")

    df["text"] = df["text"].astype(str).apply(clean_text)

    X_train, X_test, y_train, y_test = train_test_split(
        df["text"], df["label"], test_size=0.2, random_state=42
    )

    vectorizer = TfidfVectorizer(ngram_range=(1,2), max_features=20000)
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model = MultinomialNB()
    model.fit(X_train_vec, y_train)

    preds = model.predict(X_test_vec)
    print(classification_report(y_test, preds))

    MODEL_DIR.mkdir(exist_ok=True)
    joblib.dump(model, MODEL_DIR / "cledian_nb_model.pkl")
    joblib.dump(vectorizer, MODEL_DIR / "vectorizer.pkl")

    print("✅ Model saved to models/")

if __name__ == "__main__":
    main()
