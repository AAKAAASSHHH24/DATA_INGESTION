import pandas as pd

#SOLAR PANELS
Alchemy_Solar_panels = pd.read_excel('data cleaning/Vendor Catalogues/Alchemy Solar/alchemy_solar_panels.xlsx')
Alchemy_Solar_panels.to_excel('out/Alchemy_Solar_panels.xlsx')

#INVERTERS
Alchemy_Solar_inverters = pd.read_excel('data cleaning/Vendor Catalogues/Alchemy Solar/alchemy_solar_inverters.xlsx')

# Keep only the columns starting from index 2 (0-based)
Alchemy_Solar_inverters = Alchemy_Solar_inverters.iloc[:, 1:]
Alchemy_Solar_inverters.to_excel('out/Alchemy_Solar_inverters.xlsx')

#RACKING
Alchemy_Solar_racking = pd.read_csv('data cleaning/Vendor Catalogues/Alchemy Solar/alchemy_solar_racking.xlsx')

# Set the column names to be the values in the second row
Alchemy_Solar_racking.columns = Alchemy_Solar_racking.iloc[2]

# Reset the index
Alchemy_Solar_racking = Alchemy_Solar_racking.reset_index(drop=True)

# Drop the first three row

Alchemy_Solar_racking =Alchemy_Solar_racking.drop([0,1,2])

Alchemy_Solar_racking.to_excel('out/Alchemy_Solar_racking.xlsx')