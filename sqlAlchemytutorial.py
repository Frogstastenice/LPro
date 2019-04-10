import sqlalchemy as db

#engine = db.create_engine('dialect+driver://user:pass@host:port/db')

engine = db.create_engine('mssql+pyodbc://pretender:nAJK9bqo$% 4Gi ^ w34Xko@machineslearn.database.windows.net/TestPythonAnalytics?driver=ODBC+Driver+13+for+SQL+Server)
#("mssql+pyodbc://scott:tiger@myhost:port/databasename?driver=SQL+Server+Native+Client+10.0")

connection = engine.connect()
metadata = db.MetaData()
census = db.Statuses('census', metadata, autoload=True, autoload_with=engine)

print(census.columns.keys())
