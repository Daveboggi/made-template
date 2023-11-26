import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy
import re


def is_valid_ifopt(value):
    pattern = r'^[A-Za-z]{2}:\d+:\d+(?::\d+)?$'
    return bool(re.match(pattern, str(value)))



# Download the CSV data
csv_url = "https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"
df = pd.read_csv(csv_url, delimiter=";")


# Drop the "Status" column
df = df.drop(columns=["Status"])

#Drop rows with invalid Verkehr
df = df[df["Verkehr"].isin(["FV", "RV", "nur DPN"])]

# Check for NaN values
df = df.dropna()

# Filter rows with valid coordinates
#df = df[(df["Laenge"].between(-90, 90)) & (df["Breite"].between(-90, 90))]



df = df[df["IFOPT"].apply(is_valid_ifopt)]
df.to_csv('ex2.csv', sep='\t', encoding='utf-8')


# Create SQLite database using SQLAlchemy
engine = create_engine("sqlite:///trainstops.sqlite")

dtype={
    "EVA_NR": sqlalchemy.BIGINT,
    "DS100": sqlalchemy.TEXT,
    "IFOPT": sqlalchemy.TEXT,
    "NAME": sqlalchemy.TEXT,
    "Verkehr": sqlalchemy.TEXT,
    "Laenge": sqlalchemy.TEXT,
    "Breite": sqlalchemy.TEXT,
    "Betreiber_Name": sqlalchemy.TEXT,
    "Betreiber_Nr": sqlalchemy.BIGINT
}


# Write the DataFrame to the SQLite database
df.to_sql("trainstops", engine, index=False, if_exists="replace", dtype=dtype)

