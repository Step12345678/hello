import pandas as pd 

df = pd.read_csv("final.csv")


print (df.info())

#no points or assists
df.replace('-', 0, inplace=True)

df['career_TRB'] = df['career_TRB'].astype(float)

print (df.describe())

