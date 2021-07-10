#!/usr/bin/env python3

import socket
import time
import sys
# HOST = '127.0.0.1'  # The server's hostname or IP address
# PORT = 8080        # The port used by the server
HOST=str(sys.argv[1])
PORT=int(sys.argv[2])
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # while True:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    print(str(data))
    while True:
        try:
            input_string=input("Enter a message to the server: ")
            s.sendall(bytes(str(input_string), 'utf8'))
            if(input_string=='none'):
                print('closing connection as you entered :none')
                break
            data = s.recv(1024)
            ans = str(data, 'utf8')
            print('Server Replied: ', ans)
        except:
            # print("ctrl-c to quit")
            break