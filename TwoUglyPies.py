
#%%
import csv
import numpy as np
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go

#%%

def sum_and_divide(series):
    return np.sum(series) / 1000000

data = pd.read_csv('Tabgraph1.csv')
loan_industries = data[['LoanAmount', 'ReportIndName']]
#loan_industries.head()

group = loan_industries.groupby('ReportIndName')
loan_sums = group.aggregate(sum_and_divide)
#loan_sums

value_text = []
for num in loan_sums['LoanAmount']:
    val_text = '{:.2f}'.format(num)
    value_text.append(val_text)

total_loan = '{:.2f} млн'.format(np.sum(loan_sums['LoanAmount']))

    
#%%

count_prj_dict = {}

with open('Tabgraph1.csv', 'r', encoding='utf-8') as new_file:
    reader = csv.DictReader( new_file, fieldnames=['IdProject', 'LoanAmount',
    'IdIndustry', 'IdReportIndustry', 'ReportIndName'],
    delimiter=',')
    next(reader)
    for row in reader:
        industry_id = row['ReportIndName']
        if not industry_id in count_prj_dict:
            count_prj_dict[industry_id] = []
        count_prj_dict[industry_id].append(row['IdProject'])
    
count_prj_dict


#%%
chart_dict = {}

for key in count_prj_dict:
    chart_dict[key] = len(count_prj_dict[key])

chart_dict

applications_sum = '{} проект'.format(sum(chart_dict.values()))

applications_sum


#%%
fig2 = {
    'data': [
        {
            'labels': loan_sums.index,
            'values': loan_sums['LoanAmount'],
            'text': value_text,
            'type': 'pie',
            'hole': 0.6,
            'title': {
                'text': total_loan,
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
            'labels': list(chart_dict.keys()),
            'values': list(chart_dict.values()),
            'text': list(chart_dict.values()),
            'type': 'pie',
            'hole': 0.6,
            'title': {
                'text': applications_sum,
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


#%%



