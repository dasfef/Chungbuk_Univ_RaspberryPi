from socket import *
host = "127.0.0.1"
port = 9999

s = socket(AF_INET, SOCK_STREAM)
s.bind((host, port))

s.listen(1)
print("Listening for Connection : ", host)

while True:
    conn, addr = s.accept()
    print("Connection form ", addr)
    conn.send(b'Connection OK')

conn.close()