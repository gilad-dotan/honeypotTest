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
        bruteForceLogin(soc, loginCombinations)
    else:
        loginGui(soc)

    # managing the file system
    while True:
        print(soc.recv(1024).decode())
        soc.sendall(input('').encode())


if __name__ == '__main__':
    client_program()