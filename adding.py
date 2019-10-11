import pandas as pd

lst = ["USA", "France", "Germany". "Australia"]

df = pd.DataFrame(lst,colums = ["Country"])

print(df)

df2 = pd.DataFrame([[1, 2], [3, 4]], columns=[‘A’,’B’])

print(df2)

df3 = pd.DataFrame([[5, 6]], columns=list('AB’))

df2 = df2.append(df3, ignore_index=True)

print(df3)

