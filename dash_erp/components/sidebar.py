import dash_bootstrap_components as dbc
from dash_erp.components.Create import (get_view)
from dash import (
    html,
    Input,
    Output,
    callback
)
def create_sidebar():
    return html.Div(
        id="sidebar",
        className="sidebar",
        children=[
            html.Div(
                [
                    html.H4("ERP", id="sidebar-title"),

                    html.Button(
                        "☰",
                        id="sidebar-toggle",
                        n_clicks=0,
                        className="sidebar-toggle",
                    ),
                ],
                className="sidebar-header",
            ),

            html.Hr(),

            dbc.Nav(
                [
                    dbc.NavLink(
                        [
                            html.Span("📊", className="menu-icon"),
                            html.Span("Dashboard", className="menu-text"),
                        ],
                        href="/",
                        active="exact",
                    ),

                    dbc.NavLink(
                        [
                            html.Span("ℹ️", className="menu-icon"),
                            html.Span("About", className="menu-text"),
                        ],
                        href="/about",
                        active="exact",
                    ),

                    dbc.NavLink(
                        [
                            html.Span("✉️", className="menu-icon"),
                            html.Span("Contact", className="menu-text"),
                        ],
                        href="/contact",
                        active="exact",
                    ),
                    dbc.NavLink(
                        [
                            html.Span("🧾", className="menu-icon"),
                            html.Span("Sales CRUD", className="menu-text"),
                        ],
                        href="/sales-crud",
                        active="exact",
                    ),
                    dbc.NavLink(
                        [
                            html.Span("🧾", className="menu-icon"),
                            html.Span("Travel", className="menu-text"),
                        ],
                        href="/travel",
                        active="exact",
                    ),
                    dbc.NavLink(
                        [
                            html.Span("🧾", className="menu-icon"),
                            html.Span("Line", className="menu-text"),
                        ],
                        href="/line",
                        active="exact",
                    ),
                    dbc.NavLink(
                        [
                            html.Span("🧾", className="menu-icon"),
                            html.Span("Survey", className="menu-text"),
                        ],
                        href="/survey",
                        active="exact",
                    ),
                    dbc.NavLink(
                        [
                            html.Span("🧾", className="menu-icon"),
                            html.Span("Weather", className="menu-text"),
                        ],
                        href="/weather",
                        active="exact",
                    ),
                    dbc.NavLink(
                        [
                            html.Span("➕", className="menu-icon"),
                            html.Span("New Sale", className="menu-text"),
                        ],
                        id="open-sale-modal",
                    )
                ],
                vertical=True,
                pills=True,
            ),

            html.Div(
                id="sidebar-resizer",
                className="sidebar-resizer",
            ),
        ],
    )


@callback(
    Output("open-sale-request", "data", allow_duplicate=True),
    Input("open-sale-modal", "n_clicks"),
    prevent_initial_call=True,
)
def open_from_sidebar(n):
    return {
        "action": "create",
        "source": "sidebar",
    }