from Classes import StatusManager, ApplicationStatusManager
from datetime import datetime
from itertools import groupby
import plotly.offline as py
import plotly.graph_objs as go

class Barchart:

    def group_by_stages(self, applications, status_manager): 
        result = {}
        for item in applications:
            stage_name = status_manager.get_stage_by_status(item)
            if not stage_name in result: 
                result[stage_name] = []

            result[stage_name].append(item)

        return result


    def group_by_colors(self, applications, status_manager):
        result = {}
        for item in applications:
            color_name = status_manager.get_color_by_status(item)
            if not color_name in result:
                result[color_name] = []
            
            result[color_name].append(item)

        return result

    def plot_bars(self):
        # Загружаем справочник статусов, этапов и цветов
        statusManager = StatusManager()
        statusManager.load_statuses()

        all_stages = statusManager.get_all_stages()
        all_colors = statusManager.get_all_colors()

        # Получаем все заявки по заданному интервалу дат. rows - список с заявками
        retriever = ApplicationStatusManager()
        rows = retriever.get_applications_by_dates(datetime(2019, 2, 1), datetime(2019, 2, 28), statusManager.get_valid_statuses())

        # Группируем по цветам новым методом
        color_groups = self.group_by_colors(rows, statusManager)

        bars = []
        # Бежим по цветам, чтобы для каждого цвета создать свой бар
        for color in all_colors:

            # Группируем по этапам в словарь новой функцией
            color_group = color_groups.get(color, [])
            stage_groups = self.group_by_stages(color_group, statusManager)
            
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
