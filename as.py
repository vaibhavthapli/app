import pandas as pd

df = pd.read_csv('aps_failure.csv')
print(df.head())
print(df.shape)
print(df.info())