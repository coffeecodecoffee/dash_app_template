"""
Dash app instance and stylesheet declaration
https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/explorer/
"""

import dash
from dash import Input, Output, State, dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
from datetime import date

dbc_css = (
   "http://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@v1.0.4/dbc.min.css"
) 

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO, dbc_css])
server = app.server
app.config.suppress_callback_exceptions=()
   
