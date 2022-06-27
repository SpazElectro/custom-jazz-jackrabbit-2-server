import socket

def start():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 10052))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        print(conn, addr)
        conn.close()
