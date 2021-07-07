import datetime as dt
import matplotlib.pyplot as plt
import pandas_datareader as web
import pandas
from pandas_datareader import data as pdr
import yfinance as yfin

plt.style.use("dark_background")
yfin.pdr_override()

#Moving Averages
ma_1 = 35
ma_2 = 120

start = dt.datetime.now() - dt.timedelta(days=360 * 3)
end = dt.datetime.now()

# data = web.DataReader('RCL', 'yahoo', start, end)
# print(data)

data = pdr.get_data_yahoo("RCL", start=start, end=end)
# print(data)
data[f'SMA_{ma_1}'] = data['Adj Close'].rolling(window=ma_1).mean()
data[f'SMA_{ma_2}'] = data['Adj Close'].rolling(window=ma_2).mean()

data = data.iloc[ma_2:]

plt.plot(data['Adj Close'], label="Share Price", color="lightgrey")
plt.plot(data[f'SMA_{ma_1}'], label=f"SMA_{ma_1}", color="orange")
plt.plot(data[f'SMA_{ma_2}'], label=f"SMA_{ma_2}", color="blue")
plt.legend(loc="upper left")
plt.show()

buy_signals = []
sell_signals = []
trigger = 0

for x in range(len(data)):
    if data[f'SMA_{ma_1}'].iloc[x] > data[f'SMA{ma_2}'].iloc[x] and trigger != 1:
