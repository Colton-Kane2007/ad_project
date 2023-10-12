#standard DS imports
import numpy as np
import pandas as pd

#visualizion imports
import matplotlib.pyplot as plt
import seaborn as sns
def wrangle_curriculum():
    '''
    wrangle_curriculum takes a txt file that the user has downloaded from 
    Google Drive and prepares it by separating columns by space, renaming all columns descriptively, 
    engineering a datetime column and dropping old date and time columns, 
    changing datetime column to datetime type, setting datetime to index,
    engineering columns for each time attribute individually, filling nulls with zero for users
    that have no cohort_id, 

    '''
    df = pd.read_table('/Users/colt/Downloads/anonymized-curriculum-access.txt', sep=' ')
    df = df.rename(columns={'/': 'lesson', '2018-01-26': 'date', '09:55:03': 'time', '1': 'user_id', '8': 'cohort_id', '97.105.19.61': 'ip'})
    df['datetime'] = df['date'] + ' ' + df['time']
    df = df.drop(columns=['date', 'time'])
    df.datetime = pd.to_datetime(df['datetime'])
    df.set_index("datetime", inplace=True)
    df['year'] = df.index.year
    df['month'] = df.index.month_name()
    df['weekday'] = df.index.day_name()
    df['hour'] = df.index.hour
    df = df.fillna(0)
    return df
