import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = input("Enter the host of the client: ")
    port = input("Enter the port of the client: ")
    int_port = int(port)

    try:
        client_socket.connect((host, int_port))
        print(f"Connected to {host}:{int_port}")

        client_message = input("Enter the expression you want to evaluate on the server: ")
        client_socket.send(client_message.encode('utf-8'))
        response_message = client_socket.recv(1024).decode('utf-8')
        print(f"Server response: {response_message}")

    except ConnectionRefusedError as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    start_client()
