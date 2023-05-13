import socket
import threading
from server_functions import *

PORT = 8080
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "quit"
print(SERVER)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"NEW CONNECTION: {addr} CONNECTED")
    connected = True
    while connected:
        msg_len = conn.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(FORMAT)
            if msg != DISCONNECT_MESSAGE:
                #username
                if "username" in msg:
                    splited_msg = msg.split(':')
                    user = splited_msg[1]
                    print(user + " has connected to server")
                    conn.send("1".encode(FORMAT))
                #sender_email
                if "sender_email" in msg:
                    splited_msg = msg.split(':')
                    sender_email = splited_msg[1]
                    if check_email_existence(sender_email):
                        conn.send("1".encode(FORMAT))
                    else:
                        conn.send("0".encode(FORMAT))
                #receiver_email
                if "receiver_email" in msg:
                    splited_msg = msg.split(':')
                    receiver_email = splited_msg[1]
                    if check_email_existence(receiver_email):
                        conn.send("1".encode(FORMAT))
                    else:
                        conn.send("0".encode(FORMAT))
                #data
                if "data" in msg:
                    splited_msg = msg.split(':')
                    data = splited_msg[1]
                    data = data[:-1]
                    if send_email(sender_email, receiver_email, data):
                        conn.send("1".encode(FORMAT))
                    else:
                        conn.send("0".encode(FORMAT))
            else:
                connected = False
                print(f"{addr} disconnected.")
    conn.close()

def start():
    server.listen()
    print(f"Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args = (conn, addr))
        thread.start()
        print(f"ACTIVE Connections: {threading.active_count() - 1}\n")

print("***********STARTING************")
start()