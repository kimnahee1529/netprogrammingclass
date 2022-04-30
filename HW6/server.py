import socket

port = 5555
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

mbox_index = {} 

while True:    
    msg, addr = sock.recvfrom(BUFFSIZE)

    if msg.decode() == "quit": 
        break

    command, mboxID, *message = msg.decode().split() 
    message = " ".join(message) 

    if command == 'send': 
        if mboxID not in mbox_index: 
            mbox_index[mboxID] = [] 
        
        mbox_index[mboxID].append(message)

        sock.sendto("OK".encode(), addr)
        
    elif command == 'receive': 
       
        if (mboxID not in mbox_index) or (not bool(mbox_index[mboxID])):
            sock.sendto("No messages".encode(), addr)
        else: 
            sock.sendto(mbox_index[mboxID].pop(0).encode(), addr)

sock.close()