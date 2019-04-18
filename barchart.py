from Classes import StatusManager, ApplicationStatusManager
from datetime import datetime
from itertools import groupby
import plotly.offline as py
import plotly.graph_objs as go

py.init_notebook_mode()

def group_by_stages(tuples): # В tuples у нас кортеж (row, этап, цвет)
    result = {}
    for item in tuples:
        if not item[1] in result: # В item[1] - этап
            result[item[1]] = []

        result[item[1]].append(item)

    return result

def group_by_colors(tuples):
    result = {}
    for item in tuples:
        if not item[2] in result:
            result[item[2]] = []
        
        result[item[2]].append(item)

    return result

def plot_bars():
    # Загружаем справочник статусов, этапов и цветов
    statusManager = StatusManager()
    statusManager.load_statuses()

    all_stages = statusManager.get_all_stages()
    all_colors = statusManager.get_all_colors()

    # Получаем все заявки по заданному интервалу дат. rows - список с заявками
    retriever = ApplicationStatusManager()
    rows = retriever.get_applications_by_dates(datetime(2019, 2, 1), datetime(2019, 2, 28))

    # Создаем кортежи вида (заявка, этап, цвет)
    tuples = []
    for row in rows:
        if (statusManager.is_status_valid(row)):
            tuples.append((row, statusManager.get_stage_by_status(row), statusManager.get_color_by_status(row)))

    # Группируем по цветам новым методом
    color_groups = group_by_colors(tuples)

    bars = []
    # Бежим по цветам, чтобы для каждого цвета создать свой бар
    for color in all_colors:

        # Группируем по этапам в словарь новой функцией
        color_group = color_groups.get(color, [])
        stage_groups = group_by_stages(color_group)
        
        x = []
        for stage in all_stages:
            if stage in stage_groups:
                x.append(len(stage_groups[stage]))
            else:
                x.append(0)

        bar = go.Bar(y=all_stages, x=x, name=color, orientation='h')
        
        bars.append(bar)

    layout = go.Layout(barmode='stack')
    figure = go.Figure(data=bars, layout=layout)
    py.iplot(figure)

#plot_bars()
