'''Assignment 3
1.	Given a CSV file or excel file to read it into a dataframe and display it. 
'''
import pandas as pd

df = pd.read_csv('data.csv')
df1 = pd.DataFrame(df)

print(df1)
