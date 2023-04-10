from breeze_connect import BreezeConnect
import pandas as pd
import numpy as np
import datetime as dt
import breeze_connect

class Fetcher():
    def __init__(self, token: int) -> None:
        # Initialize client
        self.client = BreezeConnect(api_key="06890j43os6a521A7b7241i934KQ9S56")
        self.client.generate_session(api_secret="$42367K2z98758S712349896J6i^64Mx", 
                              session_token=token)
        return
    
    def get_ohlcv(self, stock_code: str, interval: str, from_date: str, to_date: str) -> pd.DataFrame:
            # Fetch data using client
            data_dict = self.client.get_historical_data(interval=interval, 
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