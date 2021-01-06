import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
import datetime

start = datetime.datetime(1985, 1, 1)
end = datetime.datetime(2018, 9, 18)


stocks = ["MSFT", "AAPL"]

for stock in stocks:       
    f = web.DataReader('WIKI/' + stock, 'quandl', start, end)
    print(f)
    f.to_csv("Apple Stock Data.csv")