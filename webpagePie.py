import dash
import dash_core_components as dcc
import dash_html_components as html

from Piechart import Piechart

piefigure = Piechart()
piegraph = piefigure.make_ugly_pies()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H6(children='Еженедельный отчет'),

    #html.Div(children='''
     #   Распределение проектов по отраслям
    #'''),

    dcc.Graph(
        id='piechart',
        figure=piegraph
        )
])

if __name__ == '__main__':
    app.run_server(debug=True)
