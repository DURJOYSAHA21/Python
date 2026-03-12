import pandas as pd
print(pd.read_csv("data.csv"))

df = pd.read_csv("data.csv")
print(df.head())

data={
    "Artist": ["Michael Jackson", "AC/DC"],
    "Released": [1982, 1980]
}
df1=pd.DataFrame(data)
print(df1)
print("\n")
print(df1["Artist"])
print("\n")
print(df1.iloc[0,0]) #position based search

print(df1.loc[0,"Artist"])#label based

print(df1.iloc[0:2, 0:3])
print(df1.loc[0:2,["Artist"]])