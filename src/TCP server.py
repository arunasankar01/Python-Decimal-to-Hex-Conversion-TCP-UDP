import socket

HOST = '192.168.29.158'
PORT = 7
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print("Socket successfully created")
            s.bind(('',PORT))
            print("socket binded to %s" % (PORT))
            s.listen()
            print("socket is listening")
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    xx = data.decode("utf-8")
                    x=int(xx)
                    b=[]
                    while(x>=1):
                        b.append(int(x%2))
                        x=x/2
                    res=str(b)
                    conn.send(res.encode("utf-8"))