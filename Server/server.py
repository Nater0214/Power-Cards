# server.py
# Handles server stuff


# Imports
import socket
from threading import Thread


# Methods
def start():
    """Perfom actions nessecary to start the server"""
    # Create socket
    global sock; sock = socket.socket()

    # Get the host port
    e = True
    while e:
        try:
            inp = input("Host port (leave blank for recomended: 21408): ")
            assert inp.isdigit() or inp == ''
            if inp == '': port = 21408
            else: port = int(inp)
        except: pass
        else: e = False

    # Bind socket
    sock.bind((socket.gethostbyname(socket.gethostname()), port))
    sock.listen()


def get_clients():
    """Get new clients that connect to the server"""
    conn, addr = sock.accept()
    thrd = Thread(target=client_listen, args=(conn, addr))
    thrd.start()


def client_listen(conn, addr):
    """Listens for data comming from a client"""
    print(f"New connection from {addr[0]}:{addr[1]}")
    while True:
        data = conn.recv(64)
        if data != b'': print(data.decode())
        else: continue