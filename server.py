import socket
import req_parser
import sys

HDDRS = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"

HOST = '127.0.0.1'
PORT = int(sys.argv[1])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {conn}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print('Data', data.decode())
            conn.sendall(req_parser.parse_data(data.decode()).encode())
