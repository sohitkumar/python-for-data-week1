import pandas as pd

df = pd.read_csv("data/input/employees.csv")
df.to_json("data/output/employees.json", orient="records")