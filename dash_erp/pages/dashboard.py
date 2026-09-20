from dash import (
    html,
    dcc,
    Input,
    Output,
    callback,
    register_page
)
import pandas as pd
import plotly.express as px
from dash_erp.repositories.sales_repository import SalesRepository


register_page(
    __name__,
    path="/",
    name="Dashboard",
)


sales_repository = SalesRepository()


def layout():
    try:
        regions = sales_repository.get_regions()

    except Exception:
        regions = []

    return html.Div(
        [
            html.H1("Sales Dashboard"),

            dcc.Dropdown(
                id="region-filter",
                options=[
                    {
                        "label": region,
                        "value": region,
                    }
                    for region in regions
                ],
                placeholder="Select region",
            ),

            html.Br(),

            dcc.DatePickerRange(
                id="date-filter",
            ),

            html.Br(),

            dcc.Graph(
                id="sales-chart",
            ),
        ]
    )


@callback(
    Output(
        "sales-chart",
        "figure",
    ),
    Input(
        "region-filter",
        "value",
    ),
    Input(
        "date-filter",
        "start_date",
    ),
    Input(
        "date-filter",
        "end_date",
    ),
    Input(
        "sales-refresh",
        "data",
    ),
)
def update_chart(
    region,
    start_date,
    end_date,
    refresh_count,
):
    start = (
        pd.to_datetime(start_date).to_pydatetime()
        if start_date
        else None
    )

    end = (
        pd.to_datetime(end_date).to_pydatetime()
        if end_date
        else None
    )

    try:
        documents = sales_repository.find_sales(
            region=region,
            start_date=start,
            end_date=end,
        )

    except Exception:
        return px.line(
            title="Database unavailable"
        )

    df = pd.DataFrame(documents)

    if df.empty:
        return px.line(
            title="No data"
        )

    df["date"] = pd.to_datetime(
        df["date"]
    )

    return px.line(
        df,
        x="date",
        y="revenue",
        title="Revenue Over Time",
    )