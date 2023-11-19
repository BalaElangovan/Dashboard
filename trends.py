# trends.py
import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

# Load your financial dataset
df = pd.read_csv('sample.csv')

# Register this page
dash.register_page(__name__, path='/trends', name="Spending Trends")

# Prepare data for trend analysis
monthly_trends = df.groupby(['year', 'Month'])['out'].sum().reset_index()

# Page layout
layout = html.Div([
    html.H2("Spending Trends Over Time"),
    html.P("This page analyzes the spending trends and patterns."),
    dcc.Graph(figure=px.line(monthly_trends, x='Month', y='out', color='year', title='Monthly Spending Trends'))
])
