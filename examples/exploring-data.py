import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


excel_file_path = 'data/2023_03_15_em_entwicklung_in_d_ksg-sektoren_pm.xlsx'  # Replace with the path to your Excel file

# Specify the sheet name or sheet index
sheet_name = 'CO2'  # Replace with the name of the sheet you want to read

# Read the specified sheet into a Pandas DataFrame
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

print(df)

csv_path = 'data/neuzulassung_eauto.csv'
df2 = pd.read_csv(csv_path, delimiter='\t')

print(df2)
