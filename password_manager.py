from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return


pswrd = input("Enter a master password: ")
key = load_key()
fer = Fernet(key)
def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("Account:", user, "| Password:", passw)


def add():
    name = input("Account Name: ")
    password = input("Password:")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + password + "\n")

while True:
    mode = input("Would you like to add or view a password? (add/view), press q to quit:").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
