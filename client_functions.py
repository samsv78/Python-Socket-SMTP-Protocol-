HEADER = 64
FORMAT = "utf-8"

def get_message_len_based_on_header(message_len_str):
    if len(message_len_str) > HEADER:
        print("your message is too long!")

    while len(message_len_str) < HEADER:
        message_len_str += " "
    return message_len_str

def send(client, msg):
    message = msg.encode(FORMAT)
    message_len_str = get_message_len_based_on_header(str(len(message)))
    client.send(message_len_str.encode(FORMAT))
    client.send(message)