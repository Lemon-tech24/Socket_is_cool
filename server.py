import socket

s = socket.socket()

s.bind(('localhost', 8080))

s.listen(3)

print('waiting for connections')

while True:
    conn, addr = s.accept()
    name = conn.recv(1024).decode()
    print("connected with", addr, name)

    conn.send(bytes('Welcome' + name, 'utf-8'))

    conn.close()
