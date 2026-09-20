import dash_bootstrap_components as dbc
from dash import (html, dcc, Input, Output, State, callback, MATCH, ctx)
import dash
from dash_erp.figures import (fig_bar, fig_line, 
#fig_map, 
fig_vibe, fig_startups, fig_wave, fig_fuji)

dash.register_page(
    __name__,
    path="/travel",
    name="Travel",
)

hero = dbc.Row(
    [
        dbc.Col(
            dbc.Row(
                dbc.Col(
                    [
                        html.Div("smart travel picks", className="kicker"),
                        html.H1([
                            "Find your next ",
                            html.Span("perfect escape", className="gradient-text"),
                        ], className="mb-3"),
                        html.P(
                            "Plan, compare, and book stunning destinations. "
                            "Get curated recommendations based on season, budget, and vibe.",
                            className="sub mb-4",
                        ),
                        html.Div(
                            className="search",
                            children=[
                                html.Div(
                                    className="field",
                                    children=["📍", dbc.Input(placeholder="Where to? ", type="text", id="where-input")]
                                ),
                                html.Div(
                                    className="field",
                                    children=["📅", dbc.Input(placeholder="Dates (Fri–Sun)", type="text", id="dates-input")]
                                ),
                                html.Div(
                                    className="field",
                                    children=["👥", dbc.Input(placeholder="Guests", type="text", id="guests-input")]
                                ),
                                
                                html.Button("🔍 Explore trips", className="cta", id="explore-btn", n_clicks=0),
                            ],
                        ),
                        html.Div(
                            className="chips",
                            children=[
                                html.Span("🔥 Trending: Mount Fuji", className="chip"),
                                html.Span("🌿 Nature escapes", className="chip"),
                                html.Span("💻 Workations", className="chip"),
                            ],
                        ),
                    ]
                )
            ), md=6
        ),
        dbc.Col(
            dbc.Card(
                className="pick-card",
                children=[
                    dbc.CardBody(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(html.Span("Editor’s pick", className="badge"), width="auto"),
                                    dbc.Col(html.Span("Fri – Sun", className="meta-top"), width="auto"),
                                ],
                                className="pick-head",
                            ),
                            html.H3("Tokyo Weekend", className="pick-title"),
                            html.Div(
                                [
                                    html.Span("🚶 5 activites"),
                                    html.Span("⚖ 2 attractions"),
                                    html.Span("💸 deals: 6"),
                                ],
                                className="pick-facts",
                            ),
                            html.Div(
                                dbc.CardImg(
                                    src="assets/tokyo.png",
                                ),
                                className="pick-illustration",
                            ),      
                        ]
                    )
                ], 
            ), width={"offset" : "1"}, 
        )
    ], className="hero", 
)

top_destination_section = dbc.Row(
    [
        dbc.Col(
            [
                html.H2("🌍 Top Destination This Month", className="topdest-heading"),
                dbc.Card(
                    class_name="topdest-card",
                    children=dbc.CardBody(
                        dbc.Row(
                            children=[
                                dbc.Col(
                                    md=7,
                                    children=[
                                        html.H3("Tokyo, Japan", className="topdest-title"),
                                        html.P(
                                            [
                                                "Tokyo is surging. Japan welcomed ",
                                                html.Strong("36.87M international visitors in 2024"),
                                                ", and 2025 is pacing even faster. At the heart of the buzz: ",
                                                html.Strong("Shibuya Crossing"),
                                                ", where ",
                                                html.Em("1,000–2,500 people cross every two minutes"),
                                                " at peak. With rail hubs like ",
                                                html.Strong("Shibuya Station (3M passengers/day)"),
                                                ", the city compresses nightlife, culture, shopping, and food into a walkable, non-stop experience.",
                                            ],
                                            className="topdest-intro",
                                        ),
                                        html.Ul(
                                            className="topdest-bullets",
                                            children=[
                                                html.Li("🌸 Ideal travel: Spring & Autumn", ),
                                                html.Li("📈 Visitors up +16% YoY", ),
                                                html.Li("🌐 World-class connectivity", ),
                                            ],
                                        ),
                                    ],
                                ),
                                dbc.Col(
                                    md=5,
                                     
                                    children=html.Div(
                                        className="topdest-imagewrap",
                                        children=html.Img(
                                            src="https://plus.unsplash.com/premium_photo-1661914240950-b0124f20a5c1?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                                            className="topdest-image",
                                        ),
                                    ),
                                ),
                            ],
                        )
                    ),
                ),
            ],
            width=12,
        )
    ],
)

# Chart Area

line_chart_section = dbc.Card(
    class_name="one-chart glass-card",
    children=[
        html.Div(
            className="glass-head",
            children=[
                html.H3("Visitors Trend (M)"),
                html.Span("📈 Record 36.9M in 2024", className="chip"),
            ],
        ),
        html.Div(
            children=dcc.Graph(
                figure=fig_line,
                style={"height": "330px"},
                config={"displayModeBar": False, "responsive": True},
            ),
        ),
        
    ],
)

vibe_chart_section = dbc.Card(
    class_name="one-chart glass-card",
    children=[
        html.Div(
            className="glass-head",
            children=[
                html.H3("Vibe Score"),
                html.Span("🌃 Nightlife & 🛍️ Shopping lead", className="chip"),
            ],
        ),
        html.Div(style={"overflow": "hidden","border-radius": "28px","border": "1px solid rgba(255,255,255,.65)"},
            children=dcc.Graph(
                figure=fig_vibe,
                style={"height": "330px"},
                config={"displayModeBar": False, "responsive": True},
            ),
        ),
    ],
)

season_chart_section = dbc.Card(
    class_name="one-chart glass-card",
    children=[
        html.Div(
            className="glass-head",
            children=[
                html.H3("Seasonality (M)"),
                html.Span("✅ Best: July/December", className="chip"),
            ],
        ),
        html.Div(
            children=dcc.Graph(
                figure=fig_bar,
                style={"height": "330px"},
                config={"displayModeBar": False, "responsive": True},
            ),
        ),
    ],
)

map_chart_section = dbc.Card(
    class_name="one-chart glass-card",
    children=[
        html.Div(
            className="glass-head",
            children=[
                html.H3("Where they are"),
                html.Span("🎎 Full Activities", className="chip"),
            ],
        ),
        html.Div(
            children=dcc.Graph(
                #figure=fig_map,
                style={"height": "330px",},
                config={"displayModeBar": False, "responsive": True},
            ),
        ),
        
    ],
)

chart_section = dbc.Row(
    [
        dbc.Col(line_chart_section, md=7),
        dbc.Col(vibe_chart_section, md=5),
        dbc.Col(season_chart_section, md=6),
        dbc.Col(map_chart_section, md=6),
    ],
    className="mt-4 gy-4",
)

# Off-Canvas Shibuya Charts

startup_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("No. of Startups in 23 Wards of Tokyo", className="mb-2"),
            dcc.Graph(figure=fig_startups, config={"displayModeBar": False}, style={"height": "340px"}),
            html.P(
                "Shibuya City is home to the largest collection of startup companies (1,651) in the 23 wards of Tokyo.",
                className="text-muted mb-0",
            ),
        ]
    ),
    class_name="one-chart glass-card"
)


hallowen_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Shibuya Scramble: Hourly Crowd Pulse (Oct 31–Nov 1)", className="mb-2"),
            dcc.Graph(figure=fig_wave, config={"displayModeBar": False}, style={"height": "340px"}),
            html.P(
                "Halloween brings a sudden, short-lived surge of people into Shibuya",
                className="text-muted mb-0",
            ),
        ]
    ),
    class_name="one-chart glass-card"
)


shibuya_contain = dbc.Row(
    [
        dbc.Col(
            [
                html.P(
                    [
                        "Shibuya is the beating heart of Tokyo, a vibrant district where culture, entertainment, and urban energy collide. ",
                        "A 2023 Tokyo survey crowned it the city's top destination, attracting ",
                        html.Strong("67.1% of visitors"),
                        ". Standout attractions include ",
                        html.Strong("SHIBUYA SKY"),
                        ", a stunning 229-meter-high observation deck offering a ",
                        html.Em("breathtaking 360-degree panorama"),
                        ". New developments like the ",
                        html.Strong("Pokemon Center"),
                        " and ",
                        html.Strong("Miyashita Park"),
                        " elevate the area with cutting-edge shopping and dining experiences. Meanwhile, timeless landmarks remain iconic: ",
                        html.Strong("Scramble Crossing"),
                        ", where ",
                        html.Em("thousands of pedestrians surge with every traffic light change"),
                        ", embodies Tokyo’s dynamic spirit. The beloved ",
                        html.Strong("Hachiko statue"),
                        " and the ",
                        html.Strong("Center Street"),
                        " continue to draw crowds, blending nostalgia with the area’s forward-looking energy.",
                    ],
                    className="topdest-intro",
                ),
            ],
            md=7,
        ),
        dbc.Col(
            html.Div(
                html.Img(
                    src="https://images.unsplash.com/photo-1542051841857-5f90071e7989?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                    alt="Neon sign reading Do Something Great",
                    className="topdest-image img-fluid",
                ),
                className="topdest-imagewrap",
            ),
            md=5,
        ),
    ],
    className="mt-3",
)


shibuya_card = dbc.Card(
            className="travel-picks-card",
            
            children=[
                html.Div(
                    className="travel-picks-head",
                    children=[
                        html.Div("92", className="travel-picks-score"),
                        html.Div(
                            children=[
                                html.Div("Shibuya Crossing", className="travel-picks-title"),
                                html.Div(
                                    className="travel-picks-chips",
                                    children=[
                                        html.Span("👥 Crowd: High", className="travel-picks-chip"),
                                        html.Span("🚇 Access: Excellent", className="travel-picks-chip"),
                                        html.Span("💸 Spend: $100–$400", className="travel-picks-chip"),
                                        html.Span("⏰ Peak: 18:00–22:00", className="travel-picks-chip"),
                                    ],
                                ),
                            ]
                        ),
                    ],
                ),
                dbc.Row(
                    class_name="g-2 mt-2 mb-3",
                    children=[
                        dbc.Col(
                            html.Div(
                                [html.Small("Best months", className="text-muted d-block mb-1"),
                                html.Strong("March - May")],
                                className="search"),
                            md=4,
                        ),
                        dbc.Col(
                            html.Div(
                                [html.Small("Vibe", className="text-muted d-block mb-1"),
                                html.Strong("Nightlife • Food • Shopping")],
                                className="search"),
                            md=4,
                        ),
                        dbc.Col(
                            html.Div(
                                [html.Small("Family friendly", className="text-muted d-block mb-1"),
                                html.Strong("Moderate")],
                                className="search"),
                            md=4,
                        ),
                    ],
                ),
                shibuya_contain,
                html.Div(
                    className="travel-picks-actions",
                    children=[
                        dbc.Button(
                            "More",
                            id={"type":"open", "index":"shibuya"},
                            n_clicks=0,
                            class_name="travel-picks-btn",
                        ),
                        dbc.Button(
                            "View deals",
                            id="pick-fuji-deals",
                            n_clicks=0,target="_blank", 
                            href="https://www.skyscanner.co.id/",
                            class_name="travel-picks-score border-0 shadow-0",
                        ),
                    ],
                ),
            ],
        )

#Off Canvas Section

shibuya_offcanvas = dbc.Offcanvas(
    id={"type":"offcanvas", "index":"shibuya"},
    title="Interesting Shibuya Facts",
    placement="end", 
    is_open=False,
    scrollable=True,
    backdrop=True,
    children=[
        dbc.Container(
            fluid=True,
            children=[
                dbc.Row(
                    class_name="g-3",
                    children=[
                        dbc.Col(
                            startup_card,
                            width=12
                        ),
                        dbc.Col(
                            hallowen_card,
                            width=12
                        )
                    ],
                ),
                html.Div(className="mt-3 d-flex gap-2", children=[
                    dbc.Button("Close", id={"type":"close", "index":"shibuya"}, class_name="btn btn-light")
                ])
            ]
        )
    ],
)


#Off canvas fuji

fuji_stats_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Annual Number of Accident Victims (2011–2020)", className="mb-2"),
            dcc.Graph(figure=fig_fuji, config={"displayModeBar": False}, style={"height": "340px"}),
            html.P(
                "Peaks in 2013 (121) and 2016 (111) mark the worst years in the decade.",
                className="text-muted mb-0",
            ),
        ]
    ),
    class_name="one-chart glass-card"
)

fuji_temp_card = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Mount Fuji - Temperature °C ", className="fuji-title"),
            html.Div(className="fuji-titlebar"),
            html.Div(
                    className="fuji-tablewrap",
                    children=html.Table(
                        className="fuji-table",
                        children=[
                            html.Thead(
                                html.Tr([
                                    html.Th("Month", scope="col"),
                                    html.Th(["Average",], scope="col",),
                                    html.Th(["Daily max ", ], scope="col"),
                                    html.Th(["Daily min ",], scope="col"),
                                    html.Th(["Humidity ",], scope="col"),
                                ])
                            ),
                            html.Tbody([
                                html.Tr([
                                    html.Th("July", scope="row", className="month"),
                                    html.Td("5.3", className="num strong"),
                                    html.Td("8.0", className="num strong"),
                                    html.Td("2.8", className="num strong"),
                                    html.Td(html.Span("79", className="humid"), className="num"),
                                ]),
                                html.Tr([
                                    html.Th("August", scope="row", className="month"),
                                    html.Td("6.4", className="num strong"),
                                    html.Td("9.5", className="num strong"),
                                    html.Td("3.8", className="num strong"),
                                    html.Td(html.Span("75", className="humid"), className="num"),
                                ]),
                                html.Tr([
                                    html.Th("September", scope="row", className="month"),
                                    html.Td("3.5", className="num strong"),
                                    html.Td("6.5", className="num strong"),
                                    html.Td("0.6", className="num strong"),
                                    html.Td(html.Span("67", className="humid"), className="num"),
                                ]),
                            ])
                        ],
                    ),
                ),

            html.Small("Japanese Meteorological Association: statistical period 1991 – 2020", className="fuji-note"),
        ]
    ),
    class_name="fuji-card"
)

fuji_contain = dbc.Row(
    [
        dbc.Col(
            [
                html.P(
                    [
                        "Mt. Fuji, Japan’s tallest peak at ",
                        html.Strong("3,776 meters"),
                        ", stands as a spiritual, cultural, and geographical marvel. Formed by volcanic activity ",
                        html.Em("100,000 years ago"),
                        ", this majestic mountain in Shizuoka and Yamanashi prefectures draws global travelers for its breathtaking beauty and recreational allure, from hiking and camping to serene relaxation. ",
                        "For the Japanese, Mt. Fuji is more than a natural wonder. it’s a sacred site and a wellspring of artistic inspiration. ",
                        "During the Edo period (1603-1867), woodblock print artists like ",
                        html.Strong("Katsushika Hokusai"),
                        " and ",
                        html.Strong("Utagawa Hiroshige"),
                        " immortalized the mountain in iconic series, capturing its grandeur from diverse perspectives. ",
                        "Hokusai’s works, in particular, left a lasting impact, even influencing Western artists like ",
                        html.Strong("Vincent van Gogh"),
                        ", making Mt. Fuji a global symbol of Japan’s cultural and natural heritage.",
                    ],
                    className="topdest-intro",
                ),
            ],
            md=7,
        ),
        dbc.Col(
            html.Div(
                html.Img(
                    src="https://images.unsplash.com/photo-1741851373499-e2c10ed2eeb3?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                    alt="Mount Fuji",
                    className="topdest-image img-fluid",
                ),
                className="topdest-imagewrap",
            ),
            md=5,
        ),
    ],
    className="mt-3",
)


fuji_pick_card = dbc.Card(
            className="travel-picks-card mt-4",      
            children=[
                html.Div(
                    className="travel-picks-head",
                    children=[
                        html.Div("88", className="travel-picks-score"),
                        html.Div(
                            children=[
                                html.Div("Mount Fuji", className="travel-picks-title"),
                                html.Div(
                                    className="travel-picks-chips",
                                    children=[
                                        html.Span("👥 Crowd: Moderate", className="travel-picks-chip"),
                                        html.Span("🚇 Access: Excellent", className="travel-picks-chip"),
                                        html.Span("💸 Spend: $400–$700", className="travel-picks-chip"),
                                        html.Span("⏰ Peak: 03:00–05:00", className="travel-picks-chip"),
                                    ],
                                ),
                            ]
                        ),
                    ],
                ),
                dbc.Row(
                    class_name="g-2 mt-2 mb-3",
                    children=[
                        dbc.Col(
                            html.Div(
                                [html.Small("Best months", className="text-muted d-block mb-1"),
                                html.Strong("December - February")],
                                className="search"),
                            md=4,
                        ),
                        dbc.Col(
                            html.Div(
                                [html.Small("Vibe", className="text-muted d-block mb-1"),
                                html.Strong("Nature • Food")],
                                className="search"),
                            md=4,
                        ),
                        dbc.Col(
                            html.Div(
                                [html.Small("Family friendly", className="text-muted d-block mb-1"),
                                html.Strong("Moderate")],
                                className="search"),
                            md=4,
                        ),
                    ],
                ),
                fuji_contain,
                html.Div(
                    className="travel-picks-actions",
                    children=[
                        dbc.Button(
                            "More",
                            id={"type":"open", "index":"fuji"},
                            n_clicks=0,
                            class_name="travel-picks-btn",
                        ),
                        dbc.Button(
                            "View deals",
                            id="pick-shibuya-deals",
                            n_clicks=0,target="_blank", 
                            href="https://www.skyscanner.co.id/",
                            class_name="travel-picks-score border-0 shadow-0",
                        ),
                    ],
                ),
            ],
        )

fuji_offcanvas = dbc.Offcanvas(
    id={"type":"offcanvas", "index":"fuji"},
    title="Interesting Fuji Facts",
    placement="end",  
    is_open=False,
    scrollable=True,
    backdrop=True,
    children=[
        dbc.Container(
            fluid=True,
            children=[
                dbc.Row(
                    class_name="g-3",
                    children=[
                        dbc.Col(
                            fuji_stats_card,
                            width=12
                        ),
                        dbc.Col(
                            fuji_temp_card,
                            width=12
                        )
                    ],
                ),
                html.Div(className="mt-3 d-flex gap-2", children=[
                    dbc.Button("Close", id={"type":"close", "index":"fuji"}, class_name="btn btn-light")
                ])
            ]
        )
    ],
)

top_pick_destination = dbc.Row(
    [
        dbc.Col([
            html.H2("Top Picks Destination"),
            html.P("Every pick includes a score and mini-trend.", className="travel-picks-muted"),
            shibuya_card, 
            fuji_pick_card
    ], width={"size": 10, "offset": 1},)
    ], className="mt-5 mb-5"
)


layout = dbc.Container(
    [
        hero,
        top_destination_section,
        chart_section,
        top_pick_destination,
        shibuya_offcanvas,
        fuji_offcanvas
    ], fluid=False
)


@callback(
    Output({"type":"offcanvas","index":MATCH}, "is_open"),
    [
        Input({"type":"open","index":MATCH}, "n_clicks"),
        Input({"type":"close","index":MATCH}, "n_clicks"),
    ],
    State({"type":"offcanvas","index":MATCH}, "is_open"),
    prevent_initial_call=True,
)
def toggle_tokyo_offcanvas(open_clicks, close_clicks, is_open):
    ctx = dash.callback_context
    if not ctx.triggered:
        return is_open
    return not is_open


if __name__ == "__main__":
    app.run(debug=True)