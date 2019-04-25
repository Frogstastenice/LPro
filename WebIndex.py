import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from WebApp import app
import WebBarChart
import WebPieChart


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

index_layout = html.Div([
    dcc.Link('Распределение заявок по отраслям', href='/piechart'),
    html.Br(),
    dcc.Link('Распределение заявок по статусам', href='/barchart'),
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname.lower() == '/barchart':
         return WebBarChart.layout
    elif pathname.lower() == '/piechart':
         return WebPieChart.layout
    elif pathname == '' or pathname == '/':
        return index_layout
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)
