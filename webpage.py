import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


from barchart import Barchart
from dateutil.relativedelta import relativedelta, TH, WE
from datetime import datetime

delta = relativedelta(days=1,weekday=TH)
button_list = []

current_date = datetime(2019,1,1)
max_date = datetime.today()

while True:
    current_date = current_date+delta
    if current_date > max_date:
        break
    button_list.append(current_date)

barfigure = Barchart()
#bargraph = barfigure.get_bars()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H4(children='Еженедельный отчет'),

    html.Div(children='''
        Распределение заявок по статусам
    '''),

    dcc.Graph(
        id='barchart',
        #figure= bargraph
    ),

    dcc.RadioItems(
        id='week_selector',
        options=[{'label': date.strftime(
            '%d-%b'), 'value': date.strftime('%Y-%m-%d')} for date in button_list],
        value=button_list[-1].strftime('%Y-%m-%d'),
        labelStyle={'display': 'inline-block'}
    )
])


@app.callback(
    Output('barchart', 'figure'),
    [Input('week_selector', 'value')]
)
def update_plot(input_data):
    start_date = datetime.strptime(input_data, '%Y-%m-%d')
    end_date = start_date + relativedelta(weekday=WE)
    return barfigure.get_bars(start_date, end_date)


if __name__ == '__main__':
    app.run_server(debug=True)
