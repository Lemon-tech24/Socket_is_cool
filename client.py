import socket

c = socket.socket()

c.connect(('192.168.0.104', 8080))

name = input("Enter your name: ")
c.send(bytes(name, 'utf-8'))
print(c.recv(1024).decode())
