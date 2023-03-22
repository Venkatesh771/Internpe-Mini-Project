import socket

# create socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# set port number
port = 8000

# bind socket to a public host, and a port
server_socket.bind((host, port))

# configure how many clients the server can listen to simultaneously
server_socket.listen(1)

print('Server listening on {}:{}'.format(host, port))

while True:
    # establish a connection with a client
    client_socket, addr = server_socket.accept()

    print('Got connection from', addr)

    # receive a message from the client
    message = client_socket.recv(1024).decode()

    # if the message is a file request
    if message == 'file':
        # receive the filename from the client
        filename = client_socket.recv(1024).decode()

        # open the file in binary mode
        with open(filename, 'rb') as f:
            # read the file contents
            file_data = f.read()

            # send the file data to the client
            client_socket.sendall(file_data)

        print('File transfer completed')
    # if the message is a data request
    elif message == 'data':
        # receive the data from the client
        data = client_socket.recv(1024).decode()

        # print the received data
        print('Received data:', data)

    # close the client socket
    client_socket.close()
