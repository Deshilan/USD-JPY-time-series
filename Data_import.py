import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def data():
    data = pd.read_csv('USD_JPY_2015_07_2025_ASK.csv')
    print(data["timestamp"])
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

def hours_file():
    data = pd.read_csv('USD_JPY_2015_07_2025_ASK.csv')
    data['timestamp'] = pd.to_datetime(data["timestamp"], format="%d.%m.%Y %H:%M:%S.%f GMT%z")
    data = data.loc[data["timestamp"].dt.minute.eq(59)].copy()
    data.to_csv("plik.csv", index=False)

def add_Japan_interest_rate():
    data = pd.read_csv('plik.csv')
    data["timestamp"] = pd.to_datetime(data["timestamp"],  errors="raise")
    data['Japan IR'] = 0
    x1 = pd.Timestamp("2025-10-30 09:00:00+05:30")
    mask1 = data["timestamp"] < x1
    data.loc[mask1, "Japan IR"] = 0.5
    x2 = pd.Timestamp("2025-01-24 09:00:00+05:30")
    mask1 = data["timestamp"] < x2
    data.loc[mask1, "Japan IR"] = 0.25
    x3 = pd.Timestamp("2024-07-31 09:00:00+05:30")
    mask1 = data["timestamp"] < x3
    data.loc[mask1, "Japan IR"] = 0.1
    x4 = pd.Timestamp("2024-03-19 09:00:00+05:30")
    mask1 = data["timestamp"] < x4
    data.loc[mask1, "Japan IR"] = -0.1
    x5 = pd.Timestamp("2016-01-29 09:00:00+05:30")
    mask1 = data["timestamp"] < x5
    data.loc[mask1, "Japan IR"] = 0

    data['USA IR'] = 0
    U1 = pd.Timestamp("2025-08-31 23:30:00+05:30")
    mask1 = data["timestamp"] < U1
    data.loc[mask1, "USA IR"] = 4.5

    U2 = pd.Timestamp("2024-12-18 23:30:00+05:30")
    mask1 = data["timestamp"] < U2
    data.loc[mask1, "USA IR"] = 4.75

    U3 = pd.Timestamp("2024-10-31 23:30:00+05:30")
    mask1 = data["timestamp"] < U3
    data.loc[mask1, "USA IR"] = 5

    U4 = pd.Timestamp("2024-10-31 23:30:00+05:30")
    mask1 = data["timestamp"] < U4
    data.loc[mask1, "USA IR"] = 4.75

    U5 = pd.Timestamp("2024-09-18 23:30:00+05:30")
    mask1 = data["timestamp"] < U5
    data.loc[mask1, "USA IR"] = 5.5

    U6 = pd.Timestamp("2023-07-26 23:30:00+05:30")
    mask1 = data["timestamp"] < U6
    data.loc[mask1, "USA IR"] = 5.25

    U7 = pd.Timestamp("2023-05-03 23:30:00+05:30")
    mask1 = data["timestamp"] < U7
    data.loc[mask1, "USA IR"] = 5.0

    U8 = pd.Timestamp("2023-03-22 23:30:00+05:30")
    mask1 = data["timestamp"] < U8
    data.loc[mask1, "USA IR"] = 4.75

    U9 = pd.Timestamp("2023-02-01 23:30:00+05:30")
    mask1 = data["timestamp"] < U9
    data.loc[mask1, "USA IR"] = 4.5

    U10 = pd.Timestamp("2022-12-14 23:30:00+05:30")
    mask1 = data["timestamp"] < U10
    data.loc[mask1, "USA IR"] = 4.0

    U11 = pd.Timestamp("2022-11-02 23:30:00+05:30")
    mask1 = data["timestamp"] < U11
    data.loc[mask1, "USA IR"] = 3.25

    U12 = pd.Timestamp("2022-09-21 23:30:00+05:30")
    mask1 = data["timestamp"] < U12
    data.loc[mask1, "USA IR"] = 2.5

    U13 = pd.Timestamp("2022-07-27 23:30:00+05:30")
    mask1 = data["timestamp"] < U13
    data.loc[mask1, "USA IR"] = 1.75

    U14 = pd.Timestamp("2022-06-15 23:30:00+05:30")
    mask1 = data["timestamp"] < U14
    data.loc[mask1, "USA IR"] = 1.0

    U15 = pd.Timestamp("2022-05-04 23:30:00+05:30")
    mask1 = data["timestamp"] < U15
    data.loc[mask1, "USA IR"] = 0.5

    U16 = pd.Timestamp("2022-03-16 23:30:00+05:30")
    mask1 = data["timestamp"] < U16
    data.loc[mask1, "USA IR"] = 0.25

    U17 = pd.Timestamp("2020-03-15 23:30:00+05:30")
    mask1 = data["timestamp"] < U17
    data.loc[mask1, "USA IR"] = 1.25

    U18 = pd.Timestamp("2020-03-03 23:30:00+05:30")
    mask1 = data["timestamp"] < U18
    data.loc[mask1, "USA IR"] = 1.75

    U19 = pd.Timestamp("2019-10-30 23:30:00+05:30")
    mask1 = data["timestamp"] < U19
    data.loc[mask1, "USA IR"] = 2.0

    U20 = pd.Timestamp("2019-09-18 23:30:00+05:30")
    mask1 = data["timestamp"] < U20
    data.loc[mask1, "USA IR"] = 2.25

    U21 = pd.Timestamp("2019-07-31 23:30:00+05:30")
    mask1 = data["timestamp"] < U21
    data.loc[mask1, "USA IR"] = 2.5

    U22 = pd.Timestamp("2018-12-19 23:30:00+05:30")
    mask1 = data["timestamp"] < U22
    data.loc[mask1, "USA IR"] = 2.25

    U23 = pd.Timestamp("2018-09-26 23:30:00+05:30")
    mask1 = data["timestamp"] < U23
    data.loc[mask1, "USA IR"] = 2.0

    U24 = pd.Timestamp("2018-06-13 23:30:00+05:30")
    mask1 = data["timestamp"] < U24
    data.loc[mask1, "USA IR"] = 1.75

    U25 = pd.Timestamp("2018-03-21 23:30:00+05:30")
    mask1 = data["timestamp"] < U25
    data.loc[mask1, "USA IR"] = 1.5

    U26 = pd.Timestamp("2017-12-13 23:30:00+05:30")
    mask1 = data["timestamp"] < U26
    data.loc[mask1, "USA IR"] = 1.25

    U27 = pd.Timestamp("2017-06-14 23:30:00+05:30")
    mask1 = data["timestamp"] < U27
    data.loc[mask1, "USA IR"] = 1.0

    U28 = pd.Timestamp("2017-03-15 23:30:00+05:30")
    mask1 = data["timestamp"] < U28
    data.loc[mask1, "USA IR"] = 0.75

    U29 = pd.Timestamp("2016-12-14 23:30:00+05:30")
    mask1 = data["timestamp"] < U29
    data.loc[mask1, "USA IR"] = 0.5

    U30 = pd.Timestamp("2015-12-16 23:30:00+05:30")
    mask1 = data["timestamp"] < U30
    data.loc[mask1, "USA IR"] = 0.25

    print(data)
    data.drop(columns=['volume','High','Low','Open'], inplace=True)
    data.to_csv("USD-JPY-with-IR.csv", index=False)

add_Japan_interest_rate()