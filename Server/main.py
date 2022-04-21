# main.py
# The scripts in this folder are for the server script;
# For client code, go to the client folder


# Imports
import server


server.start()
while True:
    server.get_clients()