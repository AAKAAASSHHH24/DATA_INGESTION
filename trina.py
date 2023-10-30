import pandas as pd
trina = pd.read_excel('data cleaning/Vendor Catalogues/Trina/PROD_Trina_Inventory_Older_Cable_Variants-2023-05-31_DataSheet.xlsx')

# Set the column names to be the values in the second row
trina.columns = trina.iloc[0]

# Reset the index
trina = trina.reset_index(drop=True)

# Drop the first row (index 0)
trina= trina.drop(0)

# Keep only the columns starting from index 2 (0-based)
trina = trina.iloc[:, 2:]

# Create a description column 
trina.insert(1, 'Description','Product Type: '+ trina['Product Type'].astype(str)  + ' , '  + 'Port: ' + trina['Port'] + ' , ' + 'Power per piece: ' + trina['Power per'].astype(str) + ' , '+ 'Mounting Holes: ' + trina['Mounting Holes'].astype(str) +' , '+ 'Wattage: ' + trina['Watts '].astype(str)+ ' , ' +'Connector Type: ' + trina['Connector Type']+ ' , ' +'Cell Shape: ' + trina['Cell Shape']+ ' , ' +'Glass Thickness: ' + trina['Glass Thickness'] + ' , '+ 'Cable Length: ' + trina['Cable Length'] + ' , ' + 'Dimension: ' + trina['Dimension'] + ' , '  + 'Full Pallet Qty: ' + trina['Full Pallet Qty'])

trina.drop(columns = ['Product Type', 'Power per', 'Watts ', 'Port', 'Mounting Holes', 'Connector Type', 'Cell Shape', 'Glass Thickness',
       'Cable Length', 'Dimension', 'Full Pallet Qty'], inplace = True)

trina.to_excel('out/trina.xlsx')