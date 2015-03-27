# ==================================
#|    THIS IS A TEST! (Client)    |
#==================================

import socket
from tkinter import *
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()

port = 9999
sb = 'recv\\'
os.chdir(sb)

s.connect((socket.gethostname(), port))
fln = ""
size = ""
strng = ""

while True:
    while fln == "":
        fln = s.recv(1024).decode("ascii")  #read the name of the file
    f = open(fln, 'wb')  #create the new file
    while size == "":
        size = s.recv(4).decode("utf-8")  #receive the size of the file
    while strng == "":
        strng = s.recv(int(size))  #receive the data of the file
    #if strng:
    f.write(strng)  #write the file
    f.close()
    break

os.chdir("..")
root = Tk()
root.geometry("280x240")
print(fln)
directory = os.path.join(sb, os.listdir(sb)[0])

Hat = PhotoImage(file=directory)
Label = Label(root, image=Hat).pack()
