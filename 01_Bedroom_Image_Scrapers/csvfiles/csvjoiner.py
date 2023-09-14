import pandas as pd
df1 = pd.read_csv('csvfiles/potterybarn_final.csv')
df2 = pd.read_csv('csvfiles/bedbathbeyond.csv', encoding='ISO-8859-1')
df3 = pd.read_csv('csvfiles/dallasdesignerfurniture.csv', encoding='ISO-8859-1')
df4 = pd.read_csv('csvfiles/marlofurniture.csv', encoding='ISO-8859-1')
df5 = pd.read_csv('csvfiles/woodstock.csv', encoding='ISO-8859-1')
df6 = pd.read_csv('csvfiles/afd.csv')
df7 = pd.read_csv('csvfiles/luna_homes.csv')
df8 = pd.read_csv('csvfiles/cetmob.csv')

dfmain1 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8], axis=0)


print(dfmain1.columns)

print(len(dfmain1))

dfmain1.to_csv("csvfiles/final_concat.csv")