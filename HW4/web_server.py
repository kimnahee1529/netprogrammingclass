# from socket import *
# s = socket()
# s.bind(('',80))
# s.listen(10)

# while True:
#     client, addr = s.accept()
#     data = client.recv(1024) 
#     msg = data.decode() 
#     req = msg.split('\r\n')

#     req_m = req[0].split()[1].strip('/')
    
#     print(req_m)

#     if req_m == "index.html": 
#         client.send(b'HTTP/1.1 200 OK\r\n')
#         client.send(b'Content-Type: text/html \r\n\r\n')
#         f = open("index.html",'r', encoding='utf-8')
#         data=f.read()
#         client.send(data.encode('euc-kr'))

#     elif req_m == "iot-1.png":
#         client.send(b'HTTP/1.1 200 OK\r\n')
#         client.send(b'Content-Type: image/png\r\n\r\n')
#         f = open('iot-1.png', 'rb')
#         data = f.read()
#         client.send(data)

#     elif req_m == "favicon.ico":
#         client.send(b'HTTP/1.1 200 OK\r\n')
#         client.send(b'Content-Type: image/x-icon\r\n\r\n')
#         f = open('favicon.ico', 'rb')
#         data = f.read()
#         client.send(data)
        
#     else : 
#         client.send(b'HTTP/1.1 404 Not Found\r\n\r\n')
#         client.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
#         client.send(b'<BODY>Not Found</BODY></HTML>')

    
#     client.close()


    #####

import mimetypes
from socket import *

s=socket()
s.bind(('', 80))
s.listen(10)

while True:
    filename=''
    print("start!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    c, addr=s.accept()

    data=c.recv(1024)
    msg=data.decode()
    req=msg.split('\r\n')

    print(req)
   
    a=req[0].find('/')
    
    for i in range(a, len(req[0])):
        if(req[0][i]==' '):
            break
        else:
            filename=filename+req[0][i]
            print(req[0][i], end='')

    
    filename=filename.strip('/')
    print("filename:", filename)
    if filename=="index.html":
        mimeType='text/html'
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: '+ mimeType.encode() + b'\r\n\r\n')
        f=open(filename, 'r', encoding='utf-8')
        data=f.read()
        c.send(data.encode('euc-kr'))
    elif filename=="iot-1.png":
        mimeType='image/png'
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: '+ mimeType.encode() + b'\r\n\r\n')
        f=open(filename, 'rb')
        data=f.read()
        c.send(data)
    elif filename=="favicon.ico":
        mimeType='image/x-icon'
        print(filename)
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: '+ mimeType.encode() + b'\r\n\r\n')
        f=open(filename, 'rb')
        data=f.read()
        c.send(data)
    else :
        print("else")
        c.send(b'HTTP/1.1 404 Not Found\r\n\r\n')
        c.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
        c.send(b'<BODY>NOT FOUND</BODY></HTML>')




    c.close()