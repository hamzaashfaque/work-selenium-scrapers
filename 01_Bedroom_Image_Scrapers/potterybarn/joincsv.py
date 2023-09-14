import pandas as pd

df1 = pd.read_csv('potterybarn.csv')
df1 = df1.drop('title', axis=1)
df2 = pd.read_csv('potterybarn_titles.csv')
df3 = pd.concat([df1, df2], axis=1)
df3.to_csv("potterybarn_final.csv", index=False)