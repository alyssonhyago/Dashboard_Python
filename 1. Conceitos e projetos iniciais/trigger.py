from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash
import pandas as pd
import numpy as np


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
  html.Button('Button 1', id='bnt-1-ctx-example'),
  html.Button('Button 2', id='bnt-2-ctx-example'),
  html.Button('Button 3', id='bnt-3-ctx-example'),
  html.Div(id='container-ctx-example')
])

@app.callback(Output('container-ctx-example','children'),
              Input('btn-1-ctx-example','n_clicks'),
              Input('btn-2-ctx-example','n_clicks'),
              Input('btn-3-ctx-example','n_clicks')
)
def display(btn1,btn2,btn3):
  id_triggered = callback_context.triggered[0]['prop_id'].split('.')[0]

  return id_triggered
 
if __name__ == '__main__':
  app.run_server(debug=True)
