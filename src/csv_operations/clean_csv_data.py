import pandas as pd

df = pd.read_csv("data/input/messy_data.csv", skipinitialspace=True)
cleaned_df = df.replace(r"^\s*$", pd.NA, regex=True)
cleaned_df = cleaned_df.map(lambda x: x.strip() and x.lower() if isinstance(x, str) else x)
cleaned_df.to_csv("data/output/clean.csv", index=False)