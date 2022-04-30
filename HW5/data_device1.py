from socket import *
import random

BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 7000))
sock.listen()
conn, remotehost = sock.accept()

while True:
    print("WAITING...")
    data = conn.recv(BUFSIZE).decode()
    
    if data=="Request": 
        temperature=random.randint(0,40)
        humidity=random.randint(0,100)
        illumination=random.randint(70,150)
        data = f"Temp={temperature}, Humid={humidity}, lilum={illumination}"
        conn.send(data.encode())
    elif data=="quit":
        sock.close()
        break
    else:
        print("Wrong")
        break
