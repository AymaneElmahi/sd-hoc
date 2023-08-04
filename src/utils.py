"""Module providingFunction printing python version."""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

def json_to_pd(json_file):
    """
    extract data from json file and convert to pandas dataframe
    :param json_file: json file
    :return: pandas dataframe
    """
    with open(json_file,encoding = 'utf-8') as js_file:
        data = json.load(js_file)
    df_ = pd.DataFrame(data)
    return df_

def create_df_(json_files):
    """
    create big dataframe from all json files
    :param json_files: list of json files
    :return: pandas dataframe
    """
    df_ = pd.DataFrame()
    for json_file in json_files:
        # use concat to append all dataframes
        df_ = pd.concat([df_, json_to_pd(json_file)], ignore_index=True)
    return df_



def epoch_to_datetime(epoch_time, h_add = 2):
    """
    Convert epoch time to datetime64 in GMT+2
    :param epoch_time: epoch time in milliseconds
    :param h_add: int, number of hours to add
    :return: datetime64 in GMT+2
    """
    datetime = np.datetime64(epoch_time, 'ms')  # Convert to datetime64 in GMT
    datetime += np.timedelta64(h_add, 'h')  # Add 2 hours for GMT+2
    return datetime



def plot_time_series(df_, y_axis, title, matplotlib=False):
    """
    Plot time series of people count, plot png if matplotlib = True
    :param df_: pandas dataframe
    :param y_axis: string, name of the column to plot
    :param matplotlib: boolean, if True plot png, else plot html
    :param first: boolean, if True, it is the first time to plot, else not
    :return: None
    """
    # Always convert the 'time' column to datetime
    df_.loc[:, 'time'] = pd.to_datetime(df_['time'])

    if matplotlib:
        # use matplotlib to plot
        fig, axis = plt.subplots()  # Create a figure and axes object
        axis.plot(df_['time'], df_[y_axis])
        axis.set(xlabel='time', ylabel=y_axis, title='Time Series of ' + title)
        axis.grid()
        plt.show()
    else:
        fig = px.line(df_, x='time', y=y_axis, title='Time Series of ' + title)
        fig.show()

def plot_time_series_dbd(df_,y_axis, title,matplotlib = False):
    """
    Plot time series of people count, plot png if matplotlib = True
    :param df_: pandas dataframe
    :param y_axis : string, name of the column to plot
    :param matplotlib: boolean, if True plot png, else plot html
    :param first: boolean, if True, it is the first time to plot, else not
    :return: None
    """
    # Always convert the 'time' column to datetime
    df_.loc[:,'time'] = pd.to_datetime(df_['time'])
    df_.loc[:,'date'] = df_['time'].dt.date
    dates = df_['date'].unique()
    for date in dates:
        df__date = df_[df_['date'] == date]
        if matplotlib :
            # use matplotlib to plot
            fig, axis = plt.subplots()  # Create a figure and axes object
            axis.plot(df__date['time'], df__date[y_axis])
            axis.set(xlabel='time', ylabel=y_axis, title='Time Series of '+title)
            axis.grid()
            plt.show()
        else:
            fig = px.line(df__date, x='time', y= y_axis, title='Time Series of '+title)
            fig.show()
