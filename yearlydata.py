import pandas as pd
df = pd.read_csv("players.csv")
print (df.columns)

df = df.drop(['index', '_id',
       'career_AST', 'career_FG%',
       'career_FG3%', 'career_FT%', 'career_G', 'career_PER', 'career_PTS',
       'career_TRB', 'career_WS', 'career_eFG%',
       'draft_round',
       'shoots', 'weight'],axis = 1)
df.dropna(inplace = True)
print (df.head())
print (df.columns)
df = df.iloc[:,[8,9,5,6,2,1,0,4,3,7]]

print (df.head())
df.to_csv("yeardata.csv")
