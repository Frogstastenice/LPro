import pyodbc

server = 'machineslearn.database.windows.net'
database = 'TestPythonAnalytics'
username = 'pretender'
password = 'nAJK9bqo$%4Gi^w34Xko'
driver = '{ODBC Driver 13 for SQL Server}'

cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server +
                      ';PORT=1443;DATABASE='+database+';UID='+username+';PWD=' + password)

cursor = cnxn.cursor()
cursor.execute("SELECT * FROM Industries")
row = cursor.fetchone()
while row:
    print(row[1])
    row = cursor.fetchone()
