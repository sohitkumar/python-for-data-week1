import pandas as pd

df = pd.read_csv("data/input/employees.csv")
filtered_df = df[df['salary'] > 80000]
filtered_df.to_csv("data/output/filtered.csv", index=False)