# Fashion Trend & Price Comparison Dashboard

An interactive data tool that shows which well-known fashion brands are most popular and trending in each clothing category, and how their prices compare.

**Status:** In progress. The data foundation and the category chart are working. The product breakdown table is next.

## How it works

Pick a category (e.g. sneakers, jeans, jackets) from the dropdown and the dashboard shows:

- **Chart:** brands ordered left to right by score (most popular on the left). Bar height is the average price of each brand's top 3 products, and bar color shows average rating (darker blue = higher rated). Hover over a bar to see avg price, avg rating, and total reviews.
- **Table (coming next):** the same top 3 products per brand (Brand, Product, Price, Rating), so the chart and table always match

### Ranking rules

1. Remove products rated below 3.75
2. Rank the remaining products by review count within each brand and category
3. Keep the top 3 per brand (fewer if a brand has fewer qualifying products)
4. **Score** = total reviews of those top 3 products
5. **Price** = average price of those same 3 products

## Tech stack

Python, pandas, SQLAlchemy, SQLite, Streamlit, Plotly

## Roadmap

- [x] **Phase 1: Data foundation:** load a sample dataset and apply the ranking rules
- [ ] **Phase 1.5: Basic interface:** category dropdown and bar chart (done), breakdown table (to do)
- [ ] **Phase 2: Cleaning:** brand name matching and data quality checks
- [ ] **Phase 3: Live data:** daily scheduled pull from one API source with a rolling 30-day window
- [ ] **Phase 4: Second dataset:** kept separate first, then combined into one popularity and trend score

## Project structure

```
data/                    sample data (CSV) and the SQLite database
scripts/
  transform_load.py      cleans the sample data and loads it into the database
  load_data.py           load_products(): reads the products table (swap this for an API later)
  ranking.py             get_top3(df): filters and ranks products
  brand_summary.py       get_brand_summary(top3): score, avg rating, avg price per brand and category
  brand_plot.py          Streamlit page with the dropdown and bar chart
```

Each file does one job and passes a table to the next, so changing the data source later only means editing `load_data.py`.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Build the database (it isn't stored in the repo):

```bash
python scripts/transform_load.py
```

Run the dashboard from the project root:

```bash
streamlit run scripts/brand_plot.py
```