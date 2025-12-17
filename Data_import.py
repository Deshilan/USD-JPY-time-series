import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

def one_week1(start):
    data = cleared_data()
    week = data.Close.values[(2880+start*(5*1440)): (2880+start*1440*5 + (5*1440))]
    return week

def hours_dataset():
    dataset = data()
    dataset.drop(columns=['volume','High','Low','Open'], inplace=True)
    dataset_cleared = dataset.iloc[:-57]
    x = int(len(dataset_cleared)/60)
    hours = np.zeros(x)
    for i in range(x):
        hours[i] = dataset_cleared.Close.values[i*60]
    return hours


