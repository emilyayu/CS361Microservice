# Name: Emily Yu
# Date: 7/18/22
# Description: Microservice that creates Caesar Cipher
#              Outputs .txt file with encrypted key to be used to encrypt messages
#
#               REQUIREMENT: to run microservice, need 'encrypt-key.txt' to display the word 'run'.
#               'Run' is not case-sensitve.
import string
import time
import random
import socket

def encrypt_key():
    letters = string.ascii_letters
    key = ''.join(random.sample(letters, len(letters)))
    return key


host = 'localhost'
port = 5000
# Code for socket modified from XXXXXXX

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

