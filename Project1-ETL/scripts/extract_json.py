import requests
import pandas as pd
from datetime import datetime, timedelta
import time
import os
import json

# config
API_KEY = "YOUR_NYT_API"
LIST_NAME = "hardcover-fiction"

# set date range
start_date = datetime(2018, 1, 7)
today = datetime.today()

days_ago_to_sunday = (today.weekday() + 1) % 7  
end_date = today - timedelta(days=days_ago_to_sunday)

# fetch data
rows = []
date = end_date

while date >= start_date:
    # construct URL
    date_str = date.strftime("%Y-%m-%d")
    url = f"https://api.nytimes.com/svc/books/v3/lists/{date_str}/{LIST_NAME}.json"
    params = {"api-key": API_KEY}

    # make request
    response = requests.get(url, params=params)

    # avoid hitting rate limits (5 requests per minute)
    time.sleep(12)

    if response.status_code == 200:
        data = response.json()

        # save JSON to file
        os.makedirs("data/raw", exist_ok=True)
        json_path = f"data/raw/{date_str}.json"
        with open(json_path, "w") as f:
            json.dump(data, f, indent=2)

        # extract book data
        if "results" in data and data["results"]:
            for book in data["results"]["books"]:
                rows.append({
                    "list_date": date_str,
                    "rank": book.get("rank"),
                    "title": book.get("title"),
                    "author": book.get("author"),
                    "publisher": book.get("publisher"),
                    "description": book.get("description"),
                    "weeks_on_list": book.get("weeks_on_list"),
                    "isbn10": book.get("primary_isbn10"),
                    "isbn13": book.get("primary_isbn13"),
                })
            print(f"Pulled data for {date_str}.")
        else:
            print(f"Missing data for {date_str}.")

    else:
        print(f"Request failed for {date_str}: {response.status_code}")

    # move back one week
    date -= timedelta(days=7)
