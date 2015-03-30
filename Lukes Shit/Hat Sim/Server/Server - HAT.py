#==================================
#|    THIS IS A TEST! (SERVER)    |
#==================================

import socket
import os
from threading import *
import World


def init():
    global IP
    global threads
    global serversocket
    global port
    global sb
    IP = input("IP: ")
    threads = []
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 9999
    serversocket.bind((IP, port))
    serversocket.listen(5)
    sb = '..\\Art\\'
    serversocket.listen(5)


def program(clientsocket, addr):
    os.chdir(sb)
    dirs = os.listdir(sb)
    for file in dirs:
        f = open(file, "rb")
        l = f.read()
        clientsocket.send(file.encode("ascii"))
        st = os.stat(sb + '\\' + file).st_size
        clientsocket.send(str(st).encode("utf-8"))
        clientsocket.send(l)
        f.close()
    for x in range(len(threads)):
        if threads[x][1] == clientsocket:
            threads.remove(threads[x])
            break

serversocket.listen(5)

while True:
    print("Getting connection")
    CS, ADDR = serversocket.accept()
    print("Got a connection from %s" % str(ADDR))
    t = Thread(target=program, args=(CS, ADDR))
    threads.append([t, CS, ADDR])
    t.start()
