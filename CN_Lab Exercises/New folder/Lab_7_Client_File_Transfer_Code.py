import socket

# create socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# set port number
port = 8000

# connect to the server
client_socket.connect((host, port))

# send a message to the server requesting a file transfer
client_socket.sendall('file'.encode())

# receive a filename from the server
filename = input('Enter the filename: ')
client_socket.sendall(filename.encode())

# receive the file data from the server
file_data = client_socket.recv(1024)

# create a new file with the received data
with open('received_file', 'wb') as f:
    f.write(file_data)

print('File transfer completed')

# send a message to the server requesting a data transfer
client_socket.sendall('data'.encode())

# send some data to the server
data = input('Enter some data: ')
client_socket.sendall(data.encode())

# close the client socket
client_socket.close()
