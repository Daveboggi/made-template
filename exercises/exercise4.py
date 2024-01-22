import zipfile
import urllib.request
import pandas as pd
import sqlite3
import os
from pathlib import Path

# Step 1: Download and unzip data
url = "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip"
csv_file_name = "data.csv"

data_name = Path(url).stem
extract_path = os.path.join(os.curdir, data_name)
zip_name = data_name + '.zip'

# Download ZIP file
try:
    urllib.request.urlretrieve(url, zip_name)
except:
    print('Couldn\'t load zip from given url!')

# Unzip data.csv
with zipfile.ZipFile(zip_name, 'r') as zip_ref:
    zip_ref.extract(csv_file_name, '.')


# Read CSV file
try:
    df = pd.read_csv(os.path.join(csv_file_name),
                     sep=';',
                     index_col=False,
                     usecols=['Geraet', 'Hersteller', 'Model', 'Monat', 'Temperatur in °C (DWD)', 'Batterietemperatur in °C', 'Geraet aktiv'],
                     decimal=',')

    
    # Rename columns
    df = df.rename(columns={"Temperatur in °C (DWD)": "Temperatur", "Batterietemperatur in °C": "Batterietemperatur"})

    # Discard columns to the right of "Geraet aktiv"
    df = df.loc[:, :"Geraet aktiv"]

    # Step 3: Transform data
    # Convert temperatures to Fahrenheit
    df["Temperatur"] = (df["Temperatur"] * 9/5) + 32
    df["Batterietemperatur"] = (df["Batterietemperatur"] * 9/5) + 32

    # Step 4: Validate data
    # Example validation: Check if "Geraet" is an id over 0
    df = df[df["Geraet"] > 0]

    # Step 5: Write data into SQLite database
    db_path = "temperatures.sqlite"
    table_name = "temperatures"

    # Connect to SQLite database
    conn = sqlite3.connect(db_path)

    # Write DataFrame to SQLite
    df.to_sql(table_name, conn, index=False, if_exists='replace')

    # Close the connection
    conn.close()
    
except pd.errors.ParserError as e:
    # Print the error and handle as needed
    print(f"Error reading CSV: {e}")