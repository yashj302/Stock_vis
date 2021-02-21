import os,sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from process_main import process
import dash
from dash.dependencies import Input,Output,State
import conf
from Layout_dash import LAYT
app = dash.Dash()
# deployment = app.server
from layout_conf import *
import dash_core_components as dcc
layt = LAYT(conf.csv,conf.pack)

app.layout = layt.FullLayout
@app.callback(
    Output(FIGURE_ID,'figure'),
    [
        Input(DROPDOWN_ID,'value'),
        Input(DATEPICKER_ID,'start_date'),
        Input(DATEPICKER_ID,'end_date'),
        Input(DROPDOWN_TS_ID,'value')
    ]
)
def follow(symbol,start,end,timeseries):
    figure = process(symbol,start,end,timeseries)
    return figure

if __name__=='__main__':
    app.run_server(host='0.0.0.0',port='8050',debug=conf.debug)