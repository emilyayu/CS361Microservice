# CS361Microservice
Microservice Description: Microservice that creates encrypted key similar to Caesar Cipher
                          Returns to client encoded key that can be used to encrypt messages. 
                          Communication with microservice is via socket connection.


# Requesting Data
1. Connect to socket using host = 'localhost' and port = 5000
2. Send encoded 'Run' to the encryption_microservice server. 'Run' is case sensitive.


# Receiving Data
1. Using socket receive data still using host = 'localhost' and port = 5000. 
      msg = s.recv(1024) will be sufficient
      where s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
2. Decode message and save for other use.


# UML sequence diagram
<img width="449" alt="image" src="https://user-images.githubusercontent.com/83041778/179863670-f22d8efe-ab36-43f5-a7c9-31fd308574c9.png">
