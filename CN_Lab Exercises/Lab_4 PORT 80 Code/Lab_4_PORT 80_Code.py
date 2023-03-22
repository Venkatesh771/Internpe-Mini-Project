#4.Server And Client Port 80:
import socket
HOST = 'www.google.com'
PORT = 80 # HTTP port
message = f"GET /index.html HTTP/1.1\r\nHost: {HOST}\r\n\r\n"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
client_socket.connect((HOST, PORT))
print(f"Connected to {HOST}:{PORT}...")
client_socket.sendall(message.encode('utf-8'))
response = b''
while True:
data = client_socket.recv(1024)
if not data: # break the loop if no more data received
break
response += data
print(response.decode('utf-8'))
