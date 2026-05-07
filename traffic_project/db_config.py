import pyodbc

def connect_db():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost\SQLEXPRESS;'
        'DATABASE=traffic_db;'
        'Trusted_Connection=yes;'
    )
    return conn