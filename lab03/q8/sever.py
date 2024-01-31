import socket

# Define the server host and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((SERVER_HOST, SERVER_PORT))

# Listen for incoming connections
server_socket.listen(1)

print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

# Accept incoming connections
client_socket, client_address = server_socket.accept()

print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")

# Receive data from the client
data = client_socket.recv(1024)
print(f"[*] Received: {data.decode()}")

# Close the connection
client_socket.close()
server_socket.close()
