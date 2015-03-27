__author__ = 'dugging'
import socket
from threading import *

host = socket.gethostname()
port = 12345                   # The same port as used by the server
Threads = [0, 0]

msg = input("Hi: ")
bob = 1
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
while bob != 0:
    msg = input("Hi: ")
    if msg == "":
        msg = "Don't put nothing!"
    elif msg == "EXIT":
        bob = 0
    s.sendall(msg.encode("ascii"))
    data = s.recv(1024)
    print("Received: ", data.decode("ascii"))
s.close()
print('Received: ', data.decode("ascii"))
