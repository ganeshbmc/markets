from functions.breeze import *
print("import successful")

# df = get_data.get_data_using_breeze(7622102, "NIFTY", "1day", "2018-04-01", "2023-03-31")
# print(df)

# d = Data(1)
# print(d.get_data(10))

f = Fetcher(7734262)
# nifty = f.get_ohlcv("NIFTY", "1day", "2022-04-01", "2023-03-31")
# print(nifty)

# vix = f.get_ohlcv("INDVIX", "1day", "2022-04-01", "2023-03-31")
# print(vix)

finnifty = f.get_ohlcv("NIFFIN", "1day", "2022-04-01", "2023-03-31")
print(finnifty)