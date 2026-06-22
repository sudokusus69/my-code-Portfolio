import pandas as pd

df = pd.read_csv('data2.csv')

# df.loc[9, "Duration"] = 45
print(df)

def rd():
    for x in df.index:
        if df.loc[x, "Duration"] > 45:
            df.loc[x, "Duration"] = 45
        elif df.loc[x, "Duration"] < 10:
            df.loc[x, "Duration"] = 10
    print(df)

def rd2():
    # or you can just remove the rows if you want to insetead of replacing the data with a new one

    for x in df.index:
        if df.loc[x, "Duration"] >= 60 or df.loc[x, "Duration"] < 10:
            df.drop(x, inplace = True)
    print(df)


x  = df.duplicated()
y = df.drop_duplicates()

# print(x)
# print(y)