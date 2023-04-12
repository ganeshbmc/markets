import pandas as pd

def resample_day_to_week(df_daily: pd.DataFrame) -> pd.DataFrame:
    logic = {'open'  : 'first',
            'high'  : 'max',
            'low'   : 'min',
            'close' : 'last',
            'volume': 'sum'}

    df_weekly = df_daily.resample('W').apply(logic)
    df_weekly.index -= pd.tseries.frequencies.to_offset("6D")

    return df_weekly
