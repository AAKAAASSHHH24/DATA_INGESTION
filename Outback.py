import pandas as pd

Sheet1 = pd.read_excel('data cleaning/Vendor Catalogues/Krannich Solar West LLC/PROD_Krannich_Solar_West_LLC_2023-08-16_DataSheet.xlsx', sheet_name= 'Available Stock')

Sheet2 = pd.read_excel('data cleaning/Vendor Catalogues/Krannich Solar West LLC/PROD_Krannich_Solar_West_LLC_2023-08-16_DataSheet.xlsx', sheet_name= 'Drop Ship & Varying lead times')

Sheet3 = pd.read_excel('data cleaning/Vendor Catalogues/Krannich Solar West LLC/PROD_Krannich_Solar_West_LLC_2023-08-16_DataSheet.xlsx', sheet_name= 'Remaining stocks ')
