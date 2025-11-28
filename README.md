# NYT Bestsellers Data Engineering & NLP Analysis

A two-part portfolio project combining data engineering, analytics engineering, and NLP to uncover patterns New York Times Bestseller lists from 2018-2025.

# Folder Structure
nyt-bestsellers-analysis/
- README.md
- requirements.txt
- data/
    - raw/
    - clean/
    - results/
    - analysis/
- db/
    - nyt_books.db
- Project1-ETL/
    - README.md
    - scripts/
        - extract_json.py
        - load_to_sqlite.py
        - transform_json.py
    - sql/
        - exploratory_queries.sql
        - sql_queries_results.ipynb
- Project2-Analysis/
    - README.md
    - notebooks/
        - 01_etl.ipynb
        - 02_analysis.ipynb


## Project 1 – ETL Pipeline
- Extract raw NYT bestseller JSON files  
- Normalize nested data into structured tables  
- Clean and dedupe books + appearances  
- Load into a SQLite database  
- Export an analysis-ready dataset:
  - `data/analysis/bestsellers_analysis_ready.csv`

## Project 2 – Exploratory & NLP Analysis
- Exploratory data analysis (categories, authors, rankings)
- Text cleaning & lemmatization
- Word frequency analysis + wordclouds
- TF–IDF modeling
- Topic modeling (LDA)
- Sentiment analysis (VADER)
- Outputs stored in:
  - `data/results/`
  
## Tech Stack
- Python, pandas, numpy
- SQLite3
- scikit-learn
- NLTK
- matplotlib

