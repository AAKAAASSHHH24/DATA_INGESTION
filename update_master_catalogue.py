from pandas_datareader import wb
import pandas as pd

#Indicators: GDP, GDP per capita, access to electricity, population, CO2 emissions
indicators = ["NY.GDP.MKTP.CD", "NY.GDP.PCAP.CD", "EG.ELC.ACCS.ZS",
              "SP.POP.TOTL", "EN.ATM.CO2E.KT"]

#ISO Code of countries: Australia, Bhutan, Germany, France, Indonesia, India, Japan,
#Korea, Netherlands, Nepal, Russia, South Africa 
countries = ["AUS", "BTN", "DEU", "FRA", "IDN", "IND", "JPN",
              "KOR", "NPL", "NLD", "RUS", "ZAF"]


df = wb.download(country = countries,
                 indicator = indicators,
                 start = 2018, 
                 end = 2018)

df.rename({"NY.GDP.MKTP.CD":"GDP",
           "NY.GDP.PCAP.CD":"GDP per capita",
           "EG.ELC.ACCS.ZS":"Access to electricity",
           "SP.POP.TOTL": "Population",
           "EN.ATM.CO2E.KT": "kt CO2"}, 
         axis = 1, inplace = True)

df.index = df.index.get_level_values(0)

df


excel_file = pd.ExcelFile('data.xlsx')

for sheet_name in excel_file.sheet_names:
    df = excel_file.parse(sheet_name)
    # Add your lookup and update logic here

# Assuming you have a dictionary mapping values to update
update_dict = {
    'Vendor A': 'Updated Vendor A',
    'Vendor B': 'Updated Vendor B'
}

df['Vendor'] = df['Vendor'].map(update_dict)


with pd.ExcelWriter('data_updated.xlsx', engine='openpyxl') as writer:
  writer.book = excel_file.book
  writer.sheets = {ws.title: ws for ws in excel_file.book.worksheets}
  df.to_excel(writer, sheet_name=sheet_name, index=False)
