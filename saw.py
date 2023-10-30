import pandas as pd
saw_tech = pd.read_excel('data cleaning/Vendor Catalogues/S.A.W. Technology/PROD_Inventory_List_SAW_2023-09-19_DataSheet.xlsx')

# Set the column names to be the values in the second row
saw_tech.columns = saw_tech.iloc[0]

# Reset the index
saw_tech = saw_tech.reset_index(drop=True)

# Drop the first row (index 0)
saw_tech= saw_tech.drop(0)
saw_tech = saw_tech.rename(columns={'S.A.W. Technology': 'Item No.', 'Price in CAD': 'Price'})

saw_tech.to_excel('out/saw_final.xlsx')