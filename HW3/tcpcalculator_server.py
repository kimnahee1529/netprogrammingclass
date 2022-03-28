from socket import *
BUFSIZE = 1024
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 9999))
sock.listen(1)
conn, (remotehost, remoteport) = sock.accept()
print('connected by', remotehost, remoteport)
while True:
    data = conn.recv(BUFSIZE)
    list=[]
    list=data.split()
    
    n1=int(list[0].decode())
    n2=int(list[2].decode())
    n=(list[1]).decode()

    if n=='+':
        conn.send(str(n1+n2).encode())
    elif n=='-':
        conn.send(str(n1-n2).encode())
    elif n=='x':
       conn.send(str(n1*n2).encode())
    elif n=='/':
        conn.send(str(n1/n2).encode())

    print("Received message: ", data.decode()) #식 다시 출력

conn.close()
sock.close()