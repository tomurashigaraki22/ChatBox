import socket

HOST = '127.0.0.1'  # empty string represents localhost
PORT = 22345  # choose a port number

# create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # bind the socket to a specific address and port
    s.bind((HOST, PORT))
    
    # listen for incoming connections
    s.listen()
    
    print(f'Server is listening on port {PORT}')
    
    # wait for two clients to connect
    conn1, addr1 = s.accept()
    print(f'Connected by {addr1}')
    f = open('ip.txt', 'a')
    f.write(f'Connected by {addr1}\n')
    
    conn2, addr2 = s.accept()
    print(f'Connected by {addr2}')
    f = open('ip.txt', 'a')
    f.write(f'Connected by {addr2}\n')

    
    # communicate between the two clients
    while True:
        # receive and send messages between the clients
        data = conn1.recv(1024)
        conn2.sendall(data)
        print(f'Received from {addr1}: {data.decode()}')
        
        data = conn2.recv(1024)
        conn1.sendall(data)
        print(f'Received from {addr2}: {data.decode()}')
