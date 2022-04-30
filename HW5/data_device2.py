from socket import *
import random

BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 8000))
sock.listen()
conn, remotehost = sock.accept()

while True:
    print("WAITING...")
    data = conn.recv(BUFSIZE).decode()
    
    if data=="Request": 
        heartRate=random.randint(40,140)
        step=random.randint(2000,6000)
        calorie=random.randint(1000,4000)
        data = f"Heartbeat={heartRate}, Steps={step}, Cal={calorie}"
        conn.send(data.encode())
    elif data=="quit":
        sock.close()
        break
    else:
        print("Wrong")
        break