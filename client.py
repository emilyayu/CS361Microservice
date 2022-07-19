# Name: Emily Yu
# Date: 7/18/22
# Description: Microservice that creates Caesar Cipher
#              Outputs .txt file with encrypted key to be used to encrypt messages
#
#               REQUIREMENT: to run microservice, need 'encrypt-key.txt' to display the word 'run'.
#               'Run' is not case-sensitve.

import socket

host = 'localhost'
port = 5000
# Code for socket modified from https://pythonprogramming.net/sockets-tutorial-python-3/

# create a socket at client side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

# connect it to server and port
# number on local computer.
s.connect((host, port))
s.send(b'Run')

# receive message string from
# server, at a time 1024 B
full_msg = ''

while True:
    msg = s.recv(1024)
    if len(msg) <= 0:
        break
    full_msg += msg.decode('utf-8')
print(full_msg)

# disconnect the client
s.close()
