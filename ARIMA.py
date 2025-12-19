from Data_import import hours_dataset, cleared_data
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
import pandas as pd

def arima_test(start, end):
    pure_data = cleared_data()
    pure_data = pure_data[start:end]
    pure_data.index = pd.to_datetime(pure_data.index)
    pure_data = pure_data.asfreq("min")
    data = pure_data['Close']
    split = int(len(data)*0.8)
    train, test = data[:split], data[split:]

    model = ARIMA(train, order=(30,0,1))
    res = model.fit()
    print(res.summary())


    forecast_res = res.get_forecast(steps=len(test))
    pred = forecast_res.predicted_mean
    ci = forecast_res.conf_int()

    # Wykres
    plt.figure(figsize=(12, 5))
    plt.plot(train, label="train")
    plt.plot(test, label="test")
    plt.plot(pred, label="forecast")
    plt.fill_between(ci.index, ci.iloc[:, 0], ci.iloc[:, 1], alpha=0.1)
    plt.legend()
    plt.show()

arima_test(0, 300)