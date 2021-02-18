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
            
        return html.Div(id='HEAD',children=[
            html.H1('Stock Comparison Graph'),
            html.Div(id=DROPDOWN_TITLE,children=[
                
                html.H3("Dropdown Multi"),
                dcc.Dropdown(id=DROPDOWN_ID,
                            multi=True,
                            style={'height':40},
                            options=[{"label": '('+row[1][0]+") "+row[1][1], "value":row[1][0]} for row in DF.iterrows()],
                            value="AAPL"
                            )
                
                ],style={'display':'inline-block','float':'left','width':'30%'}),

                html.Div(id=DATEPICKER_TITLE,children=[
                
                html.H3("Select range"),
                dcc.DatePickerRange(
                                        id=DATEPICKER_ID,
                                        min_date_allowed=date(2010,8,5),
                                        max_date_allowed=date(2021,2,18),
                                        initial_visible_month=date(2020,1,1),
                                        start_date=date(2020,1,1),
                                        end_date=date(2020,1,30),
                                        style={
                                            'height':40
                                        }
                                    )

                ],style={'float':'middle','margin-left':'8%','width':'25%','display':'inline-block'}),

            html.Div(id=DROPDOWN_TS,children=[
                
                html.H3("Time-Series"),
                dcc.Dropdown(   id=DROPDOWN_TS_ID,
                                multi=False,
                                style={
                                            'height':40
                                        },
                                options=[   {"label": item ,"value":item} for item in ['av-intraday','av-daily','av-daily-adjusted','av-weekly','av-weekly-adjusted','av-monthly','av-monthly-adjusted','av-forex-daily']],
                                value='av-daily'          
                            )

                ],style={'float':'right','margin-right':'10%','width':'25%','display':'inline-block'}),

            html.Div(id=FIGURE_TITLE,children=[
                
                html.H3("Figure"),
                dcc.Graph(id=FIGURE_ID)
                ],style={'width':'100%'}),

            ])