import camelot
import pandas as pd

tables = camelot.read_pdf("data cleaning/Vendor Catalogues/Solar Electric Supply/PROD_SES_Solar_Module_Dealer_Pricing_Effective_[6629830]_2023-06-08.pdf", pages = "all")
columns=['Model No.','Description','Wattage','Cell Format','# Per pallet','Less than Pallet Price $/Watt','Pallet + Price $/Watt','3+ Pallet Price $/Watt','10+ Pallet Price $/Watt','Stocking Location','Comments']


tables_df =[]
for i in range(len(tables)):
    tables_df.append(tables[i].df[1:])

solar_electric = pd.concat(tables_df, axis=0, ignore_index=True)
solar_electric.columns = columns

solar_electric = solar_electric.dropna(thresh=2)

# Define a regular expression pattern to match values following the dollar sign
pattern = r'\$([\d.]+)'

# Extract the values and create a new column
solar_electric['Price'] = solar_electric['Less than Pallet Price $/Watt'].str.extract(pattern, expand=False)

solar_electric.to_excel('out/ses_final.xlsx')

