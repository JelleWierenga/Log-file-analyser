import os
import pandas as pd

logs = pd.DataFrame(columns=['time', 'state', 'message'])
path = "path/to/log/file/folder"
for file in os.listdir(path):
    new_path = f"{path}{file}"
    # new_path = path
    with open(new_path) as f:
        for line in f:
            time = line[1:9]
            state = line[11:15]
            message = line[17:].strip()
            new_row = pd.DataFrame({'time': [time], 'state': [state], 'message': [message]})
            logs = pd.concat([logs, new_row], ignore_index=True)
    logs.to_csv(f"csv/{file}.csv")