from tkinter import Tk, Label, Entry, Button, StringVar, IntVar, DoubleVar, messagebox
from tkinter import DISABLED, NORMAL
from tkinter.ttk import Progressbar
import os
from socket import *
from PIL import Image
import numpy as np
import cv2


root = Tk()
root.title("Video transport")
root.geometry("330x220")
root.resizable(0,0)
## IP field  row = 0

Label(root, text="IP address: ").grid(row=0,column=0)

def limitSizeip(*args):
	for i in range(4):
	    value = ip[i].get()
	    if len(value) > 3: ip[i].set(value[:3])


ip = []

for i in range(4):
	ip.append(StringVar())
	ip[i].trace('w',limitSizeip)


column = 1
for i in range(4):
	dot = Label(root,text=".")
	entry = Entry(root, textvariable=ip[i], width=3)
	entry.grid(row=0,column=column)
	column+=1
	if i == 3:
		break
	dot.grid(row=0,column=column)
	column+=1

#IP = '.'.join(str(e.get()) for e in ip)
''''''


## port number row = 1
row = 1
port = StringVar()

def hello():
	Label(root, text="Wait...",width=4).grid(row=1, column=5,columnspan=2)
	try:
		if mode.get() == 0:
			get_file('.'.join(str(e.get()) for e in ip), port.get(), video_name.get(),"100")
		elif mode.get() == 1:
			get_file('.'.join(str(e.get()) for e in ip), port.get(), video_name.get(),"100")
	except:
		messagebox.showinfo("Error!", "Network Error!")

Label(root, text="Port number: ").grid(row=row, column=0)
Entry(root, textvariable=port, width=5).grid(row=row, column=1,columnspan=2)
Button(root, text='Check', width=6, command=hello).grid(row=row, column=3,columnspan=2)

## video name row = 2
row = 2
video_name = StringVar()
Label(root, text="Video name: ").grid(row=row, column=0)
Entry(root, textvariable=video_name, width=20).grid(row=row, column=1, columnspan=10)



## mode button
row = 3
mode = IntVar()
def button_1():
	mode.set(0)
	button1['fg']="black"
	button2['fg']="gray"
	print(mode)
def button_2():
	mode.set(1)
	button1['fg']="gray"
	button2['fg']="black"
	print(mode)
Label(root, text="Choose mode: ").grid(row=row, column=0)
button1 = Button(root, text='Mode A', width=9, command=button_1, fg="black")
button2 = Button(root, text='Mode B', width=9, command=button_2, fg="gray")

button1.grid(row=row, column=1, columnspan=3)
button2.grid(row=row, column=5, columnspan=3)
#button1.bind('<Button-1>',button1)
#button2.bind('<Button-1>',button2)

## public key if choose Mode B   row = 4


## progress bar  row = 5
row = 5
ratio = DoubleVar()
ratio_per = StringVar()
ratio_per.set("Progress: "+str(ratio.get()/3.0)[:3]+"%")
ratio_per_label = Label(root, textvariable=ratio_per)

ratio_per_label.grid(row=row, column=0, columnspan=10)
row = 6

file_size_int = IntVar()
progress = Progressbar(orient = 'horizontal', length=300, mode = 'determinate', variable=ratio, maximum=300)
progress.grid(row = row, column=0, columnspan=10)
## button OK  row = 6
row = 7



def get_file(HOST, PORT, file_name, request_code):
	PORT = int(PORT)
	#HOST = str(input("Enter the ip address: "))


	tcpCliSock = socket(AF_INET, SOCK_STREAM)
	tcpCliSock.connect((HOST,PORT))
	data = ""
	#sent = tcpCliSock.recv(1000).decode('utf-8')
	if mode.get() == 0:
		data = file_name[:-4]+"_encry.mp4"
	elif mode.get() == 1:
		data = "cover.mp4"

	print(data)
	tcpCliSock.send(request_code.encode())

	response = tcpCliSock.recv(1000).decode('utf-8')
	if response == request_code:
		if len(data) != 0:
			tcpCliSock.send(data.encode())
			if request_code == "100":
				file_size = tcpCliSock.recv(1000).decode('utf-8')
				try:
					file_size_int.set(int(file_size))
					file_size_str = str(int(file_size)/1024/1024)[:3]+"Mb"
					Label(root, text="OK, "+file_size_str,width=8, fg="red").grid(row=1, column=5,columnspan=3)
				except ValueError:
					Label(root, text=file_size,width=8, fg="red").grid(row=1, column=5,columnspan=3)
				
				OK_but['state']=NORMAL
			else:
				f = open("./"+data,'wb')
				stream = tcpCliSock.recv(1024)
				count = 1
				while(stream):
					f.write(stream)
					stream = tcpCliSock.recv(1024)
					ratio.set(ratio.get()+300*1024/file_size_int.get())
					ratio_per.set("Progress: "+str(ratio.get()/3.0)[:3]+"%")
					if count % 100 == 0:
						root.update()
						count = 1
					else:
						count+=1
				f.close()
				#root.after(100,get_file)
				print("Transaction sucessful")

				succ.grid(row=8, column=0, columnspan=10)
		else:
			Label(root, text="Video Name",width=8, fg="red").grid(row=1, column=5,columnspan=3)
	tcpCliSock.close()

def resize(image,width,height):
    try:
        im = Image.fromarray(image)
        new = im.resize((width,height),Image.BILINEAR)
        return np.array(new)
    except:
        return 0


def decry(video_path, cover_path,transform_number):
    out_name = video_path.split('/')[-1][:-4]+"_"+cover_path.split('/')[-1][:-4]
    #out = cv2.VideoWriter(out_name+"_decry.avi",cv2.VideoWriter_fourcc('M','J','P','G'),20.0,(480,360))
    #out = cv2.VideoWriter("../mp4/"+out_name+"_decry.mp4",cv2.VideoWriter_fourcc(*'mp4v'),25.0,(480,360))
    origin_cap = cv2.VideoCapture(video_path)
    cover_cap = cv2.VideoCapture(cover_path)
    while(origin_cap.isOpened()):
        origin_ret, origin_frame = origin_cap.read()
        cover_ret, cover_frame = cover_cap.read()
        if (cover_ret == False):
            cover_cap.release()
            cover_cap = cv2.VideoCapture(str(cover_path))
            cover_ret, cover_frame = cover_cap.read()
        #origin_frame = resize(origin_frame,480,360)
        cover_frame = resize(cover_frame,480,360)
        blur = origin_frame - np.uint8(np.ceil(cover_frame / 2))
        blur*=transform_number
        '''if(origin_ret == True):
            pass
            #out.write(blur)
        else:
            break'''
        cv2.imshow("blur",blur)
        if cv2.waitKey(25) & 0xFF == ord(' '):
        	while 1:
        		#cv2.imshow("blur",blur)
        		if cv2.waitKey(25) & 0xFF == ord(' '):
        			break
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        
    origin_cap.release()
    cover_cap.release()
    #out.release()
    cv2.destroyAllWindows()





def press_button3():
	try:
		if mode.get() == 0:
			get_file('.'.join(str(e.get()) for e in ip), port.get(), video_name.get(),"101")
		elif mode.get() == 1:
			get_file('.'.join(str(e.get()) for e in ip), port.get(), "cover.mp4","102")
		else:
			messagebox.showinfo("Error", "Choose a mode")
	except:
		messagebox.showinfo("Error", "Unknown Error")

def press_button4():
	if mode.get() == 0:
		os.system("open "+video_name.get())
	if mode.get() == 1:
		decry(video_name.get()[:-4]+"_encry.mp4","cover.mp4",11)





OK_but = Button(root, text='OK', width=9, command=press_button3, state=DISABLED)
view_but = Button(root, text='View', width=9, command=press_button4)

OK_but.grid(row=row, column=1, columnspan=3)
view_but.grid(row=row, column=4, columnspan=3)



# message line row = 8

succ = Label(root, text="Transaction is sucessful! ", fg="red")








root.mainloop()