# Name: Emily Yu
# Date: 7/18/22
# Description: Microservice that creates encrypted key similar to Caesar Cipher
#              Returns to client encoded key that can be used to encrypt messages
#
#               REQUIREMENT: To run microservice, connect via socket on host = 'localhost' and port=5000
#                                and send encoded 'Run' to receive return
#
# Code for socket modified from https://pythonprogramming.net/sockets-tutorial-python-3/


import string
import time
import random
import socket

def encrypt_key():
    """
    Generates a randomized encryption key with all lowercase and uppercase ASCII letters.
    Letters are not repeated
    """
    letters = string.ascii_letters
    key = ''.join(random.sample(letters, len(letters)))
    return key

# host and port settings
host = 'localhost'
port = 5000

# create a socket at client side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f'Connection from {address} has been established!')
    msg = clientsocket.recv(1024)
    if msg.decode() =='Run':
        clientsocket.send(encrypt_key().encode())
    clientsocket.close()

