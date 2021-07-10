import selectors
import socket
import sys
# import sys
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
sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('Connection accepted for:', addr)
    conn.sendall(bytes(str("you are connected to network"),'utf8'))
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(4096)  # Should be ready
    if data:
        msg=str(data,'utf8')
        if msg=='none':
            print("connection closed:",conn)
            sel.unregister(conn)
            conn.close()
            return
        ans=calculate(msg)
        conn.sendall(bytes(str(ans), 'utf8'))
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()
HOST=str(sys.argv[1])
PORT=int(sys.argv[2])
sock = socket.socket()
sock.bind((HOST, PORT))
while True:
    sock.listen(100)
    sock.setblocking(False)
    sel.register(sock, selectors.EVENT_READ, accept)
    while True:
        events = sel.select()
        for key, mask in events:
            callback = key.data
            callback(key.fileobj, mask)