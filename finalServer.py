import socket
import time

host = '127.0.0.1'
port = 5000
clients1 = {}
clients2 = {}
exception = False

private_clients = {}

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))


#s.setblocking(0)

quitting = False
n = 0
print "Server Started."

while not quitting:
    print "waiting to receive"
    data, addr = s.recvfrom(1024)
    print "received"
    if not data:
        break
    if "Quit" in str(data):
        quitting = True
      
        
    
    if data[:6] == "lOgiNu":
        user = data[6:12]
        friend = data[12:]
        print user
        
        
        #clients[user] = addr
        n = 0
        
        while True:
            key = user + str(n)
            if key in clients2:
                n = n + 1
            else:
                break

                
        nS = str(n)
        u = user + nS
        clients1[addr] = u
        clients2[u] = addr
            
                
        print clients1
        print clients2
        if friend != "":
            n = 0
            while True:
                key = friend + str(n)
                if key in private_clients:
                    n = n + 1
                else:
                    break
            nS = str(n)
            f = friend + nS
            private_clients[u] = f
            private_clients[f] = u
            print private_clients           
            
            
            ###if friend not in private_clients:
            #private_clients[user] = friend
            #private_clients[friend] = user
                #s.sendto("wow",addr)
            #else:
             #   exception = True
              #  s.sendto("Failed",addr)
             #print private_clients
    else:
        #if exception == False:
        message = data
        print time.ctime(time.time()) + str(addr) + ": :" + str(data)
        addr1 = addr
        uid  = clients1[addr]
        fid = private_clients[uid]
        addr2 = clients2[fid]
        #fid = message[:6]
        #print fid
        print "here1"
        #uid = message[:6]
        #print uid
        print "here2"
        #addr1 = clients[uid]
        #fid = private_clients[uid]
        #addr2 = ""
        #try:
         #    addr2 = clients[fid]
                #s.sendto("Success",addr1)
        #except:
             #exception = True
          #   s.sendto("Error-401",addr1)
        if exception == False:
        #if addr2 in clients:
            print "here3"
            #s.sendto(message[6:],addr1)
            print message,addr1,'message and addr1'
            s.sendto(message[6:],addr2)
            print message,addr2,'message and addr2'
        
       
s.close()
    
