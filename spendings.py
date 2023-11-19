# spendings.py
import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

# Load your financial dataset
df = pd.read_csv('sample.csv')

# Register this page
dash.register_page(__name__, path='/spendings', name="Spendings Analysis")

# Summarize data
monthly_spendings = df.groupby('Month')['out'].sum().reset_index()
yearly_spendings = df.groupby('year')['out'].sum().reset_index()

# Page layout
layout = html.Div([
    html.H2("Spendings Analysis"),
    html.P("This page shows the total spendings per month and per year."),
    
    html.H3("Monthly Spendings"),
    dcc.Graph(figure=px.bar(monthly_spendings, x='Month', y='out', title='Monthly Spendings')),

    html.H3("Yearly Spendings"),
    dcc.Graph(figure=px.bar(yearly_spendings, x='year', y='out', title='Yearly Spendings'))
])
