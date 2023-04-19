import MySQLdb

dbase = MySQLdb.connect(host='localhost', user='root', password='1234', db='testdbase')
cursor = dbase.cursor()

try:
    while True:
        sql = input("SQL : ")
        cursor.execute(sql)
        
        for i in cursor:
            print(i)
            
finally:
    dbase.close()