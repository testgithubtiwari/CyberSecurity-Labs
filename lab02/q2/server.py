import socket
import sys
import signal
import multiprocessing

def handle_client_connection(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            result = eval(data.decode())
            client_socket.send(str(result).encode())
        except Exception as e:
            print("Error:", e)
            break
    client_socket.close()

def handle_client(client_socket, client_address):
    print(f"Connection from {client_address}")
    handle_client_connection(client_socket)

def main():
    port = int(input("Enter the port: "))
    localhost_server=input("Enter the server ip address: ")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((localhost_server, port))
    server_socket.listen(10)
    print(f"Server listening on port {port}")

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            process = multiprocessing.Process(target=handle_client, args=(client_socket, client_address))
            process.start()
            client_socket.close()

        except KeyboardInterrupt:
            print("Server terminated.")
            break
        except Exception as e:
            print("Error:", e)
            break
    server_socket.close()

if __name__ == "__main__":
    main()
