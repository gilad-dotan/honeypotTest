import socket
from login import *
from variables import *

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 7000  # socket server port number

    soc = socket.socket()  # instantiate
    soc.connect((host, port))  # connect to the server

    # login in
    if bruteForceLoginCombination:
        if not bruteForceLogin(soc, loginCombinations):
            return 1
    else:
        loginGui(soc)

    # managing the file system
    while True:
        print(soc.recv(1024).decode())
        soc.sendall(input('').encode())
        print(soc.recv(1024).decode())


if __name__ == '__main__':
    client_program()