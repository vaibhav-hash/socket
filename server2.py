def calculate(string):
    import re
    string = string #string
    pattern = '([*/+-])'
    result = re.split(pattern, string)
    input1=int(result[0])
    input2=int(result[2])
    ans=0
    if(result[1]=='-'):
        ans=input1-input2
    elif result[1]=='+':
        ans=input1+input2
    elif result[1]=='*':
        ans=input1*input2
    elif result[1]=='/':
        ans=input1/input2
    elif result[1]=='%':
        ans=input1%input2
    # print(ans)
    return ans
import socket, threading
import sys
class create_client(threading.Thread):
    def __init__(self,addr,conn):
        threading.Thread.__init__(self)
        self.csocket = conn
        print('connected to client having port number:',addr)
    def run(self):
        print ("Connection from : ", addr)
        self.csocket.sendall(b'connected to server')
        while True:
            data = self.csocket.recv(2048)
            data = str(data, 'utf8')
            if data=='none':
              break
            ans=calculate(str(data))
            self.csocket.sendall(bytes(str(ans),'utf8'))
        print ("disconnecting client:", addr," diconnected")
# HOST = "127.0.0.1"
# PORT = 5000
HOST=str(sys.argv[1])
PORT=int(sys.argv[2])
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
while True:
    server.listen(1)
    clientsock, addr = server.accept()
    newthread = create_client(addr, clientsock)
    newthread.start()