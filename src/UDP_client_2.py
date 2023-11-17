import socket

HOST_ADDRESS = '192.168.29.158'
PORT_NUMBER = 199

ss = input('Enter an integer: ')
with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
    s.sendto(bytes(ss,'utf-8'),(HOST_ADDRESS,PORT_NUMBER))
    data = s.recv(1024)
    res=data.decode("utf-8")
    str_res = str(res)

print('Result (in Hexadecimal) :', str_res)