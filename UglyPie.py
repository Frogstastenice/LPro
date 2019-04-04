import pandas as pd
import numpy as np
import plotly.offline as py
import plotly.graph_objs as go

data = pd.read_csv('Tabgraph1.csv')
loan_industries = data[['LoanAmount', 'ReportIndName']]
#loan_industries.head()

group = loan_industries.groupby('ReportIndName')
loan_sums = group.aggregate(np.sum)
#loan_sums

py.init_notebook_mode()
pie = go.Pie( labels=loan_sums.index, values=loan_sums['LoanAmount'], hole=0.6,
title = 'First Chart')

py.iplot([pie])
