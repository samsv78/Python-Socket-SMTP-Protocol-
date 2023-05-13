from datetime import datetime

list_of_emails = ["john@gmail.com", "sam@outlook.com"]
def check_email_existence(sender_email):
    if sender_email in list_of_emails:
        return True
    else:
        return False

def send_email(sender_email, receiver_email, data):
    try:
        if "gmail" in receiver_email:
            path = "gmail/"
        if "outlook" in receiver_email:
            path = "outlook/"
        date_time = datetime.now().strftime("%m-%d-%Y_%H:%M:%S")
        path = path + receiver_email + "/" + date_time + ".txt"
        f = open(path, "w+")
        f.write("sender_email: " + sender_email + "\nreceiver_email: " + receiver_email + "\ndata: " + data)
        f.close()
        return True
    except:
        return False
