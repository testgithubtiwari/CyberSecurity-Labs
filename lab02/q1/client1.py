import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = input("Enter the host of the client: ")
    port = input("Enter the port of the client: ")
    int_port = int(port)

    try:
         print("Connection refused already connected client! Server is already busy")

    except ConnectionRefusedError as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    start_client()
