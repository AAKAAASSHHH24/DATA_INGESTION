import camelot
import pandas as pd
import numpy as np


tables = camelot.read_pdf("data cleaning/Vendor Catalogues/The Powerstore/2023-09-05/TPS Catalogue-05-09-2023.pdf", pages = "all")
columns=['Item No.', 'Description', 'Price']

tables_df =[]
for i in range(len(tables)):
    tables_df.append(tables[i].df[1:])

tps = pd.concat(tables_df, axis=0, ignore_index=True)
tps.columns = columns

price_prices = tps['Price'].astype(str).str.extract(r'\$([\d,]+(\.\d{1,2})?)')[0].str.replace(',', '').astype(float)
# Use extracted prices from Price column to overwrite where needed
mask_price = price_prices.notna()
tps.loc[mask_price, 'Price'] = price_prices.dropna().astype(float)

# Replace empty strings with NaN
tps.replace('', np.nan, inplace=True)

# Drop rows where all elements are NaN
tps.dropna(how='all', inplace=True)
tps['Item No.'] = tps['Item No.'].astype(str)


tps.to_excel('out/tps_final.xlsx')
