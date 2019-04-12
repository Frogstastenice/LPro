from Classes import StatusManager, ApplicationDataRetriever
from datetime import datetime
from itertools import groupby
import plotly.offline as py
import plotly.graph_objs as go

py.init_notebook_mode()

def plot_bars():
    # Загружаем справочник статусов, этапов и цветов
    statusManager = StatusManager()
    statusManager.load_statuses()

    all_stages = statusManager.get_all_stages()

    # Получаем все заявки по заданному интервалу дат. rows - список с заявками
    retriever = ApplicationDataRetriever()
    rows = retriever.get_applications_by_dates(datetime(2015, 2, 1), datetime(2015, 5, 1))

    # Создаем кортежи вида (заявка, этап, цвет)
    tuples = []
    for row in rows:
        tuples.append((row, statusManager.get_stage_by_status(row), statusManager.get_color_by_status(row)))

    # Сортируем кортежи по цвету, получаем список тех же кортежей, но в другом порядке
    sorted_by_color = list(sorted(tuples, key=lambda item: item[2]))

    # Группируем кортежи по цвету, в color_groups получаем новые кортежи вида (цвет, список кортежей tuples этого цвета)
    color_groups = groupby(sorted_by_color, lambda item: item[2])

    bars = []
    # Бежим по цветам, чтобы для каждого цвета создать свой бар
    for color_group in color_groups:

        # Список кортежей tuples каждого цвета сортируем по этапу
        sorted_by_stages = list(sorted(color_group[1], key=lambda item: item[1]))

        # Отсортированный список кортежей группируем по этапу в словарь
        stage_groups = {}
        for stage, stage_tuples in groupby(sorted_by_stages, lambda item: item[1]):
            stage_groups[stage] = list(stage_tuples)

        x = []
        for stage in all_stages:
            if stage in stage_groups:
                x.append(len(stage_groups[stage]))
            else:
                x.append(0)

        bar = go.Bar(y=all_stages, x=x, name=color_group[0], orientation='h')
        
        bars.append(bar)

    layout = go.Layout(barmode='stack')
    figure = go.Figure(data=bars, layout=layout)
    py.iplot(figure)

#plot_bars()