import pandas as pd

def combine_two_csv(file1, file2):
    merged_df = pd.concat([f1, f2])
    merged_df.to_csv("data/output/combined.csv", index=False)
    return

f1 = pd.read_csv("data/input/students_part1.csv")
f2 = pd.read_csv("data/input/students_part2.csv")
combine_two_csv(f1, f2)