import MySQLdb
from time import localtime, strftime, sleep
import random

dbase = MySQLdb.connect(host='localhost', user='root', password='1234', db="testdbase")
cursor = dbase.cursor()

try:
    for k in range(100):
        dtime = strftime("%H:%M:%S", localtime())
        rand = random.randrange(0, 101)
        even = rand % 2
        sql = 'insert into randnum(Time, Random, evenOdd) values("%s", "%d", "%d")' % (dtime, rand, even)
    
        print(sql)
        cursor.execute(sql)
        sleep(1)
        
    dbase.commit()
    for i in cursor :
        print(i)
finally:
    dbase.close()

