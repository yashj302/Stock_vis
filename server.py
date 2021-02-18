import os,sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

import dash
from dash.dependencies import Input,Output,State
import conf
from Layout_dash import LAYT

app = dash.Dash()

layt = LAYT(conf.csv,conf.pack)

app.layout = layt.FullLayout

if __name__=='__main__':
    app.run_server(debug=conf.debug)