import pandas as pd
import numpy as np
import datetime as dt
import breeze_connect
from breeze_connect import BreezeConnect

def get_data_using_breeze(token: int, stock_code: str, interval: str, from_date: str, to_date: str) -> pd.DataFrame:
    # Initialize client
    isec = BreezeConnect(api_key="06890j43os6a521A7b7241i934KQ9S56")
    isec.generate_session(
    api_secret="$42367K2z98758S712349896J6i^64Mx",
    session_token=token)

    # Fetch data using client
    data_dict = isec.get_historical_data(interval=interval, 
                                        from_date=from_date, 
                                        to_date=to_date,
                                        stock_code=stock_code,
                                        exchange_code="NSE",
                                        product_type="",
                                        expiry_date="")
    df = pd.DataFrame(data_dict["Success"])
    df = df[['datetime', 'open', 'high', 'low', 'close', 'volume']]
    df["datetime"] = pd.to_datetime(df["datetime"], format="%Y-%m-%d %H:%M:%S")
    df[['open', 'high', 'low', 'close', 'volume']] = df[['open', 'high', 'low', 'close', 'volume']].astype(float)
    return df
