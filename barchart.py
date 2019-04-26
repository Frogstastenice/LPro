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

    def group_by_passed_stages(self, applications, status_manager):
        result = {}
        for item in applications:
            passed_stages = status_manager.get_passed_stages_by_status(item)
            for stage in passed_stages:
                if not stage in result:
                    result[stage] = []

                result[stage].append(item)

        return result


    def group_by_colors(self, applications, status_manager):
        result = {}
        for item in applications:
            color_name = status_manager.get_color_by_status(item)
            if not color_name in result:
                result[color_name] = []
            
            result[color_name].append(item)

        return result

    def get_bars(self, start_date, end_date):
        # Загружаем справочник статусов, этапов и цветов
        status_manager = StatusManager()
        status_manager.load_statuses()

        all_stages = status_manager.get_all_stages()
        all_colors = status_manager.get_all_colors()

        # Получаем все заявки по заданному интервалу дат. rows - список с заявками
        retriever = ApplicationStatusManager()
        rows = retriever.get_applications_by_dates(
            start_date, 
            end_date, 
            status_manager.get_valid_statuses(),
        )

        # Группируем по цветам новым методом
        color_groups = self.group_by_colors(rows, status_manager)

        color_bars = []
        # Бежим по цветам, чтобы для каждого цвета создать свой бар
        for color in all_colors:

            # Группируем по этапам в словарь новой функцией
            color_group = color_groups.get(color, [])
            stage_groups = self.group_by_stages(color_group, status_manager)
            
            x = []
            for stage in all_stages:
                if stage in stage_groups:
                    x.append(len(stage_groups[stage]))
                else:
                    x.append(0)

            bar = go.Bar(y=all_stages, x=x, name=color, orientation='h')
            
            color_bars.append(bar)
        
        passed_stages_groups = self.group_by_passed_stages(rows, status_manager)

        x = []
        for stage in all_stages:
            if stage in passed_stages_groups:
                x.append(len(passed_stages_groups[stage]))
            else:
                x.append(0)
        
        bar = go.Bar(y=all_stages, x=x, name='Этап пройден', orientation='h')

        color_bars.append(bar)

        layout = go.Layout(barmode='stack')
        figure = go.Figure(data=color_bars, layout=layout)
        figure['layout'].update(autosize=False, width=900, height=600, margin=dict(l=180))
        #py.iplot(figure)
        return figure

#plot_bars()
