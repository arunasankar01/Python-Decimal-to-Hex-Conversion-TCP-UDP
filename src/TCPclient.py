import socket

HOST = '192.168.29.158'
PORT = 7

ss = input('Enter an integer: ')
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.send(bytes(ss,'utf-8'))
    data = s.recv(1024)
    res=data.decode("utf-8")
    ans=int(0)
    base=0
    for i in res:
        if(i>='0' and i<='9'):
            ans+=int(i)*pow(10,base)
            base+=1
print('Result :', ans)