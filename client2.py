import socket
from client_functions import *

PORT = 8080
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "quit"
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)
USER = "client2"

def start():
    option = input("Enter 'smtp' to start or 'quit' to quit!\n")
    if(option == "smtp"):
        sender_email = input("Enter Sender Email: ")
        send(client, "sender_email:" + sender_email)
        result = client.recv(1).decode(FORMAT)
        if result != "1":
            print("sender email does not exist!\n")
            start()
        else:
            print("email ok\n")
        receiver_email = input("Enter Receiver Email: ")
        send(client, "receiver_email:" + receiver_email)
        result = client.recv(1).decode(FORMAT)
        if result != "1":
            print("receiver email does not exist!\n")
            start()
        else:
            print("email ok")
        print("Enter your data then write '.' and press 'enter':")
        data = ""
        new_data_input = ""
        while(new_data_input != "."):
            new_data_input = input()
            data += "\n" + str(new_data_input)

        send(client, "data:" + data)
        result = client.recv(1).decode(FORMAT)
        if result != "1":
            print("Failed to send email!\n")
        else:
            print("Email sent!\n")
        start()
    else:
        if option == "quit":
            send(client, DISCONNECT_MESSAGE)
        else:
            print("wrong input!\n")
            start()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
send(client, "username:" + USER)
result = client.recv(1).decode(FORMAT)
if result != "1":
    print("Connection to server failed!\n")
    exit(0)
print("Hello " + USER)
start()