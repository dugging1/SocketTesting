#==================================
#|    THIS IS A TEST! (SERVER)    |
#==================================

import socket
from tkinter import *
import os
from threading import *
IP = input("IP: ")

threads = []
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9999
serversocket.bind((IP, port))
serversocket.listen(5)

sb = '..\\Art\\'

def program(clientsocket, addr):
    sb = '..\\Art\\'
    os.chdir(sb)
    dirs = os.listdir(sb)
    while True:
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

serversocket.listen(5)
while True:
    CS, ADDR = serversocket.accept()
    print("Got a connection from %s" % str(ADDR))
    t = Thread(target=program, args=(CS, ADDR))
    threads.append([t, CS, ADDR])
    t.start()
