import MySQLdb

dbase = MySQLdb.connect(host='localhost', user='root', password='1234')
cursor = dbase.cursor()

dbname = input("Database name : ")
try:
    sql = "create database " + dbname + ";"
    print(sql)
    cursor.execute(sql)
    dbase.commit()
    cursor.execute("show databases")
    
    print(cursor)
    for i in cursor:
        print(i)
        
finally:
    dbase.close()