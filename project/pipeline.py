import pandas as pd
#from sqlalchemy import create_engine

#Defining Data urls
#Climate Dataset
climate_data = 'https://www.umweltbundesamt.de/sites/default/files/medien/361/dokumente/2021_03_10_trendtabellen_thg_nach_sektoren_v1.0.xlsx'
cars_with_alternate_drive = 'https://www.kba.de/SharedDocs/Downloads/DE/Statistik/Fahrzeuge/FZ14/fz14_2022.xlsx?__blob=publicationFile&v=4'

#Using Open Datasets to analyze Correlations
df = pd.read_excel(climate_data, 'CO2')
df2 = pd.read_excel(cars_with_alternate_drive, 'FZ 14.2.1')


#sqlite_file_path = '/data/cars_with_alternate_drive.sqlite'

#engine = create_engine(f'sqlite:///{sqlite_file_path}')

#df.to_sql('cars_with_alternate_drive', engine, index=False, if_exists='replace')

#engine.dispose()
df.to_csv('./data/climate_data.csv', sep='\t', encoding='utf-8')
df2.to_csv('./data/cars_with_alternative_drive_data.csv', sep='\t', encoding='utf-8')
