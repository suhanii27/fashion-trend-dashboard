import pandas as pd

df = pd.read_csv("data/sample_products.csv")
print(df.head()) # only shows how much we see on screen, default 5, still affects all
print(len(df), "rows")

# Data checks
print("Missing values:")
print(df.isnull().sum())

print("Bad prices:", (df["price"] <= 0).sum())
print("Bad ratings:", ((df["rating"] < 1) | (df["rating"] > 5)).sum())
print("Bad review counts:", (df["review_count"] < 0).sum())
print("Duplicate rows:", df.duplicated().sum())

# Clean
for col in ["brand", "category", "product"]:
    df[col] = df[col].str.strip()
df["category"] = df["category"].str.lower()
df = df.drop_duplicates()

# Load
from sqlalchemy import create_engine

engine = create_engine("sqlite:///data/product.db")
df.to_sql("products", engine, if_exists="replace", index=False)
print("Loaded", len(df), "rows into products")