'''2.	Given a dataframe, select rows based on a condition. '''
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)
num=int(input('enter the row'))

print(df.loc[num])
