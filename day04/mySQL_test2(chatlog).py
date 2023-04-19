import MySQLdb
from socket import *
host = "192.168.100.31"
port = 12345

dbase = MySQLdb.connect(host='localhost', user='root', password='1234', db='chatlog')
cursor = dbase.cursor()

s = socket(AF_INET, SOCK_STREAM)
s.connect((host, port))
print("Connect to ", host)

while True:
    message = input("Message to Server : ")
    s.send(message.encode('utf-8'))
    print(s.recv(1024))
    
#     sql = "insert into chatlog(time, acceptor, message), values('%s', '%s', '%s')" %(
    
s.close()
