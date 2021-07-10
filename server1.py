import socket
import sys
import time
# HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
# PORT = 5000        # Port to listen on (non-privileged ports are > 1023)
HOST=str(sys.argv[1])
PORT=int(sys.argv[2])
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
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    while True:
        try:
            s.listen(1)
            conn,addr=s.accept()
            s.setblocking(True)
            print('connected to the client socket number',addr)
            conn.sendall(bytes("connected to the server", 'utf8'))
            prev_conn=conn
            while True:
                try:
                    data=conn.recv(1024)
                    data = str(data, 'utf8')
                    ans=calculate(str(data))
                    conn.sendall(bytes(str(ans), 'utf8'))
            # time.sleep(10) # as to show to the user that server is busy and has refused
                except:
                    # print("ctrl-c to quit")
                    conn.close()
                    break
        except:
            break