import socket
import time

BUFSIZE = 1024

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
add1 = ("localhost", 7000)
s1.connect(add1)

s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
add2 = ("localhost", 8000)
s2.connect(add2)

f = open("data.txt", 'a+')

while True:
    msg = input("Message to send: ")
    
    if msg=="quit":
        s1.send("quit".encode())
        s2.send("quit".encode())
        break
    elif msg=="1":
        s1.send("Request".encode())
        data = s1.recv(1024).decode()
        f.write(f"{time.strftime('%c', time.localtime(time.time()))}: {data}\n")
    elif msg=="2":
        s2.send("Request".encode())
        data = s2.recv(1024).decode()
        f.write(f"{time.strftime('%c', time.localtime(time.time()))}: {data}\n")
    else:
        print("Wrong")
        break
s1.close()
s2.close()
f.close()