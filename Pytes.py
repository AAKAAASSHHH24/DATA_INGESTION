import pandas as pd
pytes = pd.read_excel('data cleaning/Vendor Catalogues/Pytes_Energy/PROD_Inventory_List_Pytes_Energy_2023-12-09_Database.xlsx')

# Create a description column 
pytes.insert(1, 'Description', 'Model No. ' + pytes['Model No.'].astype(str) +' , '+ 'Product: ' + pytes['Product'].astype(str)+ ' , ' +'Manufacturer ' + pytes['Manufacturer']+' , '+ 'Type: '+ pytes['Type'] )

pytes.drop(columns= ['S. No.', 'Item No.', 'Model No.',
       'Product', 'Manufacturer', 'Type'], inplace = True)

pytes = pytes[['US Solar SKU No.','Description','Scenario','Brand','Price','Status']]
pytes.drop(columns =['Scenario','Brand'], inplace = True)
pytes.to_excel('out/pytes_final.xlsx')