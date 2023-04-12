import pandas as pd

# from core.functions import get_data
# print("import successful")

# with open('token_breeze.md', 'r', encoding='utf-8') as file:
#     contents = file.readlines()
#     token = contents[0]
#     print(token)
#     print(type(token))

logic = {'Open'  : 'first',
         'High'  : 'max',
         'Low'   : 'min',
         'Close' : 'last',
         'Volume': 'sum'}

# offset = pd.offsets.timedelta(days=-6)

f = pd.read_clipboard(parse_dates=['Date'], index_col=['Date'])
df = f.resample('W').apply(logic)
df.index -= pd.tseries.frequencies.to_offset("6D")

print(df)
