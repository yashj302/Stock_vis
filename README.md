# Stock_vis

## Stock Visualization and Comparison

_Add Multiple Stocks and Visualize Comparison on Graph_

**Techonlogy Stack**
- Dash
- Plotly
- Pandas Datareader



<br>

### SETUP

_Set an Environment variable "ALPHAVAN" with Api key as Value or You can change API Name in conf and set that Value in Environment._

`pip install -r requirements.txt`

#### For Local run : http://127.0.0.1:8050/

#

### Setup on your own Heroku
- Include `(Remove-#)` line 12 in `server.py`
    (deployment=app.server)
- Include `(Remove-#)` (gunicorn) in `requirement.txt`
- Follow these commands:
    * heroku create `<a unique name>`
    * git add .
    * git commit -m "First Deployment"
    * git push heroku master
    * `These are experimental if using Free tier` heroku ps:scale web=1
    * Deployment will be on url : `https://<unique_name>.herokuapp.com`
    * The next step is setting up api key you can get Free API Key from `https://www.alphavantage.co/`
    * heroku config:set ALPHAVAN=`<APIKEY>`


#### Currently running on heroku: https://stocks-visualize.herokuapp.com/

