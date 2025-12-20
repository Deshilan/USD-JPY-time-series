import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def data():
    data = pd.read_csv('USD_JPY_2015_07_2025_ASK.csv')
    data.set_index('timestamp', inplace=True)
    return data

def cleared_data(start, end):

    data = pd.read_csv('USD_JPY_2015_07_2025_ASK.csv')
    data.set_index('timestamp', inplace=True)
    clear_data = data[start:end]
    clear_data.drop(columns=['volume','Open','High','Low'], inplace=True)

    return clear_data


def one_day1(start):
    n1 = 1440
    data = cleared_data()
    day = data.Close.values[(start*n1): (start*n1 + n1)]
    return day

def one_week1(start):
    data = cleared_data()
    n1 = 1440
    week = data.Close.values[(2*n1+start*(5*n1)): (2*n1+start*n1*5 + (5*n1))]
    return week

def hours_dataset():
    dataset = data()
    dataset.drop(columns=['volume','High','Low','Open'], inplace=True)
    dataset_cleared = dataset.iloc[:-57]
    x = int(len(dataset_cleared)/60)
    hours = np.zeros(x)
    for i in range(x):
        hours[i] = dataset_cleared.Close.values[i*60]

    plt.plot(hours)
    plt.show()
    return hours

cleared_data()