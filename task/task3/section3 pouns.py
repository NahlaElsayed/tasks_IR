import pandas as pd
df = pd.read_csv('top 100 streamed songs.csv')
num_null_rows = df.isnull().sum().sum()
print("Number of null rows before removal:", num_null_rows)
df.dropna(inplace=True)
num_null_rows = df.isnull().sum().sum()
print("Number of null rows after removal: ", num_null_rows)