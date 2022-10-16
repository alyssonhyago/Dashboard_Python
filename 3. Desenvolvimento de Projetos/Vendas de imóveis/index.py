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


# ========================
# Data Insertion
# ========================

df_data = pd.read_csv('dataset/cleaned_data.csv', index_col=0)

app.layout = dbc.Container(
        children=[

        ], fluid=True, )



if __name__ == '__main__':
    app.run_server(debug=True)