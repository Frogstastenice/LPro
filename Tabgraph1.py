import csv

ind_dict = {}
ind_dict_name = {}

def table_writer():
    new_row['IdProject'] = row['IdProject']
    new_row['LoanAmount'] = row['LoanAmount']
    new_row['IdIndustry'] = row['IdIndustry']
    new_row['IdReportIndustry'] = ind_dict[row['IdIndustry']]
    new_row['ReportIndName'] = ind_dict_name[new_row['IdReportIndustry']]
    writer.writerow(new_row) 

with open('Industries.csv', 'r', encoding='utf-8') as task_file2:
    fields2 = ['Id', 'IndustryName', 'IdReportIndustry']
    reader2 = csv.DictReader(task_file2, fields2, delimiter=',')
    
    for row2 in reader2:
        t_id=row2['Id']
        ind_dict[t_id] = row2['IdReportIndustry']

with open('ReportIndustries.csv', 'r', encoding='utf-8') as task_file3:
    fields3 = ['Id', 'ReportIndustryName']
    reader3 = csv.DictReader(task_file3, fields3, delimiter=',')

    for row3 in reader3:
        t_name_id = row3['Id']
        ind_dict_name[t_name_id] = row3['ReportIndustryName'].strip(' ')
#print(ind_dict_name)   

with open('Application.csv', 'r', encoding='utf-8') as task_file:
    fields = ['IdProject',
              'IdCompany',
              'IdManager',
              'IdSupportProgram',
              'LoanAmount',
              'IdIndustry',
              'IdStatus',
              'IdSubindustry',
              'IdRegion',
              'ApplicationNumber',
              'ProjectName',
              'Locality',
              'LoanAgreementDate',
              'IdBudget',
              'LoanAgreementPayement',
              'IdRegionalFund'
              ]
    reader = csv.DictReader(task_file, fields, delimiter=',')
    with open('Tabgraph1.csv', 'w', encoding='utf-8') as new_file:
        # fields_2 = ['IdProject','LoanAmount' 'IdIndustry']
        writer = csv.DictWriter(
        new_file, 
            fieldnames=['IdProject', 'LoanAmount',
                        'IdIndustry', 'IdReportIndustry','ReportIndName'],
        delimiter=',')
        writer.writeheader()
        next(reader)
        for row in reader:
            new_row = {}
            if row['IdStatus'] == '3126345':
                table_writer()
            elif row['IdStatus'] == '7552031':
                table_writer()
            elif row['IdStatus'] == '7552032':
                table_writer()
            elif row['IdStatus'] == '20761':
                table_writer() 

        
