import dash_core_components as dcc
import dash_html_components as html
import json
from DATA.fetch_symbol import lst_sym,off_sym
from layout_conf import HEADER_DIV_ID, DROPDOWN_TITLE, DROPDOWN_ID, DATEPICKER_TITLE, DATEPICKER_ID, FIGURE_TITLE, FIGURE_ID,BUTTON_ID,BACKGROUND_DIV,DROPDOWN_TS,DROPDOWN_TS_ID
from datetime import date

class LAYT:
    def __init__(self,csv,pack):
        self.csv = csv
        self.pack = pack

    def FullLayout(self):
        try:
            print(self.pack)
            DF = lst_sym(json.load(open(self.pack)))
            if(not DF):
                DF = off_sym(self.csv)
                print(DF)

        except Exception as e:
            DF = off_sym(self.csv)
            print(e)
            
        return html.Div(children=
            [
                html.Div(id="output-clientside"),
                html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H1(
                                        "Stock Comparision",
                                        
                                    ),
                                    html.H3(
                                        "Overview", style={"margin-top": "0px"}
                                    ),
                                    
                                ],
                                
                            )
                        ],
                        className="one-half column",
                        id="title",
                        style={
                                    "margin-left":"auto",
                                    "margin-right":"auto",
                                },
                    ),
                ],
                    id="header",
                    className="row flex-display",
                    style={"margin-bottom": "25px"},
                ),


                html.Div(
                    [
                        html.Div(
                                [
                                    html.P(
                                        "Filter Class", 
                                        className="control_label"
                                        ),
                                    dcc.Dropdown(
                                        id=DROPDOWN_TS_ID,
                                        multi=False,
                                        options=[   {"label": item ,"value":item} for item in ['av-intraday','av-daily','av-daily-adjusted','av-weekly','av-weekly-adjusted','av-monthly','av-monthly-adjusted','av-forex-daily']],
                                        value='av-daily',
                                        className="dcc_control",  
                                        # labelStyle={"display": "inline-block"},        
                                    ),
                                    html.P(
                                        "Select Date Range:",
                                        className="control_label",
                                    ),
                                    dcc.DatePickerRange(
                                        id=DATEPICKER_ID,
                                        min_date_allowed=date(2010,8,5),
                                        max_date_allowed=date(2021,2,18),
                                        initial_visible_month=date(2020,1,1),
                                        start_date=date(2020,1,1),
                                        end_date=date(2020,1,30),
                                        className="dcc_control" ,                          
                                    ),
                                    html.P("Pick Stocks", className="control_label"),
                                    dcc.Dropdown(
                                        id=DROPDOWN_ID,
                                        multi=True,
                                        style={'height':40},
                                        options=[{"label": '('+row[1][0]+") "+row[1][1], "value":row[1][0]} for row in DF.iterrows()],
                                        value="AAPL",
                                        className="dcc_control",
                                    ),                
                                ],
                                className="pretty_container four columns",
                                id="cross-filter-options",
                            ),
                            html.Div(
                            [
                                html.Div(
                                    [dcc.Graph(id=FIGURE_ID)],
                                    id="countGraphContainer",
                                    className="pretty_container",
                                ),
                            ],
                            id="right-column",
                            className="eight columns",
                            
                            ),
                    ],
                    className="row flex-display",
            ),

        ],
        id='mainContainer',
        style={"display": "flex", "flex-direction": "column"},
    )