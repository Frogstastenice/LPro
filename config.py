import os

DB_NAME = os.environ.get('DB_NAME', 'TestPythonAnalytics')
DB_LOGIN = os.environ.get('DB_LOGIN', 'pretender')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'nAJK9bqo$%4Gi^w34Xko')
DB_SERVER = os.environ.get('DB_SERVER', 'machineslearn.database.windows.net')
DB_DSN = "mssql+pyodbc://{login}:{password}@{server}/{dbname}?driver=ODBC+Driver+13+for+SQL+Server".format(
    password=DB_PASSWORD,
    dbname=DB_NAME,
    login = DB_LOGIN,
    server = DB_SERVER
)
