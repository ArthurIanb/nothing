import socket
import req_parser
import sys

# HDDRS = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"

HOST = '127.0.0.1'
PORT = int(sys.argv[1])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr[0]}")
        while True:
            data = conn.recv(1024)
            if not data:
                print("connection lost")
                break
            req = data.decode()
            try:
                response = req_parser.response(req)
            except:
                print("ERROR")
                
                break
            conn.sendall(response.encode())
