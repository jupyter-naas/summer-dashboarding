from setup import read_config

# Import components
from components.navbar import get_navbar
from components.card_body import card_body

# import dash and plotly
import dash_bootstrap_components as dbc
from dash import Dash, html
import plotly.express as px

# setup config
config = read_config()
PORT = config['server']['port']
HOST = config['server']['host']
DEBUG = config['app']['APP_DEBUG']

# setup stylesheet for app
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# set app title, uses app name from config file
app.title = config['app']['app_name']

# get the navbar from components/navbar.py
nav = get_navbar()
card_body = card_body()

# set the layout of the app
app.layout = html.Div([nav, card_body])


# start the app
if __name__ == '__main__':
    try:
        app.run_server(debug=DEBUG, host=HOST, port=PORT)
    except Exception as e:
        print(e)
        print('Error: Unable to start app. Check config file.')
        # RUN APP ON HOST 8080
        # python3 app.py
        # visit http://localhost:8080/ in your web browser.

