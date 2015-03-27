#==================================
#|    THIS IS A TEST! (SERVER)    |
#==================================

import socket
from tkinter import *
master = Tk()

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9999
serversocket.bind(("25.198.236.56", port))
serversocket.listen(5)
while True:
    clientsocket,addr = serversocket.accept()
    print("Got a connection from %s" % str(addr))

Image = PhotoImage(file="C:\\Users\\Luke\\Documents\\GitHub\\SocketTesting\\Lukes Shit\\Hat Sim\\Art\\StadTHat.png")
clientsocket.send(Image.encode('ascii'))
serversocket.close()
