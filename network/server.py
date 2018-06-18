import importlib.util
from socket import *
import sys
# If covered file not exist , then run the following to create mp4
'''
spec = importlib.util.spec_from_file_location("server_process", "/Users/joe/Desktop/Video-Faker/video-processing/server_process.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)


foo.encry("../example-videos/origin.mp4","../test_image/cover.mp4",9,0)
'''

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(('', 8080))
tcpSerSock.listen(1)

while 1:
	print('Ready to serve...')
	tcpCliSock, addr = tcpSerSock.accept()
	print('Received a connection from:', addr)
	try:
		tcpCliSock.send(b'Please Enter the video name: ')
		message = tcpCliSock.recv(1024).decode('utf-8')
		print(message)
		f = open("./"+message,'rb')
		data = f.read(1024)
		while(data):
			print("Sending")
			tcpCliSock.send(data)
			data = f.read(1024)
		print("transaction sucessful")
		tcpCliSock.shutdown(SHUT_WR)
	except:
		pass
