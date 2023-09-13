import socket
import sys
from login import *
from variables import *

def init_server():
    HOST = ''
    PORT = 7000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('# Socket created')

    # Create socket on port
    try:
        s.bind((HOST, PORT))
    except socket.error as msg:
        print('# Bind failed. ')
        sys.exit()

    print('# Socket bind complete')

    # Start listening on socket
    s.listen(10)
    print('# Socket now listening')

    # Wait for client
    conn, addr = s.accept()
    print('# Connected to ' + addr[0] + ':' + str(addr[1]))

    # going to the login
    login(conn, Username, Password, NumOfLoginTries)

    # going to the "system"

if __name__ == "__main__":
    init_server()


