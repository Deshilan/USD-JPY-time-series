from Data_import import hours_dataset, cleared_data
from statsmodels.tsa.holtwinters import Holt
import matplotlib.pyplot as plt



def hours_test():
    dataset = hours_dataset()
    data = dataset[:10000]
    split = int(len(data) * 0.8)
    train, test = data[:split], data[split:]
    model = Holt(train)
    fit = model.fit(optimized=True)
    forecast = fit.forecast(len(data[split:]))
    plt.plot(forecast)
    plt.plot(test)
    plt.show()


# Holt has the general property that it can be useful for estimating a trend over a certain period. Intuitively,
# if there are no changes in macroeconomic parameters (most notably inflation / interest rates), then Holt
# can indicate a trend line. As in this example: 4 days (i.e. a period with a low probability of publishing
# important data), and the overall trend is consistent with the results.

def minutes_test():
    dataset = cleared_data()
    data = dataset.Close.values[(300):(600)]
    split = int(len(data) * 0.8)
    train, test = data[:split], data[split:]
    model = Holt(train)
    fit = model.fit(optimized=True)
    forecast = fit.forecast(len(data[split:]))
    results = dataset.Close.values[(600):(620)]
    print(forecast)
    plt.plot(forecast)
    plt.plot(test)
    plt.show()

# It is hard to say here; this requires further testing. The direction of volume movement matches more often than not,
# but there is no talk of any particular regularity.
minutes_test()