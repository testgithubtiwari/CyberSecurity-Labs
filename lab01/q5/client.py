import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12346
    client_socket.connect((host, port))
    print(f"Connected to {host}:{port}")

    client_message = input("Enter the message from client to server: ")
    client_socket.send(client_message.encode('utf-8'))
    
    
    response_message = client_socket.recv(1024).decode('utf-8')
    print(f"Server response: {response_message}")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_client()
