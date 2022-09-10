# Run this app with 'python app.py' and 
# visit http://127.0.0.1:8050/ in your web browser

from dash import Dash, html, doc
import pandas as pd

app = Dash(__name__)

app.layout = html.Div(children=[
   html.H1(children='Hello Dash'),
   
   htm.Div(children='''
      Dash: A web application framework for your data.
   '''),
   ])

#Call Back Example
@app.callback(
   Output("name_out", "name_out1"), 
   Input("name_in", "name_in1"),
)
def some_function(name_in1):
   return value

if __name__ == '__main__':
   app.run_server(debug=True)
   #app.run_server(host='hostname', port='portnumber', debug=True, threaded=True)
   
