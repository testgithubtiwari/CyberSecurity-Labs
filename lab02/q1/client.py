import socket
import sys

def main():

    port_server = input("Enter the port: ")
    localhost_server=input("Enter the server ip address: ")

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((localhost_server, int(port_server)))
    except ConnectionRefusedError:
        print("Server is busy. Please try again later.")
        return

    print("Connected to server.")
    try:
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
