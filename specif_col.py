# importing module
import pandas as pd


# creating dataframe
# importing excel file
df = pd.read_excel('Sample_data.xlsx')
df.head()
print(df)