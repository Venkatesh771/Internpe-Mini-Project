import socket
HOST = ''  
PORT = 12345  
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
server_socket.bind((HOST, PORT))      
server_socket.listen()      
print(f"Server listening on port {PORT}...")
while True:
client_socket, client_address = server_socket.accept()  
print(f"Connected by {client_address}")
with client_socket:
while True:
data = client_socket.recv(1024)                  
if not data:                      
break
client_socket.sendall(data)                
print(f"Received and echoed: {data.decode('utf-8').strip()}")  
