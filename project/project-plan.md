# Project Plan

## Title
<!-- Give your project a short title. -->
Analyzing the impact of electric vehicles to the co2 value in germany

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
Do electric vehicles have a significant impact on the co2 emission value in germany?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
This project faces the topic e-mobility in sense of analyzing the impact of electric vehicles on the CO2 emission in germany. To have a better analysis we compare it to the vehicle and co2 data of Münster, to see if our result is comparable. This analysis can be used to decide wether electric vehicles should be more supported or are hyped to much.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Climate data of germany
* Data URL: https://www.umweltbundesamt.de/sites/default/files/medien/361/dokumente/2021_03_10_trendtabellen_thg_nach_sektoren_v1.0.xlsx
* Data Type: XLSX

* The Dataset containes different air quality values like CO2 or N2 and shows the time related difference over the past years

### Datasource2: Vehicle registration data of germany
* Data URL: https://www.kba.de/SharedDocs/Downloads/DE/Statistik/Fahrzeuge/FZ14/fz14_2022.xlsx?__blob=publicationFile&v=4
* Data Type: XSLX
* Meta Data: 

* The Dataset containes the number of new vehicle registrations over the last decade

### Datasource3: Climate data of muenster
* Data URL: https://opendata.stadt-muenster.de/sites/default/files/Muenster-CO2-Emissionen_2021.xls
* Data Type: XSLX
* Meta Data: https://opendata.stadt-muenster.de/dcatapde/dataset/entwicklung-der-j%C3%A4hrlichen-co2-emissionen-m%C3%BCnster.xml

* The Dataset containes co2 data of the city Münster from 2018 until 2022.

### Datasource4: Vehicle registration data of muenster
* Data URL: https://opendata.stadt-muenster.de/sites/default/files/Fahrzeugbestand-Regierungsbezirk-Muenster-2018-2022.xlsx
* Data Type: XSLX
* Meta Data: https://opendata.stadt-muenster.de/dcatapde/dataset/fahrzeugbestand-regierungsbezirk-m%C3%BCnster-2018-2022.xml

* This Dataset shows the vehicle registrations of the city Münster

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Exploring the data
2. Analyzing the co2 emission value over the last 5 years
3. Analyzing the registration of electric vehicles over the last 5 years
4. Creating Datapipeline
5. Compare analysis of data and plot graph
6. Create Report


