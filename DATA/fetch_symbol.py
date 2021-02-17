import pandas as pd
from datapackage import Package

def lst_sym(json_pack):
    res = Package(json_pack)
    try:
        for resource in res.resources:
            if(resource.descriptor['datahub']['type'] == 'derived/csv'):
                data = resource.read()
                df = pd.DataFrame(data,columns=['STOCK','1','2','3','4','5','6'])
                if(len(df)):
                    return df['STOCK'].values
                else:
                    break
        return False

    except Exception as e:
        print('Connection_ERR',e)
        return False


def off_sym(csv):
    df = pd.read_csv(csv)
    return df['STOCK'].values