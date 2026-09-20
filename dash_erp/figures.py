import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd

BRAND = {
    "text": "#0b1220",
    "muted": "#5a6a85",
    "grid": "#e9eef6",
    "brand1": "#1463ff",
    "brand2": "#36a2eb",
    "accent1": "#ff6a00",
    "accent2": "#ff9a3d",
}

season_data = [
    ("Jan", 2.69), ("Feb", 2.79), ("Mar", 3.08), ("Apr", 3.04), ("May", 3.04), ("Jun", 3.14),
    ("Jul", 3.29), ("Aug", 2.93), ("Sep", 2.87), ("Oct", 3.31), ("Nov", 3.19), ("Dec", 3.49),
]
df_bar = pd.DataFrame(season_data, columns=["Month", "Visitors_M"])
month_order = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
df_bar["Month"] = pd.Categorical(df_bar["Month"], categories=month_order, ordered=True)
df_bar = df_bar.sort_values("Month")

fig_bar = px.bar(df_bar, x="Month", y="Visitors_M", title=None,)
fig_bar.update_traces(
    marker=dict(color="#9ad0f5", line=dict(color="#36a2eb", width=0)),
    hovertemplate="%{x}: %{y}<extra></extra>",
)
fig_bar.update_layout(
    hovermode="x unified",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis_title=None,
    yaxis_title=None,
    font=dict(color="#6B7280"),
    hoverlabel=dict(bgcolor="#0b1220", font_color="#ffffff"),
)


df_line = pd.DataFrame([
    {"Year": 2014, "TotalTravelers": 13.41},
    {"Year": 2015, "TotalTravelers": 19.74},
    {"Year": 2016, "TotalTravelers": 24.04},
    {"Year": 2017, "TotalTravelers": 28.69},
    {"Year": 2018, "TotalTravelers": 31.19},
    {"Year": 2019, "TotalTravelers": 31.88},
    {"Year": 2020, "TotalTravelers": 4.12},
    {"Year": 2021, "TotalTravelers": 0.25},
    {"Year": 2022, "TotalTravelers": 3.83},
    {"Year": 2023, "TotalTravelers": 25.07},
    {"Year": 2024, "TotalTravelers": 36.87},
])

fig_line = px.line(df_line, x="Year", y="TotalTravelers", markers=True, title=None,)
fig_line.update_traces(
    line=dict(shape="spline", color=BRAND["brand2"], width=3),
    marker=dict(size=7, color=BRAND["brand2"], line=dict(color="#ffffff", width=1.5)),
    hovertemplate="%{x}: %{y}<extra></extra>",
)
fig_line.update_layout(
    hovermode="x unified",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis_title=None,
    yaxis_title=None,
    font=dict(color="#6B7280"),
    xaxis=dict(gridcolor=BRAND["grid"], zeroline=False, showline=False, ticks="", title=None),
    yaxis=dict(gridcolor=BRAND["grid"], zeroline=False, showline=False, ticks="", title=None),
    hoverlabel=dict(bgcolor="#0b1220", font_color="#ffffff"),
)

destinations = [
    ("Shibuya Crossing", 35.6595, 139.7005, "Nightlife", 95),
    ("Senso-ji (Asakusa)", 35.7148, 139.7967, "Culture", 88),
    ("Tokyo Skytree", 35.7100, 139.8107, "View", 90),
    ("Tsukiji Outer Market", 35.6655, 139.7708, "Food", 84),
    ("Akihabara", 35.6984, 139.7730, "Shopping", 86),
    ("Meiji Shrine", 35.6764, 139.6993, "Culture", 82),
    ("Shinjuku Gyoen", 35.6852, 139.7101, "Nature", 80),
    ("Ginza", 35.6717, 139.7650, "Shopping", 83),
    ("Harajuku (Takeshita St)", 35.6716, 139.7036, "Shopping", 81),
    ("Odaiba Seaside Park", 35.6298, 139.7745, "View", 78),
]
df_tokyo = pd.DataFrame(destinations, columns=["name", "lat", "lon", "category", "score"])

# fig_map = px.scatter_mapbox(
#     df_tokyo,
#     lat="lat",
#     lon="lon",
#     hover_name="name",
#     hover_data={"category": True, "score": True, "lat": False, "lon": False},
#     color="category",
#     size="score",
#     size_max=22,
#     zoom=10,
#     center={"lat": 35.68, "lon": 139.76},

# )
# fig_map.update_layout(
#     mapbox_style="open-street-map", 
#     margin=dict(t=10, r=20, b=80, l=30),
#     paper_bgcolor="rgba(0,0,0,0)",
#     plot_bgcolor="rgba(0,0,0,0)",

#     )


df_vibe = pd.DataFrame({
    "Facet": ["nightlife", "culture", "shopping", "food", "nature", "work"],
    "Score": [90, 80, 96, 60, 60, 40],
})
fig_vibe = px.line_polar(df_vibe, r="Score", theta="Facet", line_close=True, )
fig_vibe.update_traces(
    fill="toself",
    line=dict(color=BRAND["brand2"], width=2.5),
    marker=dict(size=6, color=BRAND["brand2"], line=dict(color="#ffffff", width=1)),
    hovertemplate="%{theta}: %{r}<extra></extra>",
)
fig_vibe.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100],
            tickvals=[0, 20, 40, 60, 80, 100],
            ticktext=["0", "20", "40", "60", "80", " "],
            angle=90,
            tickangle=90,
            gridcolor=BRAND["grid"], showline=False,
        ),
        angularaxis=dict(rotation=90,  showline=False,gridcolor=BRAND["grid"],),
        gridshape="linear",
        bgcolor="#ffffff",
    ),
    showlegend=False,
    font=dict(color="#6B7280"),
)


startup_data = [
    ("Shibuya City", 1651), ("Minato City", 1586), ("Chiyoda City", 1106), ("Chuo City", 758),
    ("Shinjuku City", 662), ("Shinagawa City", 406), ("Meguro City", 221), ("Bunkyo City", 207),
    ("Toshima City", 167), ("Setagaya City", 166), ("Other 13 Wards", 620),
]
df_startups = pd.DataFrame(startup_data, columns=["Ward", "Startups"])
df_startups["Color"] = ["#A855F7" if w == "Shibuya City" else "#BDBDBD" for w in df_startups["Ward"]]
fig_startups = px.bar(
    df_startups, x="Ward", y="Startups", color="Color",
    color_discrete_map={c: c for c in df_startups["Color"].unique()},
)
fig_startups.update_layout(
    showlegend=False,
    xaxis_title=None,
    yaxis_title=None,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    margin=dict(t=10, r=20, b=80, l=20),
    yaxis=dict(range=[0, 2000], gridcolor="rgba(0,0,0,0.06)"),
    xaxis=dict(tickangle=-25),
)

hours = [
    "13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00",
    "23:00","0:00","1:00","2:00","3:00","4:00","5:00","6:00","7:00","8:00","9:00","10:00","11:00"
]
people = [
    12000,12500,13000,14000,16000,19000,24000,33000,39000,41000,
    36000,25000,20000,18000,16000,14000,12000,6000,5000,6000,7000,9000,11000
]
df_wave = pd.DataFrame({"Hour": hours, "People": people})
df_wave["Hour"] = df_wave["Hour"].astype(str).str.replace("\uFF1A", ":", regex=False).str.strip()
df_wave["Hour"] = pd.Categorical(df_wave["Hour"], categories=hours, ordered=True)
df_wave = df_wave.sort_values("Hour")
base = "#A855F7"
light = "rgba(168,85,247,0.35)"
peak_idx = df_wave["People"].idxmax()
df_wave["Color"] = [base if i == peak_idx else light for i in range(len(df_wave))]

fig_wave = px.bar(
    df_wave, x="Hour", y="People", color="Color",
    color_discrete_map={c: c for c in df_wave["Color"].unique()},
)
fig_wave.update_xaxes(type="category", categoryorder="array", categoryarray=hours)
fig_wave.update_layout(
    showlegend=False,
    xaxis_title=None,
    yaxis_title=None,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    margin=dict(t=10, r=20, b=80, l=30),
    yaxis=dict(range=[0, 50000], tickformat=","),
    xaxis=dict(tickangle=-30),
)

fuji_data = [
    (2011, 61), (2012, 76), (2013, 121), (2014, 80), (2015, 75),
    (2016, 111), (2017, 83), (2018, 95), (2019, 67), (2020, 5),
]
df_fuji = pd.DataFrame(fuji_data, columns=["Year", "Victims"])
fig_fuji = px.bar(df_fuji, x="Year", y="Victims", color_discrete_sequence=["#A855F7"])
fig_fuji.update_layout(
    xaxis_title=None,
    yaxis_title=None,
    showlegend=False,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    margin=dict(t=10, r=20, b=40, l=20),
)

fig_fuji.update_xaxes(
    dtick=1,                           
    tick0=int(df_fuji["Year"].min()),  
    tickangle=0,
)