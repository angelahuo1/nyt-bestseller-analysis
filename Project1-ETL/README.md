# Project 1 – ETL Pipeline

This pipeline takes raw NYT Bestseller JSON files, normalizes them, and loads them into a relational database. This database is explored with SQL queries, and will be further analyzed in Project 2.

## Scripts

### extract_json.py
- Reads raw JSON files from `data/raw/`.

### transform_json.py
- Flattens nested JSON structures and splits into:
  - `books.csv`
  - `appearances.csv`

### load_to_sqlite.py
- Cleans fields, removes duplicates, assigns IDs  
- Saved to `data/clean/`
- Loads both tables into `db/nyt_books.db`  
- Final merged dataset: `data/analysis/bestsellers_analysis_ready.csv`

## SQL
Exploratory SQL queries in `sql/exploratory_queries.sql`. See `sql/sql_queries_results.ipynb` for easier visualization of queries.