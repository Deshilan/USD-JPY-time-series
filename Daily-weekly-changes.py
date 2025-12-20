import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import Data_import


def daily_changes_per_minute():
    res = [0] * 1440
    nb = 1440
    for x in range(10):
        old_data = Data_import.one_day1(x)
        data = Data_import.one_day1(x + 1)
        for y in range(nb):
            if y == 0:
                res[y] = res[y] + abs((data[y] - old_data[-1]))
            else:
                res[y] = res[y] + abs((data[y] - data[y - 1]))

    for m in range(len(res)):
        res[m] = res[m] / 10

    plt.plot(res)
    plt.show()


daily_changes_per_minute()


def weekly_changes_per_minute():
    res = [0] * (1440 * 5)
    for x in range(100):
        idx = x + 100
        old_data = Data_import.one_week1(idx)
        data = Data_import.one_week1(idx + 1)
        nb = len(data)
        for y in range(nb):
            if y == 0:
                res[y] = res[y] + abs((data[y] - old_data[-1]))
            else:
                res[y] = res[y] + abs((data[y] - data[y - 1]))

    for x in range(len(res)):
        res[x] = res[x] / 100

    plt.plot(res)
    plt.show()

#weekly_changes_per_minute()