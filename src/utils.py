import pandas as pd
import json

import matplotlib.pyplot as plt

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

def plot_time_series(df,y,title,matplotlib = False,first = True):
    """
    Plot time series of people count, plot png if matplotlib = True
    :param df: pandas dataframe
    :param y : string, name of the column to plot
    :param matplotlib: boolean, if True plot png, else plot html
    :param first: boolean, if True, it is the first time to plot, else not
    :return: None
    """
    if first:
        # use .loc to apply pd.to_datetime to the column 'time'
        df.loc[:,'time'] = pd.to_datetime(df['time']) 
        
    if matplotlib :
        # use matplotlib to plot
        fig, ax = plt.subplots()  # Create a figure and axes object
        ax.plot(df['time'], df[y])
        ax.set(xlabel='time', ylabel=y, title='Time Series of '+title)
        ax.grid()
        fig.savefig("./images/time_series.png")  # Save the figure instead of the axes
        plt.show()
        
    else:
        fig = px.line(df, x='time', y=y, title='Time Series of '+title)
        fig.show()
        
        
        
    
def plot_time_series_dbd(df,y, title,matplotlib = False, first = True,):
    """
    Plot time series of people count, plot png if matplotlib = True
    :param df: pandas dataframe
    :param y : string, name of the column to plot
    :param matplotlib: boolean, if True plot png, else plot html
    :param first: boolean, if True, it is the first time to plot, else not
    :return: None
    """
    if first:
        df.loc[:,'time'] = pd.to_datetime(df['time'])
        df.loc[:,'date'] = df['time'].dt.date
        
    dates = df['date'].unique()
    
    for date in dates:
        df_date = df[df['date'] == date]
        
        if matplotlib :
            # use matplotlib to plot
            fig, ax = plt.subplots()  # Create a figure and axes object
            ax.plot(df_date['time'], df_date[y])
            ax.set(xlabel='time', ylabel=y, title='Time Series of '+title)
            ax.grid()
            # name the file with date as 'yyyy-mm-dd.png'
            fig.savefig("./images/"+str(date)+".png")  # Save the figure instead of the axes
            plt.show()
            
        else:
            fig = px.line(df_date, x='time', y= y, title='Time Series of '+title)
            fig.show()
            

    
