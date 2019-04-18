from Classes import ApplicationManager, IndustryManager
import numpy as np
import plotly.offline as py
import plotly.graph_objs as go

class Piechart:

    def group_applications_by_industry(self, applications, industry_manager):
        result = {}
        for row in applications:
            industry_name = industry_manager.get_report_industry_name(row.IdIndustry) # для конретной заявки получаем имя большой индустрии по id маленькой
            if not industry_name in result: # вот теперь мы проверяем, есть ли такая индустрия в словаре
                result[industry_name] = [] # Если нет, то добавляем со значением - пустым списком
            
            result[industry_name].append(row) # в этом месте гарантированно есть ключ со списком. Получаем список по ключу и вызываем append

        return result #Забыли вернуть :))


    def make_ugly_pies(self):
        industry_manager = IndustryManager()
        application_manager = ApplicationManager()

        industry_manager.load_industries()

        applications = application_manager.get_applications_by_status({3126345, 7552031, 7552032, 20761})
        
        applications_by_industry = self.group_applications_by_industry(applications, industry_manager)
        #print(applications_by_industry)

        labels = list(applications_by_industry.keys())
        values_count_loans = []
        values_count_projects = []
        loans_sum = 0
        projects_sum = 0

        for report_industry in labels:
            loan_sum_by_industry = 0
            row = applications_by_industry.get(report_industry)
            values_count_projects.append(len(row))
            
            for item in row:
                loan_sum_by_industry += item.LoanAmount
            values_count_loans.append(loan_sum_by_industry / 1000000)
            
        loans_sum = sum(values_count_loans)    
        projects_sum = sum(values_count_projects)

        value_text = [] #чтобы подписи чисел на графике были красивы
        for num in values_count_loans:
            val_text = '{:.2f}'.format(num)
            value_text.append(val_text)

        fig2 = {
            'data': [
                {
                    'labels': labels,
                    'values': values_count_loans,
                    'text': value_text,
                    'type': 'pie',
                    'hole': 0.6,
                    'title': {
                        'text': '{:.2f} млн'.format(loans_sum),
                        'font': {
                            'size': 30
                        }
                    },
                    'textinfo': 'text',
                    'textfont': {
                        'size': 14
                    },
                    "domain": {"column": 0},
                },
                {
                    'labels': labels,
                    'values': values_count_projects,
                    'text': values_count_projects,
                    'type': 'pie',
                    'hole': 0.6,
                    'title': {
                        'text': '{} проект'.format(projects_sum),
                        'font': {
                            'size': 30
                        }
                    },
                    'textinfo': 'text',
                    'textfont': {
                        'size': 14
                    },
                    "domain": {"column": 1},
                }
            ],
            'layout': {
                "grid": {"rows": 1, "columns": 2},
                'title': {
                    'text': 'Инвестиции по отраслям',
                    'font': {
                        'size': 44
                    }
                }
            }
        }


        py.iplot(fig2)





