import socket
HOST = 'localhost'  
PORT = 12345  
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
client_socket.connect((HOST, PORT))  
print(f"Connected to {HOST}:{PORT}...")
while True:
message = input("Enter message to send (press enter to quit): ")
if not message:  
break
client_socket.sendall(message.encode('utf-8'))  
data = client_socket.recv(1024)  
print(f"Received: {data.decode('utf-8').strip()}")  
