import importlib.util
from socket import *
import sys
import os
# If covered file not exist , then run the following to create mp4
'''
spec = importlib.util.spec_from_file_location("server_process", "/Users/joe/Desktop/Video-Faker/video-processing/server_process.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)


foo.encry("../example-videos/origin.mp4","../test_image/cover.mp4",9,0)
'''

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(('', 8787))
tcpSerSock.listen(1)

while 1:
	print('Ready to serve...')
	tcpCliSock, addr = tcpSerSock.accept()
	print('Received a connection from:', addr)
	try:
		request_code = tcpCliSock.recv(1024).decode('utf-8')
		if request_code in ["100", "101", "102"]:
			print(request_code)
			tcpCliSock.send(request_code.encode())
			message = tcpCliSock.recv(1024).decode('utf-8')

			if request_code == "100":
				try:
					size = os.path.getsize("./"+message)
					size_str = str(size)
				except:
					size_str = "Video Not Exist"
				tcpCliSock.send(size_str.encode())
			else:
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
