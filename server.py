import socket
import req_parser
import sys

HOST = '127.0.0.1'
PORT = int(sys.argv[1])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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
            if req == 'shutdown':
                break
            try:
                response = req_parser.response(req)
            except:
                print("ERROR")
                s.shutdown(socket.SHUT_RD)
                break
            conn.sendall(response.encode())