import pandas as pd

df = pd.read_csv("data/input/messy_data.csv", skipinitialspace=True)

df_clean = df.replace(r'^\s*$', pd.NA, regex=True)
missing_mask = df_clean.isna()

print("Missingness mask:")
print(missing_mask)

print("\nMissing values per column:")
print(missing_mask.sum())

print("\nTotal missing values:")
print(missing_mask.values.sum())