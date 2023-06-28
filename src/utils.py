import pandas as pd
import json

def json_to_pd(json_file):
    """
    extract data from json file and convert to pandas dataframe
    :param json_file: json file
    :return: pandas dataframe
    """
    with open(json_file) as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    return df

def create_df(json_files):
    """
    create big dataframe from all json files
    :param json_files: list of json files
    :return: pandas dataframe
    """
    df = pd.DataFrame()
    for json_file in json_files:
        # use concat to append all dataframes
        df = pd.concat([df, json_to_pd(json_file)], ignore_index=True)
    return df

import numpy as np
from datetime import timedelta

def epoch_to_datetime(epoch_time):
    """
    Convert epoch time to datetime64 in GMT+2
    :param epoch_time: epoch time in milliseconds
    :return: datetime64 in GMT+2
    """
    datetime = np.datetime64(epoch_time, 'ms')  # Convert to datetime64 in GMT
    datetime += np.timedelta64(2, 'h')  # Add 2 hours for GMT+2
    return datetime

import plotly.express as px

def plot_time_series(df):
    """
    Plot time series of people count
    :param df: pandas dataframe
    :return: None
    """
    df['time'] = pd.to_datetime(df['time'])
    fig = px.line(df, x='time', y='peoplecount_rgb', title='Time Series of People Count')
    fig.show()
    
def plot_time_series_dbd(df):
    """
    Plot time series of people count day by day, every day in a new graph
    :param df: pandas dataframe
    :return: None
    """
    df['time'] = pd.to_datetime(df['time'])
    df['date'] = df['time'].dt.date
    dates = df['date'].unique()
    for date in dates:
        df_date = df[df['date'] == date]
        fig = px.line(df_date, x='time', y='peoplecount_rgb', title='Time Series of People Count (Date: {})'.format(date))
        fig.show()


    
