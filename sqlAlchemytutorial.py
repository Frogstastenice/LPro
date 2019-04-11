import sqlalchemy as db

engine = db.create_engine('mssql+pyodbc://pretender:nAJK9bqo$%4Gi^w34Xko@machineslearn.database.windows.net/TestPythonAnalytics?driver=ODBC+Driver+13+for+SQL+Server')

connection = engine.connect()
metadata = db.MetaData()
Statuses = db.Table('Statuses', metadata, autoload=True, autoload_with=engine)

print(Statuses.columns.keys())


#Сейчас можно поэкспериментировать. 
# Подключиться к нужной таблице БД. 
# Сделать селект, циклом пройти по всем строкам результата. 
# Для каждой строки сделать объект типа ApplicationStatusHistory, записать в список. 
# После окончания цикла вывести на экран все объекты из списка.
