import pandas as pd

df = pd.read_csv('./exemplo.csv')

df_sp = df[df['estado']=='SP']

print(df_sp)