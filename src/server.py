import socket
s= socket.socket()
print("Socket created")

s.bind(('localhost',9999))

s.listen()
print('waiting for connections')

while True:
    c, addr= s.accept()
    print("connected with ",addr)

    c.send('welcome')

    c.close()