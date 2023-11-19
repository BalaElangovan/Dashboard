# category.py
import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

# Load your financial dataset
df = pd.read_csv('sample.csv')

# Register this page
dash.register_page(__name__, path='/category', name="Category Analysis")

# Summarize data by category
category_spendings = df.groupby('category')['out'].sum().reset_index()

# Page layout
layout = html.Div([
    html.H2("Spendings by Category"),
    html.P("This page shows the distribution of spendings across different categories."),
    dcc.Graph(figure=px.pie(category_spendings, names='category', values='out', title='Spendings by Category'))
])
