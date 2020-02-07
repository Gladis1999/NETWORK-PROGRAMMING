import socket
from threading import Thread

def send(): 
	while True:
		msg=raw_input('>>')
		con.send(msg)
		if(msg=='stop'):
			break
			
def resv():
	while True:
		msg=con.recv(1024)
		print(msg)
		if(msg=='stop'):
			break

s=socket.socket()
port = input('Enter port: ')
s.bind(('127.0.0.1',port))
s.listen(5)
con,addr=s.accept()
t1=Thread(target=send)
t1.start()
t2=Thread(target=resv)
t2.start()


