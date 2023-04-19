import MySQLdb
from socket import *
from time import localtime, strftime, sleep

host = "192.168.100.42"
port = 12345

dbase = MySQLdb.connect(host='localhost', user='root', password='1234', db='chatlog')
cursor = dbase.cursor()

s = socket(AF_INET, SOCK_STREAM)
s.bind((host, port))

s.listen(1)
print("Listening for Connection :", host)
conn = None

while True :
    dtime = strftime("%H:%M:%S", localtime())
    if conn is None:
        print("Waiting : ")
        conn, addr = s.accept()
        print("Connection form ", addr)
    else :
        text = str(conn.recv(1024))
        print(text)
        conn.send(b'OK')
        sql = 'insert into chatlog(time, acceptor, message) values("%s", "%s", "%s")' %(dtime, conn.getsockname()[0], text.replace("\n",""))
        cursor.execute(sql)
        dbase.commit()
conn.close()
dbase.close()

