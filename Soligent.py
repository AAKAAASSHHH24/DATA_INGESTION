import pandas as pd
soligent_raw = pd.read_excel('data cleaning/Vendor Catalogues/Soligent/PROD_Inventory_List_Soligent_2023-09-28_DataSheet.xlsx')

# Filter out "Not applicable" rows
df_filtered = soligent_raw.loc[soligent_raw['Final Status'].isin(['Already Listed', 'To be Listed'])]

# Concatenate the contents of columns 
df_filtered['Description'] ='Description: ' + df_filtered['Description'] + ' ,' + 'Wattage: '+ df_filtered['Wattage'].astype(str) + ' ,' +'Non-Commissionable: ' +df_filtered['Non-Commissionable'] + ' ,' +'Item Classification: ' +df_filtered['Item Classification'] + ' ,' +'Item Status: ' +df_filtered['Item Status']

df_filtered.drop(columns=['Display Name', 'Wattage',
       'Non-Commissionable', 'Item Classification', 'Item Status',
       'Floor Price'], inplace = True)

df_filtered = df_filtered.rename(columns={'Name': 'Item No.', 'Base Price': 'Price'})

df_filtered.to_excel('out/soligent_final.xlsx')


