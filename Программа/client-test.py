import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8007
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
data = conn.recv(1000000)
print ("client is at", addr , data)
conn.send(data)
conn.close()