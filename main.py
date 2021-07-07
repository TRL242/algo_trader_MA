import datetime as dt
import matplotlib.pyplot as plt
import pandas_datareader as web
import pandas
from pandas_datareader import data as pdr
import yfinance as yfin

yfin.pdr_override()

#Moving Averages
ma_1 = 35
ma_2 = 120

# start = dt.datetime.now() - dt.timedelta(days=360 * 3)
# end = dt.datetime.now()
#
# data = web.DataReader('RCL', 'yahoo', start, end)
# print(data)

start = dt.datetime.now() - dt.timedelta(days=360 * 3)
end = dt.datetime.now()

data = pdr.get_data_yahoo("RCL", start=start, end=end)
print(data)

