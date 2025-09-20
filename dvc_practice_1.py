import os
import numpy as np
import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [24, 30, 22, 35, 28],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
})

new_row = {"Name": "Frank", "Age": 29, "City": "San Francisco"}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

folder_path = "./data"
os.makedirs(folder_path,exist_ok= True)

file_path = os.path.join(folder_path, "sample_data.csv")
df.to_csv(file_path)
