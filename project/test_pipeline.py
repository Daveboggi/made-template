import numpy as np
import pandas as pd
import pytest
import pipeline as pipe
import pathlib
import csv

def test_get_datasources():
    #Arrange
    climate_data_url = 'https://www.umweltbundesamt.de/sites/default/files/medien/361/dokumente/2021_03_10_trendtabellen_thg_nach_sektoren_v1.0.xlsx'
    cars_with_alternate_drive_url = 'https://www.kba.de/SharedDocs/Downloads/DE/Statistik/Fahrzeuge/FZ14/fz14_2022.xlsx?__blob=publicationFile&v=4'

    #Act
    df = pipe.getDataFromExcel(climate_data_url, 'CO2') 
    df2 = pipe.getDataFromExcel(cars_with_alternate_drive_url, 'FZ 14.2.1')

    #Assert
    assert isinstance(df, pd.DataFrame)
    assert isinstance(df2, pd.DataFrame)


def test_execute_pipeline():
    #Arrange
    csv_file1 = pathlib.Path('./data/cars_with_alternative_drive_data.csv')
    csv_file2 = pathlib.Path('./data/climate_data.csv')

    #Act
    pipe.pipeline()

    
    # Assert that files exist
    assert csv_file1.exists(), f"File {csv_file1} does not exist."
    assert csv_file2.exists(), f"File {csv_file2} does not exist."


def test_pipeline_operations():
    #Arrange
    climate_data_url = 'https://www.umweltbundesamt.de/sites/default/files/medien/361/dokumente/2021_03_10_trendtabellen_thg_nach_sektoren_v1.0.xlsx'
    cars_with_alternate_drive_url = 'https://www.kba.de/SharedDocs/Downloads/DE/Statistik/Fahrzeuge/FZ14/fz14_2022.xlsx?__blob=publicationFile&v=4'

    #Act
    df = pipe.getDataFromExcel(climate_data_url, 'CO2') 
    df2 = pipe.getDataFromExcel(cars_with_alternate_drive_url, 'FZ 14.2.1')

    pipe.pipeline()

    df_new = pd.read_csv('./data/cars_with_alternative_drive_data.csv', header = None, delimiter="\t", quoting=csv.QUOTE_NONE, encoding='utf-8')
    df2_new = pd.read_csv('./data/climate_data.csv', header = None, delimiter="\t", quoting=csv.QUOTE_NONE, encoding='utf-8')
    
    #Assert
    assert df.equals(df_new) == False
    assert df2.equals(df2_new) == False

