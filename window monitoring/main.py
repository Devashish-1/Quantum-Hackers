import psutil
import pandas as pd
import time
import threading
from datetime import datetime
from dash import Dash, dcc, html, Output, Input, State
import plotly.graph_objs as go
import plotly.io as pio
import dash

CSV_FILE = "task_data.csv"
REFRESH_RATE = 2
MAX_HISTORY = None

def init_csv():
    df = pd.DataFrame(columns=["Timestamp", "Process", "CPU%", "RAM_MB", "PID", "Status"])
    df.to_csv(CSV_FILE, index=False)

#CSV logging 
def logger():
    print("📊 Logger started...")
    while True:
        data = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info', 'status']):
            try:
                name = proc.info['name']
                pid = proc.info['pid']
                cpu = proc.cpu_percent(interval=0.1)  # wait a bit to get real CPU usage
                ram = proc.info['memory_info'].rss / (1024 * 1024)
                status = proc.info['status']
                timestamp = datetime.now().strftime("%H:%M:%S")
                data.append([timestamp, name, cpu, ram, pid, status])
            except:
                continue
        df = pd.DataFrame(data, columns=["Timestamp", "Process", "CPU%", "RAM_MB", "PID", "Status"])
        df.to_csv(CSV_FILE, mode='a', header=False, index=False)
        time.sleep(REFRESH_RATE)

app = Dash(__name__)
app.title = "Live Task Monitor"

app.layout = html.Div([
    html.H1("🖥️ Live Windows Task Monitor", style={'textAlign': 'center'}),
    html.Div([
        html.Label("Metric:"),
        dcc.RadioItems(
            id='metric-toggle',
            options=[
                {'label': 'RAM (MB)', 'value': 'RAM_MB'},
                {'label': 'CPU (%)', 'value': 'CPU%'}
            ],
            value='RAM_MB',
            labelStyle={'display': 'inline-block', 'marginRight': '20px'}
        )
    ], style={'textAlign': 'center', 'padding': '10px'}),
    html.Div([
        html.Label("Filter by Process:"),
        dcc.Dropdown(
            id='process-filter',
            options=[],
            multi=True,
            placeholder="Select process(es)..."
        )
    ], style={'width': '60%', 'margin': 'auto'}),
    dcc.Graph(id='live-graph'),
    html.Div([
        html.Button("⬇️ Download as PNG", id='download-png', n_clicks=0),
        html.Button("⬇️ Download as PDF", id='download-pdf', n_clicks=0)
    ], style={'textAlign': 'center', 'marginTop': 10}),
    dcc.Interval(id='interval-component', interval=REFRESH_RATE * 1000, n_intervals=0)
])

@app.callback(
    Output('process-filter', 'options'),
    Input('interval-component', 'n_intervals')
)
def update_dropdown(n):
    try:
        df = pd.read_csv(CSV_FILE)
        return [{'label': p, 'value': p} for p in sorted(df['Process'].unique())]
    except:
        return []

@app.callback(
    Output('live-graph', 'figure'),
    Input('interval-component', 'n_intervals'),
    Input('metric-toggle', 'value'),
    Input('process-filter', 'value')
)
def update_graph(n, metric, selected_procs):
    try:
        df = pd.read_csv(CSV_FILE)
        if MAX_HISTORY:
            df = df.tail(MAX_HISTORY)

        fig = go.Figure()
        procs = selected_procs if selected_procs else df["Process"].unique()
        colors = ['cyan', 'yellow', 'lime', 'orange', 'purple', 'red', 'blue']

        for i, proc in enumerate(procs):
            proc_data = df[df["Process"] == proc]
            avg = proc_data[metric].mean()
            color = colors[i % len(colors)]

            fig.add_trace(go.Scatter(
                x=proc_data["Timestamp"],
                y=proc_data[metric],
                mode='lines+markers',
                name=proc,
                line=dict(color=color, width=2, shape='spline'),
                marker=dict(color=['red' if val > avg else color for val in proc_data[metric]]),
                hovertemplate=f"App: {proc}<br>Time: %{{x}}<br>{metric}: %{{y}}"
            ))

            if len(proc_data) > 1:
                fig.add_trace(go.Scatter(
                    x=proc_data["Timestamp"],
                    y=[avg] * len(proc_data),
                    name=f"{proc} AVG",
                    line=dict(dash='dash', color=color),
                    mode='lines',
                    showlegend=False
                ))

        fig.update_layout(
            height=600,
            template='plotly_dark',
            title=f"Live {metric} Usage (Updated Every {REFRESH_RATE}s)",
            xaxis_title="Timestamp",
            yaxis_title=metric,
            legend_title="Processes"
        )
        return fig
    except Exception as e:
        print(f"Graph error: {e}")
        return go.Figure()

@app.callback(
    Output('download-png', 'n_clicks'),
    Output('download-pdf', 'n_clicks'),
    Input('download-png', 'n_clicks'),
    Input('download-pdf', 'n_clicks'),
    State('live-graph', 'figure'),
    prevent_initial_call=True
)
def export_graph(png_clicks, pdf_clicks, fig_data):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise dash.exceptions.PreventUpdate

    fig = go.Figure(fig_data)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    try:
        if ctx.triggered[0]["prop_id"].startswith("download-png"):
            pio.write_image(fig, f"graph_export_{timestamp}.png")
        elif ctx.triggered[0]["prop_id"].startswith("download-pdf"):
            pio.write_image(fig, f"graph_export_{timestamp}.pdf")
    except Exception as e:
        print(f"Export error: {e}")

    return 0, 0

if __name__ == '__main__':
    init_csv()
    threading.Thread(target=logger, daemon=True).start()
    app.run(debug=False)
