import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "datasets" / "raw"
OUT_FILE = BASE_DIR / "datasets" / "processed" / "cledian_dataset_v1.csv"

dfs = []

# fake news
fake_news = pd.read_csv(RAW_DIR / "fake_news.csv")
dfs.append(pd.DataFrame({
    "text": fake_news["post_message"],
    "label": fake_news["label"].apply(lambda x: "spam" if x == 1 else "ham")
}))

# manual spam
manual_spam = pd.read_csv(RAW_DIR / "manual_scam.csv")
dfs.append(pd.DataFrame({
    "text": manual_spam["text"],
    "label": ["spam"] * len(manual_spam)
}))

# manual safe
manual_safe = pd.read_csv(RAW_DIR / "manual_safe.csv")
dfs.append(pd.DataFrame({
    "text": manual_safe["text"],
    "label": ["ham"] * len(manual_safe)
}))

# vi spam
vi_spam = pd.read_csv(RAW_DIR / "vi_spam.csv")
text_col = "description" if "description" in vi_spam.columns else vi_spam.columns[0]
dfs.append(pd.DataFrame({
    "text": vi_spam[text_col],
    "label": ["spam"] * len(vi_spam)
}))

# vi_spam_post
vi_spam_post = pd.read_csv(RAW_DIR / "vi_spam_post.csv")
dfs.append(pd.DataFrame({
    "text": vi_spam_post["texts_vi"],
    "label": vi_spam_post["labels"]
}))

# manual urls
with open(RAW_DIR / "manual_urls.txt", "r") as f:
    urls = f.read().splitlines()

full = pd.concat(dfs).dropna()
OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
full.to_csv(OUT_FILE, index=False, encoding="utf-8-sig")

print("✅ Dataset created:", OUT_FILE)
print("Total samples:", len(full))
