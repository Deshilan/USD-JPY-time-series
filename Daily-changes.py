import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import Data_import

for x in range(100):
    res = [0] * 1440
    old_data = Data_import.one_day1(x)
    data = Data_import.one_day1(x+1)
    nb = len(data)
    for y in range(nb):
        if y == 0:
            res = res + (data[y] - old_data[-1])
        else:
            res[y] = res[y] + (data[y]-data[y-1])

print(res)
for x in range(len(res)):
    res[x] = res[x] / 10

plt.plot(res)
plt.show()