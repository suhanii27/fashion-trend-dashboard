import pandas as pd
from sqlalchemy import create_engine
engine = create_engine("sqlite:///data/product.db")

df = pd.read_sql("SELECT * FROM products", engine)
filtered = df[df["rating"] >= 3.75]
ranked = filtered.copy()
ranked["rank"] = ranked.groupby(["brand", "category"])["review_count"].rank(method="first", ascending = False) # false means the biggest value gets rank 1
top3 = ranked[ranked["rank"] <= 3]
scores = top3.groupby(["brand", "category"])["review_count"].sum() # review count to rank for popularity (x-axis)
scores = scores.sort_values(ascending=False)
avg_ratings = top3.groupby(["brand", "category"])["rating"].mean().round(2) # in
avg_prices = top3.groupby(["brand", "category"])["price"].mean().round(2)

# check if it works
print(top3)
print(scores)
print(avg_ratings)
print(avg_prices)