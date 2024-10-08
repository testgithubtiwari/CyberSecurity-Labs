import socket
import sys

server_busy_message = "Server busy now. Try again later!"
server_busy = False

class ServerBusyError(Exception):
    pass

def handle_client_connection(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            result = eval(data.decode())
            client_socket.send(str(result).encode())
        except ServerBusyError:
            client_socket.send("ServerBusyError".encode())
            client_socket.close()
            break
        except Exception as e:
            print("Error:", e)
            break
    client_socket.close()

def main():
    global server_busy
    port = input("Enter the port: ")
    localhost=input("Enter the server ip address: ")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((localhost, int(port)))
    server_socket.listen(1)
    print(f"Server listening on port {port}")

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")
            if server_busy:
                raise ServerBusyError
            else:
                server_busy = True
                handle_client_connection(client_socket)
                server_busy = False

        except KeyboardInterrupt:
            print("Server terminated.")
            break
        except Exception as e:
            print("Error:", e)
            break

    server_socket.close()

if __name__ == "__main__":
    main()
