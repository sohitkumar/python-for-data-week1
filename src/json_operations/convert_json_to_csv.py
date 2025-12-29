import pandas as pd

df = pd.read_json("data/input/sample.json")
df.to_csv("data/output/converted.csv", index=False, encoding="utf-8")