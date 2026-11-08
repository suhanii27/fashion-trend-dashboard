from ranking import get_top3

def get_brand_summary(top3):
    return (
    top3.groupby(["brand", "category"]).agg(
        score=("review_count", "sum"),
        avg_rating=("rating", "mean"),
        avg_price=("price", "mean")
    )
    .round(2)
    .reset_index()
    .sort_values(["score", "avg_rating"], ascending=False)
)

if __name__ == "__main__": 
    from load_data import load_products
    print(get_brand_summary(get_top3(load_products())))