import streamlit as st
import plotly.express as px
from load_data import load_products
from ranking import get_top3
from brand_summary import get_brand_summary

top3 = get_top3(load_products())
summary = get_brand_summary(top3)

st.title("Fashion Trend & Price Comparison")

category = st.selectbox("Fashion piece", sorted(summary["category"].unique()))
cat_summary = summary[summary["category"] == category].sort_values("score", ascending=False)

fig = px.bar(
    cat_summary,
    x="brand",
    y="avg_price",
    color="avg_rating",
    color_continuous_scale="Blues",
    category_orders={"brand": cat_summary["brand"].tolist()},
    hover_data={"brand": False, "avg_price": ":.2f", "avg_rating": ":.2f", "score": True},
    labels={"brand": "Brand", "avg_price": "Avg price ($)", "avg_rating": "Avg rating", "score": "Total reviews"},
    title="Brands ordered by popularity (most reviews on the left)",
)
st.plotly_chart(fig, use_container_width=True)