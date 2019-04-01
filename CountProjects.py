import csv

count_prj_dict = {}

with open('Tabgraph1.csv', 'r', encoding='utf-8') as new_file:
    reader = csv.DictReader( new_file, fieldnames=['IdProject', 'LoanAmount',
    'IdIndustry', 'IdReportIndustry', 'ReportIndName'],
    delimiter=',')
    next(reader)
    for row in reader:
        industry_id = row['IdReportIndustry']
        if not industry_id in count_prj_dict:
            count_prj_dict[industry_id] = []
        count_prj_dict[industry_id].append(row['IdProject'])
    
    print(count_prj_dict)

    #for row in reader:
     #   count_prj_dict[row['IdReportIndustry']] = row['IdProject']
    #  print(count_prj_dict)


#Но перед этим тебе надо:
#1) Правильно извлечь в переменную industry_id
#2) Проверить есть ли ключ равный значению переменной industry_id 
# в словаре count_prj_dict.
#3) Если нет, то задать что count_prj_dict[industry_id]=пустому списку
