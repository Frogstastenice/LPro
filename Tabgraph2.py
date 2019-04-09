import csv

statuses_dict = {}
termination_statuses = {391056, 458323}

with open('Statuses.csv', 'r', encoding='utf-8') as task_file:
    fields = ['Id', 'StatusName']
    reader = csv.DictReader(task_file, fields, delimiter=',')

    for row in reader:
        status_id = row['Id']
        if status_id == '267' or status_id == '268' or status_id == '269' or status_id == '270' or status_id == '2459':
            statuses_dict[status_id] = 'Экспресс-оценка'
        elif status_id == '271' or status_id == '272' or status_id == '458325'or status_id == '458326':
            statuses_dict[status_id] = 'Входная экспертиза'
        elif status_id == '273' or status_id == '274' or status_id == '458327':
            statuses_dict[status_id] = 'Комплексная экспертиза'
        elif status_id == '275' or status_id == '276' or status_id == '277'or status_id == '278' or status_id == '458328':
            statuses_dict[status_id] = 'Экспертный совет'
        elif status_id == '279' or status_id == '20761' or status_id == '192134'or status_id == '192135':
            statuses_dict[status_id] = 'Выдача займов'


cur_application = {}
bar = ''
if cur_application['IdCurrentStatus'] in termination_statuses:
    bar = statuses_dict[cur_application['IdPreviousStatus']]
else:
    bar = statuses_dict[cur_application['IdCurrentStatus']]



print(statuses_dict)

#for row in reader:
 #       industry_id = row['ReportIndName']
  #      if not industry_id in count_prj_dict:
   #         count_prj_dict[industry_id] = []
    #    count_prj_dict[industry_id].append(row['IdProject'])
