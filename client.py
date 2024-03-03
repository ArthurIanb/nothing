import socket
import sys
import config

HOST = '127.0.0.1'
PORT = int(sys.argv[1])
print("HELLO")
print("Available commands:")
print("add username bio - creates user")
print("get inf - inf can be 'fieldname value' or 'all'")
print("rem fieldname value - removes all raws where fieldname == value")
print("To exit type 'c'")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = input()
        if bytes(data.encode()) == bytes([110, 105, 103, 103, 97]):
            print(config.easter_egg)
            break
        if data == 'c':
            print("Bye")
            break
        s.sendall(data.encode())
        back_data = s.recv(1024)
        if not back_data:
            break
        print(back_data.decode())

