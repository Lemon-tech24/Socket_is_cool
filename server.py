import socket

s = socket.socket()
ipaddr = socket.gethostbyname(socket.gethostname())
s.bind((ipaddr, 8080))

s.listen(3)

print('waiting for connections')
allowed_conn = 5
while True:
    conn, addr = s.accept()
    name = conn.recv(1024).decode()
    print("connected with", addr, name)

    conn.send(bytes('Welcome' + name, 'utf-8'))

    conn.close()
