# NYT Bestsellers Data Engineering & NLP Analysis

A two-part portfolio project combining data engineering, analytics engineering, and NLP to uncover patterns New York Times Bestseller lists from 2018-2025.

# Folder Structure

```text
nyt-bestsellers-analysis/
│
├── README.md  ← You are here
├── requirements.txt
│
├── data/
│   ├── raw/
│   ├── clean/
│   ├── analysis/
│   └── results/
│
├── db/
│   └── nyt_books.db
│
├── Project1-ETL/
│   ├── README.md
│   ├── scripts/
│   └── sql/
│
└── Project2-Analysis/
    ├── README.md
    ├── notebooks/
    └── results/
```

## Project 1 – ETL Pipeline
- Extract raw NYT bestseller JSON files  
- Organize nested data into structured tables  
- Clean books + appearances tables
- Load into a SQLite database  
- Export clean dataset:
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

