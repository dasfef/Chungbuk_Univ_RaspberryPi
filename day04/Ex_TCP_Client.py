from socket import *
host = "127.0.0.1"
port = 9999

s = socket(AF_INET, SOCK_STREAM)
s.connect((host, port))
print(s.recv(1024))
s.close()