# Encrypted Key Generator Microservice
Microservice Description: Microservice that creates encrypted key similar to Caesar Cipher
                          Returns to client encoded key that can be used to encrypt messages. 
                          Communication with microservice is via socket connection.


# Requesting Data
1. Connect to socket using host = 'localhost' and port = 5000
2. Send encoded 'Run' to the encryption_microservice server. 'Run' is case sensitive.
<br>
<br>Example Call: s.send ( b 'Run' )


# Receiving Data
1. Using socket receive data still using host = 'localhost' and port = 5000. 
      <br>msg = s.recv(1024) will be sufficient
      <br>where s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
2. Decode message and save for other use.


# UML sequence diagram
<img width="461" alt="image" src="https://user-images.githubusercontent.com/83041778/179866825-7d5b4235-6926-4db0-a1d6-5b88418e0eb0.png">
