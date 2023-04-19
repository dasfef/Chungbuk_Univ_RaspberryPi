
from socket import *
host = "192.168.100.42"
port = 12345

s = socket(AF_INET, SOCK_STREAM)
s.bind((host, port))

s.listen(1)
print("Listening for Connection :", host)
conn = None

while True :
	if conn is None:
		print("Waiting : ")
		conn, addr = s.accept()
		print("Connection form ", addr)
	else :
		print(conn.recv(1024))
		conn.send(b'OK')
		
conn.close()
