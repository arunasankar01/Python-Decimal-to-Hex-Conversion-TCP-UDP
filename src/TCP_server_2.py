import socket

HOST_ADDRESS = '192.168.29.158'
PORT_NUMBER = 99
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print("Socket has been successfully created")
            s.bind(('',PORT_NUMBER))
            print("Socket is binded to %s" % (PORT_NUMBER))
            s.listen()
            print("Socket is listening")
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    xx = data.decode("utf-8")
                    n=int(xx)
                    b=[]
                    hexaDeciNum = ['0'] * 100
                    i = 0
                    while (n != 0):
                        temp = 0
                        temp = n % 16
                        # check if temp < 10
                        if (temp < 10):
                            hexaDeciNum[i] = chr(temp + 48)
                            i = i + 1
                        else:
                            hexaDeciNum[i] = chr(temp + 55)
                            i = i + 1
                        n = int(n / 16)

                    j = i - 1

                    while (j>=0):
                        b.append(hexaDeciNum[j])
                        j = j - 1

                    str1 = ""
                    for elem in b:
                        str1 += elem

                    res = str(str1)
                    conn.send(res.encode("utf-8"))
                    #conn.close()