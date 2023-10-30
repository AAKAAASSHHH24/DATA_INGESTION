## PANELS

# importing required modules
import PyPDF2
import pandas as pd
import re
import csv
import io


# creating a pdf file object
pdfFileObj = open('data cleaning/Vendor Catalogues/Krannich Solar East LLC/KRUSE Exclusive Panel Pricing v2 Dt. 16-10-23.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)

def modify_list(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst[0]]
    else:
        return [lst[0], ",".join(lst[1:-1]), lst[-1]]


def extract_tables_to_dataframes(text):
    # Split by the table header pattern and discard the first part as it's not a table

    try:
        tables = re.split(r'Item No. Wattage Model Number Color Cell TypePallet\nQuantitiesAvailability Price Datasheet', text)[1:]
    except Exception as e:
        tables = []

    dataframes = []

    for table in tables:
        # Get each row by splitting the table at newline characters
        rows = table.strip().split('\n')
        
        # Convert each row to a list of values
        table_data = [modify_list(row.split()) for row in rows]

        # Convert to DataFrame
        df = pd.DataFrame(table_data, columns=['Item No.', 'Description', 'Price'])
        dataframes.append(df)

    return dataframes

cols = [['Item No.', 'Wattage', 'Model No:', 'Colour', 'Cell Type', 'Pallet Qty', 'AVAILABILITY', 'Price', 'Datasheet']]

dfs = []
for i in range(len(pdfReader.pages)):
    # creating a page object
    pageObj = pdfReader.pages[i]
    text = pageObj.extract_text()
    dfs.extend(extract_tables_to_dataframes(text))

kruse_panels = pd.concat(dfs, axis=0, ignore_index=True)
#kruse = kruse[kruse['Price'].str.contains('$')]

# Filter out rows where 'col1' is None or just contains a dollar sign
filtered_kruse_df = kruse_panels[(kruse_panels['Price'].str.contains('/w'))  |  (kruse_panels['Item No.'].str.contains('KU'))]

kruse_df = filtered_kruse_df.reset_index().drop(columns= ['index'])

for i in range(len(kruse_df)):
    kruse_df['Item No.'][i] = kruse_df['Item No.'][i][:7]
    if kruse_df['Item No.'][i][:2] != 'KU':
        desc = str(kruse_df['Item No.'][i]) + str(kruse_df['Description'][i])
        price = str(kruse_df['Price'][i])
        kruse_df['Description'][[i-1]] = desc
        kruse_df['Price'][[i-1]] = price
        kruse_df = kruse_df.drop(i)
# Reset the index after dropping a row
kruse_df = kruse_df.reset_index(drop=True)

# Concatenate the two DataFrames
#concatenated_df = pd.concat([kruse, kruse_df], ignore_index=True)

kruse_df.to_excel('out/kruse_panels.xlsx')