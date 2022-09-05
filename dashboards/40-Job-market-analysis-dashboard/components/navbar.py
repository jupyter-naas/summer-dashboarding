from asyncore import read
import dash_bootstrap_components as dbc
from setup import read_config

config = read_config()

def get_navbar():
    return   dbc.NavbarSimple(brand = config['app']['APP_NAME'],
                children=[
                    # dbc.NavItem(dbc.NavLink("Home", href="/")),
                    dbc.NavItem(dbc.NavLink("Developers", href="https://www.github.com/anochima", target='blank')),
                ], 
                # set navbar background color
                color="#cbf2d2",
            )