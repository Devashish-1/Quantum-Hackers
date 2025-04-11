from flask import Flask, render_template_string, jsonify
import pandas as pd
import plotly
import plotly.graph_objs as go
import numpy as np
import json
import random
from datetime import datetime, timedelta

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <title>Dynamic Real-time Dashboard</title>
    <script src=\"https://cdn.plot.ly/plotly-latest.min.js\"></script>
    <style>
        body {
            background-color: #18191A;
            color: #E4E6EB;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            overflow: hidden;
        }
        .dashboard-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            padding: 20px;
            box-sizing: border-box;
        }
        #graphDiv {
            width: 100%;
            height: 90vh;
            border-radius: 15px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.6);
            background-color: #242526;
        }
        h1 {
            color: #FFFFFF;
            text-align: center;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px #000000;
        }
    </style>
</head>
<body>
    <div class=\"dashboard-container\">
        <h1>🚀 Real-time Dynamic Dashboard 🚀</h1>
        <div id=\"graphDiv\"></div>
    </div>

    <script>
        async function fetchGraph(){
            const res = await fetch('/graph_data');
            const graph = await res.json();
            Plotly.react('graphDiv', graph.data, graph.layout);
        }

        setInterval(fetchGraph, 2000);
        fetchGraph();
    </script>
</body>
</html>
"""

# Generate random data dynamically
def generate_dynamic_data():
    now = datetime.now()
    timestamps = [(now - timedelta(seconds=5*i)).strftime('%H:%M:%S') for i in reversed(range(30))]

    metrics = ['CPU%', 'Memory%', 'Disk%', 'Network']

    data = []
    for metric in metrics:
        y_data = [random.randint(20, 100) for _ in range(30)]
        trace = go.Scatter(
            x=timestamps,
            y=y_data,
            mode='lines+markers',
            name=metric,
            line=dict(shape='spline'),
            hoverinfo='text',
            hovertext=[f"{metric} at {timestamps[i]}: {y_data[i]}%" for i in range(30)]
        )
        data.append(trace)

    layout = go.Layout(
        xaxis=dict(title='Time', showgrid=True),
        yaxis=dict(title='Usage (%)', range=[0, 120], showgrid=True),
        plot_bgcolor='#242526',
        paper_bgcolor='#242526',
        font=dict(color='#FFFFFF'),
        margin=dict(l=40, r=40, t=40, b=40),
        hovermode='closest',
        transition={'duration': 500, 'easing': 'cubic-in-out'}
    )

    return {'data': data, 'layout': layout}

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/graph_data')
def graph_data():
    graphJSON = json.dumps(generate_dynamic_data(), cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

if __name__ == '__main__':
    app.run(debug=True)
