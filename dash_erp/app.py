from dash import (
    Dash,
    html,
    dcc,
    page_container,
    Input,
    Output,
    State,
    callback,
)
import dash_bootstrap_components as dbc
from dash_erp.components.sidebar import create_sidebar
from dash_erp.components.Create import get_view

app = Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    url_base_pathname="/dash/",
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
    ],
)
server = app.server

app.layout = html.Div(
    [
        dcc.Store(id="sales-refresh", data=0),
        dcc.Store(id="open-sale-request"),
        create_sidebar(),
        html.Div(
            page_container,
            id="main-content",
            className="main-content",
        ),
        get_view(),
        dbc.Alert(
            id="app-alert",
            is_open=False,
            duration=3000,
            className="mt-3",
        ),
    ]
)

@callback(
    Output("sidebar", "className"),
    Output("main-content", "className"),
    Input("sidebar-toggle", "n_clicks"),
    State("sidebar", "className"),
    prevent_initial_call=True,
)
def toggle_sidebar(n_clicks, sidebar_class):
    if "collapsed" in sidebar_class:
        return "sidebar", "main-content"

    return "sidebar collapsed", "main-content collapsed"

if __name__ == "__main__":
    app.run(debug=True)