# ==================================
# |    THIS IS A TEST! (SERVER)    |
#==================================

import socket
from tkinter import *
import os

master = Tk()

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9999
serversocket.bind((socket.gethostname(), port))
serversocket.listen(5)

sb = '..\\Art\\'

os.chdir(sb)  #path

dirs = os.listdir(sb)  #list of file
print(dirs)


while True:
    clientsocket, addr = serversocket.accept()
    print("Got a connection from %s" % str(addr))
    for file in dirs:
        f = open(file, "rb")  #read image
        l = f.read()
        clientsocket.send(file.encode("ascii"))  #send the name of the file
        st = os.stat(sb + '\\' + file).st_size
        clientsocket.send(str(st).encode("utf-8"))  #send the size of the file
        clientsocket.send(l)  #send data of the file
        f.close()
    break

serversocket.close()
