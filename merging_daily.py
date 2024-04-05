import pandas as pd
import os

# Path
daily_dir = 'C:/saccade_48h/daily_data'

def merge_daily_files(directory):
    daily_data = pd.DataFrame()
    for filename in os.listdir(directory):
        if filename.startswith('daily_') and filename.endswith('.csv'):
            filepath = os.path.join(directory, filename)
            df = pd.read_csv(filepath)
            daily_data = pd.concat([daily_data, df], ignore_index=True)
    return daily_data

merged_daily_data = merge_daily_files(daily_dir)
merged_daily_data.to_csv('merged_daily_data.csv', index=False)