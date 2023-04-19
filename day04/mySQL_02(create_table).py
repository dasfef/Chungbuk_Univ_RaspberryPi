import MySQLdb

dbase = MySQLdb.connect(host='localhost', user='root', password='1234', db="testdbase")
cursor = dbase.cursor()

try:
    sql = "create table randnum(Time char(8), Random int, evenOdd int);"
    print(sql)
    cursor.execute(sql)
    dbase.commit()
    cursor.execute("show tables")
    
    for i in cursor:
        print(i)
        
finally:
    dbase.close()
