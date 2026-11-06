# Fashion Trend & Price Comparison Dashboard

An interactive data tool that shows which well-known fashion brands are most popular and trending in each clothing category, and how their prices compare.

**Status:** In progress. Currently building the data foundation (Phase 1).

## How it works

Pick a category (e.g. sneakers, jeans, jackets) and the dashboard shows:

- **Chart:** brands ranked left to right by score, with the average price of each brand's top 3 products on the y-axis
- **Table:** the same top 3 products per brand (Brand, Product, Price, Rating), so the chart and table always match

### Ranking rules

1. Remove products rated below 3.75
2. Rank the remaining products by review count within each brand
3. Keep the top 3 per brand (fewer if a brand has fewer qualifying products)
4. **Score** = total reviews of those top 3 products
5. **Price** = average price of those same 3 products

## Tech stack

Python, pandas, SQLAlchemy, SQLite, Streamlit, Plotly

## Roadmap

- [ ] **Phase 1: Data foundation:** load a sample dataset, build tables (products, brands, categories), apply the ranking rules
- [ ] **Phase 1.5: Basic interface:** category dropdown, bar chart, breakdown table
- [ ] **Phase 2: Cleaning:** brand name matching and data quality checks
- [ ] **Phase 3: Live data:** daily scheduled pull from one API source with a rolling 30-day window
- [ ] **Phase 4: Second dataset:** kept separate first, then combined into one popularity and trend score

## Project structure

```
data/       sample data
scripts/    transform and load scripts
app/        Streamlit dashboard (coming soon)
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```