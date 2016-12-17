import socket
#UDP client, conectionless tool

target_host="127.0.0.1"
target_port= 80


#Create a socket object
client= socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #IPv4 address / udp client


#send some data
client.sendto("AAABBBCCC",(target_host,target_port))

#receive some data
data, addr=client.recvfrom(4096)

print data





