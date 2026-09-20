from dash import (
    html,
    Input,
    Output,
    State,
    callback,
    dash_table,
    register_page,
    ctx,
)
import dash_bootstrap_components as dbc
from bson import ObjectId
from datetime import datetime
from dash_erp.repositories.sales_repository import SalesRepository

register_page(
    __name__,
    path="/sales-crud",
    name="Sales CRUD",
)

sales_repository = SalesRepository()

def load_sales():
    documents = sales_repository.find_all()

    rows = []

    for doc in documents:
        rows.append(
            {
                "id": str(doc["_id"]),
                "region": doc.get("region", ""),
                "date": (
                    doc.get("date").strftime("%Y-%m-%d")
                    if isinstance(doc.get("date"), datetime)
                    else str(doc.get("date", ""))
                ),
                "revenue": doc.get("revenue", 0),
            }
        )

    return rows


layout = dbc.Container(
    [
        html.H1(
            "Sales CRUD",
            className="mb-4",
        ),

        dbc.Row(
            [
                dbc.Col(
                    dbc.Button(
                        "➕ Add Sale",
                        id="btn-open-create",
                        color="primary",
                    ),
                    width="auto",
                ),

                dbc.Col(
                    dbc.Button(
                        "🗑 Delete Selected",
                        id="btn-open-delete",
                        color="danger",
                        disabled=True,
                    ),
                    width="auto",
                ),
            ],
            className="mb-3",
        ),

        dash_table.DataTable(
            id="sales-table",

            columns=[
                {
                    "name": "Region",
                    "id": "region",
                },
                {
                    "name": "Date",
                    "id": "date",
                },
                {
                    "name": "Revenue",
                    "id": "revenue",
                    "type": "numeric",
                },
            ],

            data=load_sales(),

            row_selectable="multi",

            selected_rows=[],

            page_size=10,

            sort_action="native",

            filter_action="native",

            style_table={
                "overflowX": "auto",
            },

            style_header={
                "fontWeight": "bold",
            },

            style_cell={
                "padding": "10px",
                "textAlign": "left",
            },
        ),
        #
        # DELETE CONFIRMATION
        #
        dbc.Modal(
            [
                dbc.ModalHeader(
                    dbc.ModalTitle(
                        "Confirm deletion"
                    )
                ),

                dbc.ModalBody(
                    id="delete-confirm-text"
                ),

                dbc.ModalFooter(
                    [
                        dbc.Button(
                            "Cancel",
                            id="btn-cancel-delete",
                            color="secondary",
                        ),

                        dbc.Button(
                            "Delete",
                            id="btn-confirm-delete",
                            color="danger",
                        ),
                    ]
                ),
            ],
            id="delete-modal",
            is_open=False,
        ),

        #
        # FEEDBACK
        #

    ],
    fluid=True,
)

@callback(
    Output(
        "btn-open-delete",
        "disabled",
    ),
    Input(
        "sales-table",
        "selected_rows",
    ),
)
def enable_delete_button(selected_rows):
    return not bool(selected_rows)

@callback(
    Output("sales-table", "data"),
    Input("sales-refresh", "data"),
)
def refresh_sales_table(_):
    return load_sales()

@callback(
    Output(
        "delete-modal",
        "is_open",
    ),

    Output(
        "delete-confirm-text",
        "children",
    ),

    Input(
        "btn-open-delete",
        "n_clicks",
    ),

    Input(
        "btn-cancel-delete",
        "n_clicks",
    ),

    State(
        "sales-table",
        "selected_rows",
    ),

    State(
        "delete-modal",
        "is_open",
    ),

    prevent_initial_call=True,
)
def toggle_delete_modal(
    open_clicks,
    cancel_clicks,
    selected_rows,
    is_open,
):

    triggered = ctx.triggered_id

    if triggered == "btn-open-delete":

        count = len(
            selected_rows or []
        )

        return (
            True,
            f"Delete {count} selected sale(s)?"
        )

    if triggered == "btn-cancel-delete":

        return (
            False,
            ""
        )

    return (
        is_open,
        ""
    )

@callback(
    Output("sales-table",    "data",             allow_duplicate=True),
    Output("sales-table",    "selected_rows"),
    Output("delete-modal",   "is_open",          allow_duplicate=True),
    Output("app-alert",      "children",         allow_duplicate=True),
    Output("app-alert",      "color",            allow_duplicate=True),
    Output("app-alert",      "is_open",          allow_duplicate=True),

    Input(
        "btn-confirm-delete",
        "n_clicks",
    ),

    State(
        "sales-table",
        "selected_rows",
    ),

    State(
        "sales-table",
        "data",
    ),

    prevent_initial_call=True,
)
def delete_sales(
    n_clicks,
    selected_rows,
    table_data,
):
    if not selected_rows:
        return (
            load_sales(),
            [],
            False,
            "No rows selected.",
            "warning",
            True,
        )

    ids = [
        table_data[index]["id"]
        for index in selected_rows
    ]

    deleted_count = sales_repository.delete_many(ids)

    return (
        load_sales(),
        [],
        False,
        f"{deleted_count} sale(s) deleted.",
        "success",
        True,
    )


from dash.exceptions import PreventUpdate


@callback(
    Output("open-sale-request", "data", allow_duplicate=True),
    Input("btn-open-create", "n_clicks"),
    prevent_initial_call=True,
)
def open_from_crud(n_clicks):
    if not n_clicks:
        raise PreventUpdate

    return {
        "action": "create",
        "source": "crud",
    }