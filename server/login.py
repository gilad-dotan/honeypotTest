
# {(username, password), numOfCombinationTried}
failedAttempts = {}
# {username, number of attempts}
failedUsernames = {}
# {password, number of attempts}
failedPasswords = {}

def addFailedAttempt(username, password):
    combination = (username, password)
    if combination in failedAttempts:
        failedAttempts[combination] += 1
    else:
        failedAttempts[combination] = 1

    if username in failedUsernames:
        failedUsernames[username] += 1
    else:
        failedUsernames[username] = 1

    if password in failedPasswords:
        failedPasswords[password] += 1
    else:
        failedPasswords[password] = 1

    print(f"failed attempts = {failedAttempts}")
    print(f"failed usernames = {failedUsernames}")
    print(f"failed usernames = {failedUsernames}")
    print(failedUsernames)
    print(failedPasswords)

def login(soc, _username, _password, limitTries):

    soc.sendall("please enter you username: ".encode())
    username = soc.recv(1024).decode()

    soc.sendall("please enter you password: ".encode())
    password = soc.recv(1024).decode()

    # making sure that the user hadn't reached the limit of tries
    if limitTries <= 0:
        print("password cracking detected!!!")
        soc.sendall("login failed".encode())
        print("unsuccessful login (password cracking)")
        addFailedAttempt(username, password)
        login(soc, _username, _password, limitTries)

    if username == _username and password == _password:
        soc.sendall("login successful".encode())
        print("successful login")
        return 1
    else:
        soc.sendall("login failed".encode())
        print("unsuccessful login")
        addFailedAttempt(username, password)
        login(soc, _username, _password, limitTries-1)