import socket
import sys
import config

HOST = '127.0.0.1'
if len(sys.argv) == 2:
    PORT = int(sys.argv[1])
else:
    PORT = 8000
# config.help_text_en()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = input()
        if bytes(data.encode()) == bytes([116, 114, 111, 108, 108, 102, 97, 99, 101]):
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

