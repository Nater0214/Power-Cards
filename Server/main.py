# main.py
# The scripts in this folder are for the server script;
# For client code, go to the client folder


# Imports
import socket


# Create socket
sock = socket.socket()

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
conn, addr = sock.accept()
with conn:
    print(f"Connected from {addr}")

