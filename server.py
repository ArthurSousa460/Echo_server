import socket


ip = '0.0.0.0'
port = 8000

server  = socket.socket(socket.AF_INET, socket. SOCK_STREAM)

server.bind((ip, port))

server.listen(5)

print(f'Escutando no ip {ip} na porta {port}')

obj, client = server.accept()
print(f'Conexão recebida de {client[0]}')

while True:
    
    msg = obj.recv(1024)
    print(msg.decode())

    if msg.decode() == 'exit\n':
        print(msg)
        server.close()