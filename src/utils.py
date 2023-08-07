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

def create_final_df(json_files, df_co2):
    """
    Create final dataframe with all the data.
    :param json_files: list of json files
    :param df_co2: pandas dataframe containing co2 data
    :return: pandas dataframe
    """
    df_ = create_df_(json_files)
    # transform epoch time to datetime
    df_['time'] = df_['time'].apply(epoch_to_datetime, h_add=1)
    df_ = df_[['time', 'peoplecount_rgb']]
    df_ = df_[df_['peoplecount_rgb'] != -7]
    # Multiply the EpochTime/UnixTime column to get epoch time in milliseconds and make an integer
    df_co2['EpochTime/UnixTime ( UTC )'] = df_co2['EpochTime/UnixTime ( UTC )'].apply(
        lambda x: int(x * 1000))
    # Transform epoch time to datetime, let the function know that the time is in GMT+1
    df_co2['timestamp'] = df_co2['EpochTime/UnixTime ( UTC )'].apply(epoch_to_datetime, h_add=1)
    # Keep only 'timestamp' and non-null 'co2-ndir' columns
    df_co2 = df_co2[['timestamp', 'co2-ndir']].dropna()
    df_co2['days'] = df_co2['timestamp'].dt.date  # Extract only the date part
    # we are implementing this for a specific dataset, I had to delete the dates
    # after 2021-03-30 because they are not present in the 'peoplecount_rgb
    # feel free to adjust this part as needed
    df_ = df_[df_['time'] < '2021-03-30']
    unique_dates = df_.time.dt.date.unique()
    unique_dates.sort()
    df_co2 = df_co2[df_co2['days'].isin(unique_dates)]
    # drop days column
    df_co2 = df_co2.drop(columns=['days'])
    # rename columns
    df_co2 = df_co2.rename(columns={'timestamp': 'time', 'co2-ndir': 'co2'})
    df_co2 = df_co2.sort_values('time')
    # Nearest Neighbor Matching
    df_matched = pd.merge_asof(df_, df_co2, on='time', direction='nearest')
    # Fuzzy Matching
    time_window = pd.Timedelta(minutes=1)  # Define the time window (adjust as needed)
    df_matched = pd.merge_asof(df_, df_co2, on='time', tolerance=time_window)
    df_matched = df_matched[['time', 'peoplecount_rgb', 'co2']]
    df_matched.dropna(inplace=True)
    # force co2 to be float
    df_matched['co2'] = pd.to_numeric(df_matched['co2'], downcast='float')
    df_matched['occupancy'] = df_matched['peoplecount_rgb'].apply(lambda x: 0 if x == 0 else 1)
    # transform the time column only to hours
    df_matched['time_hours'] = df_matched['time'].apply(lambda x: x.hour)
    return df_matched
