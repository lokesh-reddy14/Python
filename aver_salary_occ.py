'''3.	Given is a dataframe showing the name, occupation, salary of people. Find the average salary per occupation. '''
import pandas as pd

df = pd.DataFrame(columns=["name", "occupation", "salary"])
parts = int(input("number of people:"))

for _ in range(parts):
    dp = input("enter the name:")
    st = input("Enter the occupation:".format(dp))
    et = int(input("Enter salary:".format(dp)))
    df1 = pd.DataFrame(data=[[dp,st,et]],columns=["name", "occupation", "salary"])
    df = pd.concat([df,df1], axis=0)

df.index = range(len(df.index))
print(df)
avg=df['salary'].mean()
print("average salary:",avg)
