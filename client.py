# Name: Emily Yu
# Date: 7/18/22
# Description: Microservice that creates encrypted key similar to Caesar Cipher
#              Returns to client encoded key that can be used to encrypt messages
#
#               REQUIREMENT: To run microservice, connect via socket on host = 'localhost' and port=5000
#                                and send encoded 'Run' to receive return
#
# Code for socket modified from https://pythonprogramming.net/sockets-tutorial-python-3/
#
#               *** EXAMPLE CALL BELOW ***


import socket

host = 'localhost'
port = 5000


# create a socket at client side using TCP / IP protocol
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

s.connect((host, port))
s.send(b'Run')

full_msg = ''

while True:
    # Receives encryption key
    msg = s.recv(1024)
    if len(msg) <= 0:
        break
    full_msg += msg.decode('utf-8')

#prints encryption key
print(full_msg)

# disconnect the client
s.close()
