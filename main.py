def create():
    username = input("Create Username: ")
    password = input("Create Password: ")
    new_file = open("account_details.txt", "a")
    new_file.write(username + "\n")
    new_file.write(password + "\n")
    new_file.close()


def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    read_file = open("account_details.txt", "r")
    read1 = read_file.readline().strip()
    read2 = read_file.readline().strip()
    while not (read1 == username or read2 == password) and read1 != "":
        read1 = read_file.readline().strip()
        read2 = read_file.readline().strip()
    if read1 == username and read2 == password:
        print("Welcome")
    elif read1 == username and read2 != password:
        print("Password incorrect")
    elif read1 != username and read2 == password:
        print("Username Incorrect")
    else:
        print("Username and Password Incorrect")
    
login()
