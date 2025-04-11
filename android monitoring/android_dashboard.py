import pandas as pd
from dash import Dash, dcc, html, Input, Output, State
import plotly.express as px
import datetime

LOG_FILE = "device_monitor_log.csv"
app = Dash(__name__)
app.title = "📱 Android Device Dashboard"

# Layout
app.layout = html.Div([
    html.H1("📱 Android Monitoring Dashboard", style={'textAlign': 'center'}),
    dcc.Interval(id="interval", interval=5000, n_intervals=0),

    html.Div([
        html.Button("⟳ Refresh", id="refresh-btn", n_clicks=0),
        html.Button("📤 Export Logs", id="export-btn", n_clicks=0),
        html.Button("🗑 Clear Alerts", id="clear-btn", n_clicks=0)
    ], style={'textAlign': 'center', 'marginBottom': '10px'}),

    dcc.Dropdown(id='app-filter', multi=True, placeholder="🔎 Filter by App"),

    dcc.Tabs([
        dcc.Tab(label="📊 Usage Graphs", children=[
            dcc.Graph(id="ram-graph"),
            dcc.Graph(id="cpu-graph")
        ]),
        dcc.Tab(label="🔋 Battery & Alerts", children=[
            dcc.Graph(id="battery-alerts"),
            html.Div(id="alert-messages")
        ]),
        dcc.Tab(label="📈 Summary Reports", children=[
            html.H4("Top 5 RAM Consumers"),
            html.Div(id="top5-output"),
            html.Hr(),
            html.H4("📅 Summary"),
            html.Div(id="weekly-summary")
        ])
    ])
])

# Update app list in dropdown
@app.callback(
    Output("app-filter", "options"),
    Input("interval", "n_intervals")
)
def update_filter(n):
    try:
        df = pd.read_csv(LOG_FILE)
        apps = sorted(df['App'].unique())
        return [{"label": app, "value": app} for app in apps]
    except:
        return []

# Update all graphs and data
@app.callback(
    Output("ram-graph", "figure"),
    Output("cpu-graph", "figure"),
    Output("battery-alerts", "figure"),
    Output("alert-messages", "children"),
    Output("top5-output", "children"),
    Output("weekly-summary", "children"),
    Input("interval", "n_intervals"),
    Input("refresh-btn", "n_clicks"),
    Input("clear-btn", "n_clicks"),
    Input("app-filter", "value")
)
def update_graphs(n, refresh, clear, selected_apps):
    try:
        df = pd.read_csv(LOG_FILE)
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])

        if clear > 0:
            df['Alert'] = ""
            df.to_csv(LOG_FILE, index=False)

        if selected_apps:
            df = df[df['App'].isin(selected_apps)]

        fig_ram = px.line(df, x="Timestamp", y="RAM_MB", color="App", title="Live RAM Usage")
        fig_cpu = px.line(df, x="Timestamp", y="CPU%", color="App", title="Live CPU Usage")
        fig_ram.update_layout(template="plotly_dark")
        fig_cpu.update_layout(template="plotly_dark")

        alert_df = df[df["Battery%"] < 15]
        fig_battery = px.scatter(alert_df, x="Timestamp", y="Battery%", color="App", title="Battery Alerts (<15%)")
        fig_battery.update_layout(template="plotly_dark")

        alerts = df[df["Alert"] != ""].tail(5)
        alert_msgs = [f"{row['Timestamp']} | {row['App']} → {row['Alert']}" for _, row in alerts.iterrows()]
        alert_box = html.Ul([html.Li(msg) for msg in alert_msgs]) if alert_msgs else "✅ No current alerts"

        latest = df.sort_values("Timestamp").groupby("App").tail(1)
        top5 = latest.sort_values("RAM_MB", ascending=False).head(5)
        top5_ui = html.Ul([html.Li(f"{row['App']} → {row['RAM_MB']} MB") for _, row in top5.iterrows()])

        summary = html.Ul([
            html.Li(f"Total logs: {len(df)}"),
            html.Li(f"Apps monitored: {df['App'].nunique()}"),
            html.Li(f"Low battery events: {len(df[df['Battery%'] < 15])}"),
            html.Li(f"High RAM events: {len(df[df['RAM_MB'] > 500])}"),
            html.Li(f"High CPU events: {len(df[df['CPU%'] > 70])}")
        ])

        return fig_ram, fig_cpu, fig_battery, alert_box, top5_ui, summary

    except Exception as e:
        return {}, {}, {}, f"Error loading data: {e}", "", ""

# Export CSV manually
@app.callback(
    Output("export-btn", "n_clicks"),
    Input("export-btn", "n_clicks"),
    prevent_initial_call=True
)
def export_logs(n_clicks):
    if n_clicks > 0:
        df = pd.read_csv(LOG_FILE)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        df.to_csv(f"export_android_logs_{timestamp}.csv", index=False)
    return 0

if __name__ == "__main__":
    app.run(debug=False)
