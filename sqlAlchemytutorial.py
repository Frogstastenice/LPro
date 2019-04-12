import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from db_classes import ApplicationStatusHistory

engine = db.create_engine('mssql+pyodbc://pretender:nAJK9bqo$%4Gi^w34Xko@machineslearn.database.windows.net/TestPythonAnalytics?driver=ODBC+Driver+13+for+SQL+Server')

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

connection = engine.connect()
metadata = db.MetaData()
#ApStatHis = db.Table('ApllicationStatusHistory', metadata, autoload=True, autoload_with=engine)

#print(ApllicationStatusHistory.columns.keys())

for startdate, enddate in session.query(ApplicationStatusHistory.statusBeginDate, ApplicationStatusHistory.statusEndDate):
    print(startdate, enddate)

#for row in session.query(ApplicationStatusHistory):
 #   print(row.ApplicationStatusHistory)


#Сейчас можно поэкспериментировать. 
# Подключиться к нужной таблице БД. 
# Сделать селект, циклом пройти по всем строкам результата. 
# Для каждой строки сделать объект типа ApplicationStatusHistory, записать в список. 
# После окончания цикла вывести на экран все объекты из списка.
