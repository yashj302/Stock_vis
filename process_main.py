import plotly.graph_objs as go
from DATA.fetch_data import fetch
import os
from datetime import datetime
from conf import API
def process(symbol,start,end,timeseries):
    CHART = dict()
    if(isinstance(symbol,str)):
        symbol = [symbol]
    start = start.split('-')
    start = datetime(int(start[0]),int(start[1]),int(start[2]))

    end = end.split('-')
    end = datetime(int(end[0]),int(end[1]),int(end[2]))

    for stock in symbol:
        DF = fetch(
            name=stock,
            data_source=timeseries,
            startDate=start,
            endDate=end,
            API_KEY=os.getenv(API))

        CHART[stock] = DF

    figure = {
        'data':[

            go.Scatter(
                x = v['index'],
                y = v['open'],
                mode='lines',
                text=k,
                name=k,
                hoverinfo='text+x+y'
            )

            for k,v in CHART.items()
        ],

        'layout': go.Layout(
            title="Stock chart for {}".format(', '.join(symbol)),
            hovermode='closest',
            xaxis={'title':'Date'},
            yaxis={'title':'Open Value'}
        )
    }
    

    return figure
