import socket
import sys
from login import *
from variables import *

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

login(conn, Username, Password, NumOfLoginTries)