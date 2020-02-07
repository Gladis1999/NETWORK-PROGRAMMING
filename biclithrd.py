import socket
from threading import Thread

def send():
	while True:
		msg=raw_input('>>')
		s.send(msg)
		if(msg=='stop'):
			break
			
def resv():
	while True:
		msg=s.recv(1024)
		print(msg)
		if(msg=='stop'):
			break

s=socket.socket()
port = input('Enter port: ')
s.connect(('127.0.0.1',port))
t1=Thread(target=resv)
t1.start()
t2=Thread(target=send)
t2.start()




