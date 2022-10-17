'''

Projeto com Dash - Vendas de imóveis

Autor: Eng Oliveira, Alysson

Data: 16/10/2022
'''


# Importando as bibliotecas
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd

# Importando o app.py
from app import app
from _map import *
from _histogram import *
from _controllers import *

# ========================
# Data Insertion
# ========================

#Vendas de imóveis/
df_data = pd.read_csv('dataset/cleaned_data.csv', index_col=0)

df_data['size_m2'] = df_data['GROSS SQUARE FEET'] / 10.764
df_data = df_data[df_data['YEAR BUILT'] > 0]
df_data["SALE DATE"] = pd.to_datetime(df_data['SALE DATE'])

df_data.loc[df_data['size_m2']> 1000, 'size_m2'] = 10000
df_data.loc[df_data['SALE PRICE'] > 50000000, 'SALE PRINE'] = 50000000
df_data.loc[df_data['SALE PRICE'] < 10000, 'SALE PRINE'] = 10000

# ========================
# Layout
# ========================

app.layout = dbc.Container(
        children=[
            dbc.Row([

                dbc.Col([controlers], md=3),
                dbc.Col([hist, map], md=9),
            ])

        ], fluid=True, )



if __name__ == '__main__':
    app.run_server(debug=True)
    #app.run_server(host='', port='')