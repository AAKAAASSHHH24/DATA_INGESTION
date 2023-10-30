import pandas as pd
Ontility = pd.read_excel('data cleaning/Vendor Catalogues/Ontility.com/PROD_Ontility_2023-08-25_DataSheet.xlsx')

Ontility.drop(columns=['Unnamed: 0','Unnamed: 1'], inplace=True)

Ontility= Ontility.drop([0,1,2,3,4,5,6,7,29,30,31,32,33,34,35,36,37])
Ontility.columns = Ontility.iloc[0]

# Reset the index
Ontility.reset_index(drop=True, inplace=True)
Ontility= Ontility.drop(0)

# Create a description column 
Ontility.insert(1, 'Description','Manufacturer: '+ Ontility['Manufacturer'].astype(str)  + ' , '  + 'Wattage: ' + Ontility['Wattage'].astype(str) + ' , ' + 'Part Number: ' + Ontility['Part Number'].astype(str) + ' , '+ 'Dimensions (mm): ' + Ontility['Dimensions (mm)'].astype(str) +' , '+ 'Type: ' + Ontility['Type'].astype(str)+ ' , ' +'Cell: ' + Ontility['Cell'].astype(str)+ ' , ' +'Bifacial: ' + Ontility['Bifacial']+ ' , ' +'Pallet Size: ' + Ontility['Pallet Size'].astype(str) + ' , ' + 'Total Watts: ' + Ontility['Total Watts'].astype(str) + ' , '  + 'Location: ' + Ontility['Location']+ ' , '  + 'Min Buy: ' + Ontility['Min Buy'] + ' , '  + 'Notes: ' + Ontility['Notes'])

Ontility.drop(columns = ['Manufacturer', 'Wattage', 'Part Number', 'Dimensions (mm)', 'Type', 'Cell', 'Bifacial', 'Pallet Size', 'Total Watts','Location', 'Min Buy', 'Notes'], inplace=True)
Ontility.to_excel('out/Ontility.xlsx')

