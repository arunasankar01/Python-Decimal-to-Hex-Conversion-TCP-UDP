import socket
HOST_ADDRESS = '192.168.29.158'
PORT_NUMBER = 199
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST_ADDRESS,PORT_NUMBER))
        while True:
            data,addr = s.recvfrom(1024)
            #print('Connected By',addr)
            print('Successfully connected by', addr)
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

            while (j >= 0):
                b.append(hexaDeciNum[j])
                j = j - 1

            str1 = ""
            for elem in b:
                str1 += elem

            res = str(str1)
            s.sendto(res.encode(),addr)
