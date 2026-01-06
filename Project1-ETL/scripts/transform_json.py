import json
import os
import pandas as pd
from azure.storage.blob import BlobServiceClient

# paths
RAW_DIR = "data/raw"
CLEAN_DIR = "data/clean"
os.makedirs(CLEAN_DIR, exist_ok=True)

# toggle option
USE_AZURE = True

#AZURE_CONNECTION_STRING = "AZURE_STORAGE_CONNECTION_STRING"
AZURE_CONNECTION_STRING = "placeholder_for_connection_string"
RAW_CONTAINER = "nyt-raw"
CLEAN_CONTAINER = "nyt-clean"

# Azure Blob setup
if USE_AZURE:
    blob_service_client = BlobServiceClient.from_connection_string(
        AZURE_CONNECTION_STRING
    )

    raw_container_client = blob_service_client.get_container_client(RAW_CONTAINER)
    clean_container_client = blob_service_client.get_container_client(CLEAN_CONTAINER)

    try:
        clean_container_client.create_container()
    except Exception:
        pass

book_rows = []
appearance_rows = []

if USE_AZURE:
    for blob in raw_container_client.list_blobs():
        # load JSON
        blob_client = raw_container_client.get_blob_client(blob.name)
        data = json.loads(blob_client.download_blob().readall())
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
# read from local if not using Azure
else:
    # process raw JSON files
    for filename in os.listdir(RAW_DIR):
        # load JSON
        with open(os.path.join(RAW_DIR, filename), "r") as f:
            data = json.load(f)
        # skip if no results
        if "results" not in data or not data["results"]:
            continue
        # extract list date
        list_date = data["results"]["published_date"]

        # extract book data
        for book in data["results"]["books"]:
            # book features tables
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

# save clean data locally 
books_df.to_csv(f"{CLEAN_DIR}/books.csv", index=False)
appear_df.to_csv(f"{CLEAN_DIR}/appearances.csv", index=False)
print("Saved locally as:")
print("  data/clean/books.csv")
print("  data/clean/appearances.csv")

# upload clean data to Azure Blob Storage
if USE_AZURE:
    clean_container_client.get_blob_client("books.csv").upload_blob(
        books_df.to_csv(index=False), overwrite=True
    )

    clean_container_client.get_blob_client("appearances.csv").upload_blob(
        appear_df.to_csv(index=False), overwrite=True
    )

    print("Uploaded cleaned csvs to Azure Blob Storage.")
