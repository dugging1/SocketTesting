# server.py 
import socket                                         
import time

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999                                           

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()
    tm = ''.encode('ascii')
    #print("*UY^TREW2")
    #print(tm.decode('ascii'))
    while tm.decode('ascii') == '':
        tm = serversocket.recv(1024)
        print("received: " + tm.decode('ascii'))
        clientsocket.send(tm)
    else:
        break
        
    
#print("Got a connection from %s" % str(addr))
#currentTime = time.ctime(time.time()) + "\r\n"
#clientsocket.send(currentTime.encode('ascii'))
#clientsocket.close()

