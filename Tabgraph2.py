import csv

statuses_dict = {}
project_start = {}
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


with open('ApplicationStatusHistory.csv', 'r', encoding='utf-8') as task_file2:
    fields2 = ['Id', 'IdProject', 'IdCurrentStatus', 'IdPreviousStatus', 'StatusBeginDate', 'StatusEndDate']
    reader2 = csv.DictReader(task_file2, fields2, delimiter=',')

    for row2 in reader2:
        if row2['IdCurrentStatus'] == '268':
            project_start[row2['IdProject']] = row2['StatusBeginDate']

print(statuses_dict)
print(project_start)


#cur_application = {}
#bar = ''
#if cur_application['IdCurrentStatus'] in termination_statuses:
 #   bar = statuses_dict[cur_application['IdPreviousStatus']]
#else:
 #   bar = statuses_dict[cur_application['IdCurrentStatus']]

