import socket
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('ip_address')
parser.add_argument('port')
parser.add_argument('message')

args = parser.parse_args()

with socket.socket() as client_socket:
    address = (args.ip_address, int(args.port))

    client_socket.connect(address)

    data = args.message.encode()
    client_socket.send(data)
    response = client_socket.recv(1024)

    print(response.decode())
