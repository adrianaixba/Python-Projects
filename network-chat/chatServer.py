# for networking
import socket
import time

host = '127.0.0.1'
port = 5000

# to have multiple clients
clients = []

# creating a new socket using UDP with socker.SOCK_DGRAM
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# puts the socket and host/ports together
s.bind((host, port))

# it will not block when receiving something
s.setblocking(0)

quitting = False

print('Server started...')

while not quitting:
    try:
        data, addr = s.recvfrom(1024)
        # if a user types q, it will quit the server
        if 'q' in str(data):
            quitting = True
        if addr not in clients:
            clients.append(addr)
        print(time.ctime(time.time()) + str(addr) + ': :' + str(data))
        for client in clients:
            # it will go through the clients and send them a message
            s.sendto(data, client)
    except:
        pass
# close the socket
s.close()



