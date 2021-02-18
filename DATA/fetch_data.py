import pandas as pd
import pandas_datareader.data as web

def fetch(name,data_source,startDate,endDate,API_KEY):
    try:
        dataframe = web.DataReader(
            name=name,
            data_source=data_source,
            start=startDate,
            end=endDate,
            api_key=API_KEY
        )

        return dataframe.reset_index()
    
    except Exception as e:
        print('FETCH DATA',e)
        return e

    