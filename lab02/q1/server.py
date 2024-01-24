import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 568
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    # Flag to track whether a client is connected
    client_connected = False

    while True:
        if not client_connected:
            try:
                # Accept a connection from a client
                client_socket, client_address = server_socket.accept()
                print(f"Connection from {client_address}")

                # Set the flag to indicate a client is connected
                client_connected = True

                client_message = client_socket.recv(1024).decode('utf-8')
                print(client_message)

                try:
                    result = eval(client_message)
                    response_server = str(result)
                except Exception as e:
                    response_server = f"Error: {str(e)}"

                client_socket.send(response_server.encode('utf-8'))

            except Exception as e:
                # Send a message indicating that the server is busy to the upcoming client
                busy_message = "Server is busy. Try again later."
                client_socket.send(busy_message.encode('utf-8'))

                print(f"Error: {str(e)}")
            finally:
                # Reset the flag after serving the client
                client_connected = False

                # Close the connection
                client_socket.close()
                print(f"Connection with {client_address} closed")

    # Close the server socket (this line won't be reached in the current implementation)
    server_socket.close()

if __name__ == "__main__":
    start_server()
