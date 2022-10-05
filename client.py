import socket

ip = '127.0.0.1'
port = 8000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((ip, port))


while True:
    client.sendall(str(input('>')).encode())