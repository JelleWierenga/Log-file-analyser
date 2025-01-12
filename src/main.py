import pandas as pd
import os

df = pd.DataFrame(columns=['time', 'state', 'message'])

path = "E:/Programmeren/Tarball analyse/csv"

#merge all csv files into one
for file in os.listdir(path):
    new_path = f"{path}/{file}"
    new_df = pd.read_csv(new_path)
    df = pd.concat([df, new_df], ignore_index=True)

print(df)
df.to_csv("E:/Programmeren/Tarball analyse/merged.csv")