import sqlite3
import pandas as pd
import os

# paths
DATA_DIR = "data/clean"
DB_PATH = "db/nyt_books.db"
BOOKS_CSV = os.path.join(DATA_DIR, "books.csv")
APPEARANCES_CSV = os.path.join(DATA_DIR, "appearances.csv")

# load cleaned csvs
books = pd.read_csv(BOOKS_CSV)
appearances = pd.read_csv(APPEARANCES_CSV)

# connect to sqlite
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# create tables
cur.execute("""
    CREATE TABLE IF NOT EXISTS books (
        isbn13 TEXT PRIMARY KEY,
        title TEXT,
        author TEXT,
        publisher TEXT,
        description TEXT
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS appearances (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        isbn13 TEXT,
        list_date TEXT,
        rank INTEGER,
        weeks_on_list INTEGER,
        FOREIGN KEY(isbn13) REFERENCES books(isbn13)
    );
""")

conn.commit()

# insert data
books.to_sql("books", conn, if_exists="replace", index=False)
appearances.to_sql("appearances", conn, if_exists="replace", index=False)

conn.commit()

print("\nSQLite load completed. Database saved as nyt_books.db.")
