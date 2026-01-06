import pandas as pd
import os
from sqlalchemy import create_engine
import urllib

# paths
DATA_DIR = "data/clean"
BOOKS_CSV = os.path.join(DATA_DIR, "books.csv")
APPEARANCES_CSV = os.path.join(DATA_DIR, "appearances.csv")

# Azure SQL setup
AZURE_SQL_SERVER = "placeholder_for_server.database.windows.net"
AZURE_SQL_DB = "nyttables"
AZURE_SQL_USER = "placeholder_for_username"
AZURE_SQL_PASSWORD = "placeholder_for_password"

# load cleaned csvs
books = pd.read_csv(BOOKS_CSV)
appearances = pd.read_csv(APPEARANCES_CSV)

# connect to Azure SQL
driver = "{ODBC Driver 18 for SQL Server}"

params = urllib.parse.quote_plus(
    f"DRIVER={driver};"
    f"SERVER={AZURE_SQL_SERVER};"
    f"DATABASE={AZURE_SQL_DB};"
    f"UID={AZURE_SQL_USER};"
    f"PWD={AZURE_SQL_PASSWORD};"
    f"Encrypt=yes;"
    f"TrustServerCertificate=no;"
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

# load data to Azure SQL
books.to_sql("books", engine, if_exists="replace", index=False)
appearances.to_sql("appearances", engine, if_exists="replace", index=False)

print("Data loaded to Azure SQL Database.")