from dash import html
import dash_bootstrap_components as dbc

# create a card body component
def card_body():
    card_body = dbc.CardBody(
        [
            html.Div([
                html.H6("Growth"),
                html.P(
                    "This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.",
                    className="card-text",
                ),
                html.P(
                    "Last updated 3 mins ago", className="card-text",
                ),
            ]),

            html.Div([
                html.H6('None')
            ])
        ],
        className="card-body",
    )
    return card_body