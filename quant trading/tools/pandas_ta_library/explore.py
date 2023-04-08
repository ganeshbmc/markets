import pandas as pd
import pandas_ta as ta
import talib
import yfinance as yf
import numpy as np
import  matplotlib.pyplot as plt
import seaborn as sns

# Get data the first time

# df = pd.DataFrame()
# df = df.ta.ticker("^NSEI")
# print(df.shape)
# df.to_csv("nifty_daily_07042023.csv")

# Import data from local file
df = pd.read_csv("/home/ganesh/Github/markets/quant trading/tools/pandas_ta_library/nifty_daily_07042023.csv")
# print(df.tail())

df.ta.sma(length=20, append=True)
df.ta.ema(length=20, append=True)
df.ta.adx(length=14, append=True)
df.ta.rsi(length=14, append=True)
print(df.tail())

sns.lineplot(df.RSI_14)