"""
Starting point for Dash application. 
Run this app with 'python index.py' and
visit http://127.0.0.1:8050/ in your web browser.
"""

import dash
from dash import Input, Output, State, dcc, html, callback_context
import dash_bootstrap_components as dbc
import pandas as pd
from datetime import date
from dash.exceptions import PreventUpdate
from app import app
from dash_components import callbacks


"""
Navigation bar
1. Home Page
2. About Us
"""
nav_bar = dbc.Navbar(
    [
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.NavbarBrand("MI Python", className = "mx-4"),
        dbc.Collapse(
            dbc.Nav([
                dbc.NavItem(dbc.NavLink("Home Page", href="/")),
                dbc.NavItem(dbc.NavLink("About Us", href="/about")),
            ],
            pills=True,
            className="mx-5"
            ),
        id="navbar-collapse1",
        navbar=True,
        ),
    ],
    color="primary",
    dark=True,
    light=False,
)

"""
Error message
"""
jumbotron = html.Div(
    dbc.Container(
        [
            html.H1("404 Page not Found", className="display-3"),
            html.P(
                "The link you are looking for is not found.",
                className="lead",
            ),
            html.Hr(className="my-2"),
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 bg-light rounded-3",
)


"""
Home Page Layout
"""
home_page = [
    dbc.Row(dbc.Col(html.H6("MI Python"))),
    dbc.Row([
        dbc.Col(id="display_tabs", width=8)
    ])
]

"""
About Us Layout
"""
about_us = [
    dbc.Row(dbc.Col(html.H6("Michigan Python User Group"))),
    dbc.Row([
        dbc.Col(id="about_us", width=8)
    ])
]


"""
App Layout
"""
app.layout = html.Div(
    id="parent_div",
    children=[
        dcc.Location(id="url"),
        nav_bar,
        html.Div(
            dbc.Tabs(
                [
                    dbc.Tab(home_page, tab_id="home_page", className="mx-2 p-2", disabled=True),
                    dbc.Tab(about_us, tab_id="about_us", className="mx-2 p-2", disabled=True),
                ],
                active_tab="left_menu",
                id="nav_tabs",
                style={"position":"absolute", "top":"-10rem"},
            ),
            className="mx-auto border-0",
        )
    ],
)

'''
URL call back
'''
@app.callback(
    Output("nav_tabs", "active_tab"),
    Input("url", "pathname"),
)
def render_page_content(pathname):
    if pathname == "/":
        return "home_page"
    elif pathname == "/about":
        return "about_us"
    return jumbotron

'''
Run server
'''
if __name__ == '__main__':
   #Run on a local server -- testing
   app.run_server(debug=True)
   #Run on a hosted server -- production 
   #app.run_server(host='hostname', port='portnumber', debug=True, threaded=True)