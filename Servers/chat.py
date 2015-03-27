__author__ = 'dugging'
import socket
from threading import *

threads = []


def main(conn, addr):
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data: break
        conn.sendall(data)
    print(addr, " disconnected.")
    conn.close()


host = socket.gethostname()
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(2)
while True:
    conn, addr = s.accept()
    t = Thread(target=main, args=(conn, addr))
    threads.append(t)
    t.start()