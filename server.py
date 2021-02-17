import dash
from dash.dependencies import Input,Output,State
import conf
from Layout_dash import LAYT

app = dash.Dash()

layt = LAYT(conf.csv,conf.pack)

app.layout = layt.FullLayout

if __name__=='__main__':
    app.run_server(debug=conf.debug)