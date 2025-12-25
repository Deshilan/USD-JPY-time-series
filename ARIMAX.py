from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error
import Data_import
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
import pandas as pd

def arimax():
    data = Data_import.hours_with_IR()
    data = data.iloc[:-1]
    split = int(len(data) * 0.95)
    train, test = data[:split], data[split:]
    exog_var_train = train[['JapanIR', 'USAIR']]
    exog_var_test = test[['JapanIR', 'USAIR']]
    exog_var_train.std()

    model = SARIMAX(train['Close'], order=(60,1, 1), exog=exog_var_train, seasonal_order=(0, 0, 0, 0))

    model_fit = model.fit()
    forecast = model_fit.forecast(len(test), exog=exog_var_test)
    print(forecast)
    plt.figure(figsize=(12, 8))
    plt.plot(test['Close'], color='blue', label='Test')
    plt.plot(forecast, color='red', label='Forecast')
    plt.show()

arimax()

#In my opinion ARIMAX doesn't make much more sense than ARIMA- probably due to lack of some significant changes in
#added exogs; in other words, it will give similar results to classic ARIMA.