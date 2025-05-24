# Date: 23 May, 2025
# Data loading functions along with some visualization and exploration thrown in.

import pandas as pd
import os
import io

def load_file_as_df(user: str, file_num: str) -> pd.DataFrame:
    with open(os.path.join('src', 'data', 'Geolife Trajectories 1.3', 'Data', user, 'Trajectory', f'{file_num}.plt')) as f:
        # Skip top six lines
        f.readline(); f.readline(); f.readline(); f.readline(); f.readline(); f.readline()
        file_object = io.StringIO(f.read())
        df = pd.read_csv(file_object, index_col=False)
        df.columns = ['Latitude', 'Longitude', 'Set to 0', 'Altitude', 
                      'Days Since 12/30/1899', 'Date', 'Time']
        df.drop('Set to 0', axis=1, inplace=True)
        return df
    
def load_user_as_df(user: str) -> pd.DataFrame:
    file_list = os.listdir(os.path.join('src', 'data', 'Geolife Trajectories 1.3', 'Data', user, 'Trajectory'))
    return pd.concat([load_file_as_df(user, file.split('.')[0]) for file in file_list])

if __name__ == '__main__':
    df = load_user_as_df('000')
    print(len(df))
    print(df.tail())