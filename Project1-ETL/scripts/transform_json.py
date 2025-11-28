import json
import os
import pandas as pd

# paths
RAW_DIR = "data/raw"
CLEAN_DIR = "data/clean"
os.makedirs(CLEAN_DIR, exist_ok=True)

book_rows = []
appearance_rows = []

# process raw JSON files
for filename in os.listdir(RAW_DIR):

    filepath = os.path.join(RAW_DIR, filename)
    # load JSON
    with open(filepath, "r") as f:
        data = json.load(f)
    # skip if no results
    if "results" not in data or not data["results"]:
        continue
    # extract list date
    list_date = data["results"]["published_date"]

    # extract book data
    for book in data["results"]["books"]:
        # book features table
        book_rows.append({
            "isbn13": book.get("primary_isbn13"),
            "isbn10": book.get("primary_isbn10"),
            "title": book.get("title"),
            "author": book.get("author"),
            "publisher": book.get("publisher"),
            "description": book.get("description"),
        })

        # weekly appearance table
        appearance_rows.append({
            "list_date": list_date,
            "isbn13": book.get("primary_isbn13"),
            "rank": book.get("rank"),
            "weeks_on_list": book.get("weeks_on_list")
        })

# convert to dataframes
books_df = pd.DataFrame(book_rows).drop_duplicates(subset="isbn13")
appear_df = pd.DataFrame(appearance_rows)

# save cleaned versions
books_df.to_csv(f"{CLEAN_DIR}/books.csv", index=False)
appear_df.to_csv(f"{CLEAN_DIR}/appearances.csv", index=False)

print("Saved as:")
print("  data/clean/books.csv")
print("  data/clean/appearances.csv")
