# ==================================
#|    THIS IS A TEST! (Client)    |
#==================================

import socket
from tkinter import *
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = input("IP: ")
port = 9999
sb = 'recv\\'
os.chdir(sb)

s.connect((IP, port))
input("Test: ")
fln = ""
size = ""
strng = ""

while True:
    while fln == "":
        fln = s.recv(1024).decode("ascii")
    f = open(fln, 'wb')
    while size == "":
        size = s.recv(4).decode("utf-8")
    while strng == "":
        strng = s.recv(int(size))
    f.write(strng)
    f.close()
    break

os.chdir("..")
root = Tk()
root.geometry("280x240")
print(fln)
directory = os.path.join(sb, os.listdir(sb)[0])

Hat = PhotoImage(file=directory)
Label = Label(root, image=Hat).pack()
