import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12346
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    
    client_message = client_socket.recv(1024).decode('utf-8')
    
    message_uppercase=client_message.upper()
    client_socket.send(message_uppercase.encode('utf-8'))

    # Close the connection
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
