#==================================
#|    THIS IS A TEST! (Client)    |
#==================================

import socket
from tkinter import *
root = Tk()
root.geometry("280x240")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()                           

port = 9999

s.connect((host, port))                               

TopHat = s.recv(1024)                                     
Label = Label(root, image = TopHat.decode)
