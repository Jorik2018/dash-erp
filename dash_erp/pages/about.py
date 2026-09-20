import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path="/about",
    name="About",
)

layout = html.Div(
    [
        html.H1("About"),
        html.P(
            "Sales dashboard built with "
            "Dash, Poetry and MongoDB Atlas."
        ),
        dbc.Card(
    class_name="one-chart glass-card",
    children=[
        html.Div(
            className="glass-head",
            children=[
                html.H3("Visitors Trend (M)"),
                html.Span("📈 Record 36.9M in 2024", className="chip"),
            ],
        ),
    ]
)
        
    ]
)