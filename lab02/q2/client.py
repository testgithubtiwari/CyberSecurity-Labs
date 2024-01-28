import socket
import sys

def main():
    server_ip = input("Enter the server ip address: ")
    server_port = input("Enter the port: ")

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip,int(server_port)))
        print("Connected to server.")
        while True:
            expression = input("Enter arithmetic expression: ")
            client_socket.send(expression.encode())
            result = client_socket.recv(1024).decode()
            print("Result:", result)

    except KeyboardInterrupt:
        print("Client terminated.")
    except Exception as e:
        print("Error:", e)
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
