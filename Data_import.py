import pandas as pd
import numpy as np

def data():
    data = pd.read_csv('USD_JPY_2015_07_2025_ASK.csv')
    data.set_index('timestamp', inplace=True)
    return data

def cleared_data():
    data = pd.read_csv('USD_JPY_2015_07_2025_ASK.csv')
    data.set_index('timestamp', inplace=True)
    data.drop(columns=['volume','Open','High','Low'], inplace=True)
    return data

def one_day1(start):
    data = cleared_data()
    day = data.Close.values[(start*1440): (start*1440 + 1440)]
    return day
