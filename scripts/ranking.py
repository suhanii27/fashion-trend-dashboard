import pandas as pd
from sqlalchemy import create_engine
engine = create_engine("sqlite:///data/product.db")

def get_top3(df):
    filtered = df[df["rating"] >= 3.75]
    ranked = filtered.copy()
    ranked["rank"] = ranked.groupby(["brand", "category"])["review_count"].rank(method="first", ascending = False) # false means the biggest value gets rank 1
    top3 = ranked[ranked["rank"] <= 3]
    return top3

# check if it works
if __name__ == "__main__": #text value that assigns to name when a file is run directly
    from load_data import load_products
    print(get_top3(load_products()))