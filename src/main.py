import pandas as pd
import os

df = pd.DataFrame(columns=['time', 'state', 'message'])

path = "path/to/csv/folder"

#merge all csv files into one
for file in os.listdir(path):
    new_path = f"{path}/{file}"
    new_df = pd.read_csv(new_path)
    df = pd.concat([df, new_df], ignore_index=True)

print(df)