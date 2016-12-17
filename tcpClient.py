import socket

#target_host="www.google.com"
target_host="0.0.0.0"
#target_port= 80
target_port= 9999

#Create a socket object
client= socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4 address / TCP client

#connect the client to server
client.connect((target_host,target_port))

#send some data
#client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
client.send("ABCDEFG")

#receive some data
response=client.recv(4096)

print response


