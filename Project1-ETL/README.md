# Project 1 – ETL Pipeline

This pipeline ingests raw NYT Bestseller JSON files, normalizes them, and loads them into a relational database.

## Steps

### 1. Extract
- Reads raw JSON files from `data/raw/`.

### 2. Transform
- Flattens nested JSON structures
- Splits into:
  - `books.csv`
  - `appearances.csv`
- Cleans fields, removes duplicates, assigns IDs  
- Saved to `data/clean/`

### 3. Load
- Loads both tables into `db/nyt_books.db`  
- Creates indexes for performance  

### Output
- Clean datasets: `data/clean/`
- SQLite database: `db/nyt_books.db`
- Analysis-ready merged dataset:  
  `data/analysis/bestsellers_analysis_ready.csv`

## Scripts
Located in `scripts/`:
- `extract_json.py`
- `transform_json.py`
- `load_to_sqlite.py`

## SQL
Exploratory SQL queries in `sql/exploratory_queries.sql`.