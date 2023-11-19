# dataset.py
import dash
from dash import html, dash_table
import pandas as pd

# Load your financial dataset
df = pd.read_csv('sample.csv')

# Register this page
dash.register_page(__name__, path='/dataset', name="Dataset Preview")

# Page layout
layout = html.Div([
    html.H2("Financial Dataset Overview"),
    html.P("This page provides a preview of the financial dataset."),
    dash_table.DataTable(
        df.head().to_dict('records'),
        [{"name": i, "id": i} for i in df.columns],
        style_table={'overflowX': 'auto'},
    )
])
