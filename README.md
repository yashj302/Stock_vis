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
    * These are experimental if using Free tier `heroku ps:scale web=1`
    * Deployment will be on url : `https://<unique_name>.herokuapp.com`
    * The next step is setting up api key you can get Free API Key from `https://www.alphavantage.co/`
    * heroku config:set ALPHAVAN=`<APIKEY>`


#### Currently running on heroku: https://stocks-visualize.herokuapp.com/


#
### Build Docker Image
- Replace `<API_KEY>` in Dockerfile with your own API Key
- Have docker installed on your system and build using command `docker build -t <any_name> .`  use dot(.) if dockerfile present in same folder. This name will be used as image_name.
- For run `docker run --name <suitablename> -p 8050:8050 <image_name>` port number can be changed in `server.py` and dockerfile and in run command.