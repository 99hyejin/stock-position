import pandas as pd
import os

# Path to the directory containing the intraday data files
intraday_dir = 'C:/saccade_48h/intraday_data'

# Path to the directory containing the daily data files
daily_dir = 'C:/saccade_48h/daily_data'
fields = ['open', 'high', 'low', 'close', 'volume', 'traded_value', 'num_trades', 'hit_volume', 'hit_value', 'num_hits', 'lift_volume', 'lift_value', 'num_lifts', 'midp_last', 'spread_last', 'nidp_twa', 'spread_twa']
# Function to merge intraday data files
def merge_intraday_files(directory,field):
    intraday_data = pd.DataFrame()
    for filename in os.listdir(directory):
        if filename.startswith(field):
            filepath = os.path.join(directory, filename)
            df = pd.read_csv(filepath)
            date = filename.split('_')[-1].split('.')[0]
            #print(filename)
            df['Date'] = pd.to_datetime(date, format='%m%d')
            df['Date'] = df['Date'].dt.strftime('%m-%d')
            intraday_data = pd.concat([intraday_data, df], ignore_index=True)
    return intraday_data

for f in fields:
    merged_intraday_data = merge_intraday_files(intraday_dir,f)
    merged_intraday_data.to_csv('intraday_'+f+'.csv', index=False)