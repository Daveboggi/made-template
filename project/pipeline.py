import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy


def getDataFromExcel(url_to_Excel_Data, excel_sheet_name):
    df = pd.read_excel(url_to_Excel_Data, excel_sheet_name, index_col=None)
    return df


def drop_Column(df: pd.DataFrame, constraint):
    df = df.drop(columns=constraint)
    return df



def pipeline():
    climate_data = 'https://www.umweltbundesamt.de/sites/default/files/medien/361/dokumente/2021_03_10_trendtabellen_thg_nach_sektoren_v1.0.xlsx'
    vehicle_registrations_germany = 'https://www.kba.de/SharedDocs/Downloads/DE/Statistik/Fahrzeuge/FZ14/fz14_2022.xlsx?__blob=publicationFile&v=4'
    climate_data_muenster = 'https://opendata.stadt-muenster.de/sites/default/files/Muenster-CO2-Emissionen_2021.xls'
    vehicle_registrations_muenster = 'https://opendata.stadt-muenster.de/sites/default/files/Fahrzeugbestand-Regierungsbezirk-Muenster-2018-2022.xlsx'

    #Using Open Datasets to analyze Correlations
    df = pd.read_excel(climate_data, 'CO2')
    df2 = pd.read_excel(vehicle_registrations_germany, 'FZ 14.2.1')
    df3 = pd.read_excel(climate_data_muenster, 'CO2 Emissionen (Sektoren)')
    df4 = pd.read_excel(vehicle_registrations_muenster, 'PKW')

   
    #Operations for climate data in germany

    #Column operations
    df = drop_Column(df, [f'REF.{i}' for i in range(1, 24)])
    df = drop_Column(df,["REF"])
    df = df.rename(columns={f'REF.{i}':f'{i-10+2000}' for i in range (24,30)})
    df = df.rename(columns={'Vorjahr':'2020'})
    df = drop_Column(df,["Unnamed: 0"])
    df = drop_Column(df,[f'Unnamed: {i}' for i in range(34, 37)])
    df = df.dropna(how='all')
    df = df.rename(columns={'Unnamed: 1': 'Sector'})
    df = df.rename(columns={'Unnamed: 2': 'Sum'})
    #Row operations
    df = df.drop(index=df.index[0:6])
    df = df.drop(index=df.index[31:])
    df = df[~df['Sector'].str.startswith('CRF')]
    print(df)


    
    #Operations for vehicle registration data in germany
    df2 = drop_Column(df2, [f'Unnamed: {i}' for i in range(8, 11)])
    df2 = drop_Column(df2, ["Unnamed: 0"])
    #df2 = df2.dropna()
    df2 = df2.rename(columns={'Unnamed: 1' : 'Year'})
    df2 = df2.rename(columns={'Unnamed: 2' : 'Benzin'})
    df2 = df2.rename(columns={'Unnamed: 3' : 'Diesel'})
    df2 = df2.rename(columns={'Unnamed: 4' : 'Gas (LPG)'})
    df2 = df2.rename(columns={'Unnamed: 5' : 'Gas (CNG)'})
    df2 = df2.rename(columns={'Unnamed: 6' : 'Elektro'})
    df2 = df2.rename(columns={'Unnamed: 7' : 'Hybrid'})
    df2 = df2.drop(index= df2.index[0:17])
    df2 = df2.drop(index= df2.index[9:16])



    #Operations for climate data in muenster

    df3 = df3.drop(index= df3.index[0:5])
    df3 = df3.rename(columns={'CO2-Emissionen nach Sektoren in (t)': 'Years'})
    df3 = df3.rename(columns={'Private Haushalte': 'Haushalte'})
    df3 = df3.rename(columns={'Gewerbe + Sonstiges': 'Gewerbe'})


    #Operations for vehicle registration data in muenster

    df4 = drop_Column(df4,["Regierungsbezirk"])
    print(df4.columns)
    df4 = df4.rename(columns={'Statistische Kennziffer und Zulassungsbezirk\n': 'Statistische Kennziffer und Zulassungsbezirk'})
    df4 = df4.rename(columns={'Nach Kraftstoffarten': 'Benzin'})
    df4 = df4.rename(columns={'Unnamed: 5': 'Diesel'})
    df4 = df4.rename(columns={'Unnamed: 6': 'Gas'})
    df4 = df4.rename(columns={'Unnamed: 7': 'Hybrid'})
    df4 = drop_Column(df4,["Unnamed: 8"])
    df4 = df4.rename(columns={'Unnamed: 9': 'Elektro'})
    df4 = df4.drop(0)
    idx = df4.columns.get_loc('Unnamed: 10')
    df4 = df4.iloc[:, :idx]
    df4['Jahr'] = df4['Jahr'].ffill()
    df4 = df4[df4['Statistische Kennziffer und Zulassungsbezirk'] == "GESAMT"]
    
    

    #Writing dfs to new csv
    df.to_csv('./data/climate_data_germany.csv', sep='\t', encoding='utf-8')
    df2.to_csv('./data/vehicle_registrations_germany.csv', sep='\t', encoding='utf-8')
    df3.to_csv('./data/climate_data_muenster.csv', sep='\t', encoding='utf-8')
    df4.to_csv('./data/vehicle_registrations_muenster.csv', sep='\t', encoding='utf-8')



pipeline()