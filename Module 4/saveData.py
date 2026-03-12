import pandas as pd
df= pd.read_csv("data.csv")
print(df["Age"].unique())

print(df["Age"]>27)
df1 =df[df["Age"]>27]
print(df1)

df1.to_csv("newdata.csv")