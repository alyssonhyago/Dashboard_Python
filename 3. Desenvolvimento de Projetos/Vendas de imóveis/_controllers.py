from dash import dcc, html
import dash_bootstrap_components as dbc
from app import app

list_of_locations = {
    'All': 0,
    'Manhattan': 1,
    'Bronx': 2,
    'Brooklyn': 3,
    'Queens': 4,
    'Staten Island': 5,
}

slider_size = [100, 500, 1000, 10000, 10000000]

controlers = dbc.Row([
    html.Img(id='logo', src=app.get_asset_url('logo1.png'), style={'width': '50%' ''}),
    html.H3('Vendas de imóveis - NYC', style={'margin-top': '30px'}),
    html.P('Utilize este Dashboard ára analisar vendas ocorridas na cidade de New York no periodo de 1 ano'),
    html.H4('Distrito', style={'margin-top':'50px', 'margin-bottom':'25px'}),
    dcc.Dropdown(
        id='location-dropdown',
        options=[{'label': i, 'value': j } for i, j in list_of_locations.items()],
        value=0,
        placeholder='Selecione um distrito'
    ),
    html.H4('Metragem (m²)',style={'margin-top':'50px', 'margin-bottom':'25px'}),

    dcc.Slider(min=0,max=4,id='slider-square-size',
               marks={i:str(j) for i, j in enumerate(slider_size)}
               ),
    html.H4('variavel de control', style={'margin-bottom':'20px','margin-top':'20px'}),
    dcc.Dropdown(
        options=[
            {'label': 'YEAR BUILT','value':'YEAR BUILT'},
            {'label': 'TOTAL UNITS','value':'TOTAL UNITS'},
            {'label': 'SALE PRICE','value':'SALE PRINCE'},
        ],
        value='SALE PRICE',
        id='dropdown-color', style={'margin-bottom':'20px'}
    )
])