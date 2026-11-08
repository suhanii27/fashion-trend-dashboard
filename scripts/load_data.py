import pandas as pd
from sqlalchemy import create_engine

def load_products():
    engine = create_engine("sqlite:///data/product.db")
    return pd.read_sql("SELECT * FROM products", engine)