from dash import (
    dcc,
    Input,
    html,
    Output,
    State,
    callback,
    ctx,
    no_update
)
from datetime import datetime
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from dash_erp.repositories.sales_repository import SalesRepository

sales_repository = SalesRepository()

def get_view():
    return dbc.Modal(
        [
            dbc.ModalHeader(
                dbc.ModalTitle(
                    id="form-modal-title"
                )
            ),

            dbc.ModalBody(
                [
                    dbc.Label("Region"),
                    dbc.Input(
                        id="form-region",
                        placeholder="North",
                    ),

                    html.Br(),

                    dbc.Label("Date"),
                    dcc.DatePickerSingle(
                        id="form-date",
                        display_format="YYYY-MM-DD",
                    ),

                    html.Br(),
                    html.Br(),

                    dbc.Label("Revenue"),
                    dbc.Input(
                        id="form-revenue",
                        type="number",
                        placeholder="0.00",
                    ),

                    html.Div(
                        id="form-error",
                        className="text-danger mt-3",
                    ),

                    dcc.Store(
                        id="editing-id"
                    ),
                ]
            ),

            dbc.ModalFooter(
                [
                    dbc.Button(
                        "Cancel",
                        id="btn-cancel-form",
                        color="secondary",
                    ),

                    dbc.Button(
                        "Save",
                        id="btn-save",
                        color="primary",
                    ),
                ]
            ),
        ],
        id="form-modal",
        is_open=False,
    )

@callback(
    Output("form-modal",       "is_open"),
    Output("form-modal-title", "children"),
    Output("form-region",      "value"),
    Output("form-date",        "date"),
    Output("form-revenue",     "value"),
    Output("editing-id",       "data"),
    Output("sales-refresh",    "data"),
    Output("app-alert",       "children"),
    Output("app-alert",       "is_open"),


    Input("open-sale-request", "data"),
    Input("btn-cancel-form", "n_clicks"),
    Input("btn-save", "n_clicks"),


    State("form-region", "value"),
    State("form-date", "date"),
    State("form-revenue", "value"),
    State("editing-id", "data"),
    State("sales-refresh", "data"),
    prevent_initial_call=True,
)
def handle_sale_form(
    request,
    cancel_clicks,
    save_clicks,
    region,
    date_value,
    revenue,
    editing_id,
    refresh_count,
):
    triggered = ctx.triggered_id

    # ABRIR
    if triggered == "open-sale-request":
        return (
            True,       # is_open
            "Create Sale",
            "",         # region
            None,       # date
            None,       # revenue
            None,       # editing-id
            no_update,  # sales-refresh
            no_update,
            no_update,
        )

    # CANCELAR
    if triggered == "btn-cancel-form":
        return (
            False,
            no_update,
            no_update,
            no_update,
            no_update,
            no_update,
            no_update,
            no_update,
            no_update,
        )

    # GUARDAR
    if triggered == "btn-save":
        print("btn-save")

        if not region or not date_value or revenue is None:
            return (
                True,
                no_update,
                no_update,
                no_update,
                no_update,
                no_update,
                no_update,
                "Complete all fields.",
                True
            )

        sale = {
            "region": region,
            "date": datetime.fromisoformat(date_value),
            "revenue": float(revenue),
        }

        if editing_id:
            sales_repository.update(
                editing_id,
                sale,
            )
            message = "Sale updated."
        else:
            sales_repository.create(
                sale,
            )
            message = "Sale created."

        return (
            False,
            no_update,
            no_update,
            no_update,
            no_update,
            no_update,
            (refresh_count or 0) + 1,
            message,
            True
        )

    raise PreventUpdate