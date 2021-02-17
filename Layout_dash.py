import dash_core_components as dcc
import dash_html_components as html
import json
from DATA.fetch_symbol import lst_sym,off_sym
from layout_conf import HEADER_DIV_ID, DROPDOWN_TITLE, DROPDOWN_ID, DATEPICKER_TITLE, DATEPICKER_ID, FIGURE_TITLE, FIGURE_ID,BUTTON_ID,BACKGROUND_DIV

class LAYT:
    def __init__(self,csv,pack):
        self.csv = csv
        self.pack = pack

    def call(self):
        return None

    def FullLayout(self):

        return html.Div([

            html.Div(
                children = [
                    html.H1("Stock Graphs")
                    
                        ],  

             style={       
                'fontFamily':'helvetica',
                'fontSize':18
                   }
            ),

            html.Div(

            ),

            html.Div(

            ),

            html.Div(

            )
        
        ],style={
                'width':'100%',
                # 'height':'100%', 
                # 'background-image':'url("/assets/mountain.png")',
                # 'background-repeat': 'center',
                # 'background-position': 'right top',
                # 'background-size': 'cover'   
                # 'fontFamily':'helvetica',
                # 'fontSize':18

        })
