import socket
import sys
HOST = '127.0.0.1'
PORT = int(sys.argv[1])
print("HELLO")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = input()
        if data == 'c':
            print("Bye")
            break
        s.sendall(data.encode())
        back_data = s.recv(1024)
        if not back_data:
            break
        print(back_data.decode())

