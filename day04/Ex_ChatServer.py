from socket import *
host = "192.168.100.31"
port = 12345

s = socket(AF_INET, SOCK_STREAM)
s.connect((host, port))
print("Connect to ", host)

while True:
    message = input("Message to Server : ")
    s.send(message.encode('utf-8'))
    print(s.recv(1024))
    
s.close()