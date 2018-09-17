#! /bin/python
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 4242
BUFFER_SIZE = 8196

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
data = "gfx"
for x in range(BUFFER_SIZE - len("gfx")):
    data += '#'
s.send(data)
while True:
    data = ""
    GET_FULL_DATA = False
    while not GET_FULL_DATA:
        data += s.recv(BUFFER_SIZE)
        GET_FULL_DATA = "@" in data
    p = data.replace("#", "")
    data_split = p.split("\n")
    NUM_COL = data_split[0].split(",")[0]
    NUM_ROW = data_split.pop(0).split(",")[1]
    map_data = data_split.pop(0).split(",")
	
    print ("col= " + str(NUM_COL) + "  row= " + str(NUM_ROW))
    print ("map data= " + str(map_data))
    print ("data_split= " + str(data_split))
