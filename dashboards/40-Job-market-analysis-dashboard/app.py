# import libraries
from html.entities import html5
from setup import read_config
from components.navbar import get_navbar

import dash_bootstrap_components as dbc
from dash import Dash, html
import plotly.express as px
import pandas as pd

# setup config
config = read_config()
PORT = config['server']['port']
HOST = config['server']['host']

# setup stylesheet for app
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# set app title, uses app name from config file
app.title = config['app']['APP_NAME']

# get the navbar from components/navbar.py
nav = get_navbar()

# set the layout of the app
app.layout = html.Div([nav])


# start the app
if __name__ == '__main__':
    app.run_server(debug=True, host=HOST, port=PORT)
    # RUN APP ON HOST 8080
    # python3 app.py
    # visit http://localhost:8080/ in your web browser.

