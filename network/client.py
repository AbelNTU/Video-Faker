import socket
from socket import *
import sys

HOST, PORT = sys.argv[1], 8080


tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect((HOST,PORT))

sent = tcpCliSock.recv(1000).decode('utf-8')
data = input(sent)

f = open("./"+data,'wb')

tcpCliSock.send(data.encode())

print("get stream from ", sys.argv[1])
print("Receiving...")

stream = tcpCliSock.recv(1024)
while(stream):
	print("Receiving")
	f.write(stream)
	stream = tcpCliSock.recv(1024)

f.close()

print("Transaction sucessful")

tcpCliSock.close()
