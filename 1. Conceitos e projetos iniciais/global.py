from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash
import pandas as pd
import numpy as np


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.DataFrame({
    'student_id': range(1,11),
    'score': [1, 5, 2, 5, 2, 3, 1, 5, 1, 5]
})

app.layout = html.Div([
    dcc.Dropdown(list(range(1,6)), 1, id='score'),
    html.Div(id='output')
])

@app.callback(Output('output', 'children'), Input('score','value'))
def update_output(value):
  global df
  filtered_df=df[df['score'] == value]
  return len(filtered_df)

if __name__ == '__main__':
  app.run_server(debug=True)
