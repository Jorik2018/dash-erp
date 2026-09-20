import dash
import dash_bootstrap_components as dbc
from dash import html


dash.register_page(
    __name__,
    path="/contact",
    name="Contact",
)


layout = html.Div(
    [
        html.H1("Contact"),

        dbc.Input(
            placeholder="Name",
        ),

        html.Br(),

        dbc.Input(
            placeholder="Email",
            type="email",
        ),

        html.Br(),

        dbc.Textarea(
            placeholder="Message",
        ),

        html.Br(),

        dbc.Button(
            "Send",
            color="primary",
        ),
    ]
)