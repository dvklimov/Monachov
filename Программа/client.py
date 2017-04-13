# -*- coding: utf-8 -*- 

import socket
from Tkinter import *
import sys
import random
import base64
from Crypto.Util import number

#Решаем вопрос с кирилицей
reload(sys)
sys.setdefaultencoding('utf-8')
#-----------------------------

tk=Tk()
f = open('g.txt','r')
g = int(f.readline())
f.close()

f = open('p.txt','r')
p = int(f.readline())
f.close()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('0.0.0.0',11719))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)

text=StringVar()
name=StringVar()
name.set('HabrUser')
text.set('')
tk.title('MegaChat')
tk.geometry('400x300')

log = Text(tk)
nick = Entry(tk, textvariable=name)
msg = Entry(tk, textvariable=text)
msg.pack(side='bottom', fill='x', expand='true')
nick.pack(side='bottom', fill='x', expand='true')
log.pack(side='top', fill='both',expand='true')

def loopproc():
	log.see(END)
	s.setblocking(False)
	try:
		message = s.recv(128)
		log.insert(END,message+'\n')
	except:
		tk.after(1,loopproc)
		return
	tk.after(1,loopproc)
	return

def sendproc(event):
	sock.sendto (name.get()+':'+text.get(),('255.255.255.255',11719))
	text.set('')

msg.bind('<Return>',sendproc)

msg.focus_set()

tk.after(1,loopproc)
tk.mainloop()
# Begin
print("INPUT:")
print("p= ",p)
print("g= ",g)

# Alice Sends Bob A = g^a mod p
#get random a
a = int(random.uniform(1,g))
print("a= ",a)
A = pow(g,a,p)#(g**a)%p	
# Bob Sends Alice B = g^b mod p
b = int(random.uniform(1,g))
print("b= ",b)
B = pow(g,b,p)#(g**b)%p
# Alice Computes Shared Secret: s = B^a mod p
KAlice = pow(B,a,p)#(B**a)%p
print("key ALice:",KAlice)
# Bob Computes Shared Secret: s = A^b mod p
KBob = pow(A,b,p)#(A**b)%p
print("Key Bob",KBob)