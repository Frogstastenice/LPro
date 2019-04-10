import csv

statuses_dict = {}
termination_statuses = {391056, 458323}

with open('Statuses.csv', 'r', encoding='utf-8') as task_file:
    fields = ['Id', 'StatusName']
    reader = csv.DictReader(task_file, fields, delimiter=',')

    for row in reader:
        status_id = row['Id']
        if status_id in {'267', '268', '269', '270', '2459'}:
            statuses_dict[status_id] = 'Экспресс-оценка'
        elif status_id in {'271', '272', '458325', '458326'}:
            statuses_dict[status_id] = 'Входная экспертиза'
        elif status_id in {'273', '274', '458327'}:
            statuses_dict[status_id] = 'Комплексная экспертиза'
        elif status_id in {'275', '276', '277', '278', '458328'}:
            statuses_dict[status_id] = 'Экспертный совет'
        elif status_id in {'279', '20761', '192134', '192135'}:
            statuses_dict[status_id] = 'Выдача займов'


#cur_application = {}
#bar = ''
#if cur_application['IdCurrentStatus'] in termination_statuses:
 #   bar = statuses_dict[cur_application['IdPreviousStatus']]
#else:
 #   bar = statuses_dict[cur_application['IdCurrentStatus']]



print(statuses_dict)

#for row in reader:
 #       industry_id = row['ReportIndName']
  #      if not industry_id in count_prj_dict:
   #         count_prj_dict[industry_id] = []
    #    count_prj_dict[industry_id].append(row['IdProject'])
