"""

Python program to retrieve a web page over a socket and display the headers from the web server.
http://data.pr4e.org/intro-short.txt is the URL being used here

"""

import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect(('data.pr4e.org', 80))
# \r\n\r\n or \n\n
mySocket.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode())

while True:
    data = mySocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
mySocket.close()