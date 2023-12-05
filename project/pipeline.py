import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy


def getDataFromExcel(url_to_Excel_Data, excel_sheet_name):
    df = pd.read_excel(url_to_Excel_Data, excel_sheet_name)
    return df


def drop_Column(df: pd.DataFrame, constraint):
    df = df.drop(columns=constraint)
    return df



def pipeline():
    climate_data = 'https://www.umweltbundesamt.de/sites/default/files/medien/361/dokumente/2021_03_10_trendtabellen_thg_nach_sektoren_v1.0.xlsx'
    cars_with_alternate_drive = 'https://www.kba.de/SharedDocs/Downloads/DE/Statistik/Fahrzeuge/FZ14/fz14_2022.xlsx?__blob=publicationFile&v=4'

    #Using Open Datasets to analyze Correlations
    df = pd.read_excel(climate_data, 'CO2')
    df2 = pd.read_excel(cars_with_alternate_drive, 'FZ 14.2.1')

    #Operations for Climate Data

    #Column operations
    df = drop_Column(df, [f'REF.{i}' for i in range(1, 24)])
    df = drop_Column(df,["REF"])
    df = drop_Column(df,["Unnamed: 0"])
    df = drop_Column(df,[f'Unnamed: {i}' for i in range(34, 37)])
    df = df.dropna(how='all')
    #Row operations
    df = df.drop(index=df.index[0:6])
    df = df.drop(index=df.index[31:])


    #Operations for Cars with alternative driving
    df2 = drop_Column(df2, [f'Unnamed: {i}' for i in range(8, 11)])
    df2 = drop_Column(df2, ["Unnamed: 0"])
    df2 = df2.dropna()

    #Writing dfs to new csv
    df.to_csv('./data/climate_data.csv', sep='\t', encoding='utf-8')
    df2.to_csv('./data/cars_with_alternative_drive_data.csv', sep='\t', encoding='utf-8')


pipeline()