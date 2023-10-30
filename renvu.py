import pandas as pd
renvu = pd.read_excel('data cleaning/Vendor Catalogues/Renvu/RENVU Commercial Price List.xlsx')

renvu.drop(columns=['www.renvu.com/', 'Unnamed: 11'], inplace = True)

# Drop the first row (index 0)
renvu= renvu.drop(0)

# Set the column names to be the values in the second row
renvu.columns = renvu.iloc[0]

# Reset the index
renvu = renvu.reset_index(drop=True)
# Drop the first row (index 0)
renvu= renvu.drop(0)
renvu = renvu.iloc[:-3]

# Create a description column 
renvu.insert(1, 'Description','Wattage: '+ renvu['(W)'].astype(str) + ' , ' + 'Brand: ' + renvu['Brand'] + ' , '+ 'Frame/BackSheet: ' + renvu['Frame/\nBack Sheet'].astype(str) +' , '+ 'Details: ' + renvu['Details\n(DS linked)'].astype(str)+ ' , ' +'Packing: ' + renvu['Packing\n(PLT / FTL)'])

renvu.drop(columns= ['(W)', 'Brand', 'Frame/\nBack Sheet',
       'Details\n(DS linked)','Packing\n(PLT / FTL)'], inplace = True)

renvu.to_excel('out/renvu.xlsx')