import os
import pandas as pd
import numpy as np

dir = 'C:\saccade_48h'
dataframes = {}

#merging intraday files into one 3 dimension dataframe
for filename in os.listdir(dir):
    if filename.startswith('intraday_') and filename.endswith('.csv'):
        field = filename.split('_')[1].split('.')[0]  # Extract field name from filename
        filepath = os.path.join(dir, filename)
        dataframes[field] = pd.read_csv(filepath)

merged_intraday_data = pd.concat(dataframes.values(), keys=dataframes.keys(), axis=1)
merged_intraday_data.columns = [f'{field}_{column}' for field, column in merged_intraday_data.columns]

