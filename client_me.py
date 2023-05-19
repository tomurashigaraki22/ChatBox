import socket

HOST = '127.0.0.1'  # replace with the server IP address if it's running on a different machine
PORT = 22345  # same port number as the server

# create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # connect to the server
    s.connect((HOST, PORT))
    
    # send and receive messages
    while True:
        message = input('You: ')
        s.sendall(message.encode())
        data = s.recv(1024)
        print(f'Client 2: {data.decode()}')
