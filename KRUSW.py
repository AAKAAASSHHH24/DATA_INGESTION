import pandas as pd

Sheet1 = pd.read_excel('data cleaning/Vendor Catalogues/Krannich Solar West LLC/PROD_Krannich_Solar_West_LLC_2023-08-16_DataSheet.xlsx', sheet_name= 'Available Stock')

Sheet2 = pd.read_excel('data cleaning/Vendor Catalogues/Krannich Solar West LLC/PROD_Krannich_Solar_West_LLC_2023-08-16_DataSheet.xlsx', sheet_name= 'Drop Ship & Varying lead times')

Sheet3 = pd.read_excel('data cleaning/Vendor Catalogues/Krannich Solar West LLC/PROD_Krannich_Solar_West_LLC_2023-08-16_DataSheet.xlsx', sheet_name= 'Remaining stocks ')

Krannich_Solar_West = pd.concat([Sheet1,Sheet2,Sheet3], axis=0, ignore_index=True)

# Create a description column 
Krannich_Solar_West.insert(1, 'Description', 'Description: ' + Krannich_Solar_West['Description 1'].astype(str) +' , '+ Krannich_Solar_West['Description 2'].astype(str)+ ' , ' +'Matchcode ' + Krannich_Solar_West['Matchcode']+' , '+ 'Manufacturer: '+ Krannich_Solar_West['Manufacturer']+' , '+ 'Manufacturer-Item No.: '+ Krannich_Solar_West['Manufacturer-Item No.'] )
Krannich_Solar_West.drop(columns= ['Description 1', 'Description 2',
       'Matchcode', 'Manufacturer', 'Manufacturer-Item No.'], inplace = True)

Krannich_Solar_West.to_excel('out/KRUSW_final.xlsx')

