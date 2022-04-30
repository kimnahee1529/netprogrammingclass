from dis import Instruction
import socket

port = 5555
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    msg = input("Enter a message:(\"send mboxId message\") or (\"receive mboxId\") : ")
    if msg == 'quit':
        sock.sendto(msg.encode(), ('localhost', port))    
        break
    else: 
        sock.sendto(msg.encode(), ('localhost', port)) 

        msg, addr = sock.recvfrom(BUFFSIZE) 
        print(msg.decode())

sock.close()