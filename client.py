from socket import *
import time
import select
import threading
import sys
serverName = "192.168.56.1"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
if(len(sys.argv) != 2):
    print("please follow the order : python client.py <IP ADDRESS>")
    exit()
serverName = str(sys.argv[1])
clientSocket.connect((serverName,serverPort))
v = 1
mess = None
flag2 = False
    
def check():
    time.sleep(0.1)
    a = time.time()
    while(time.time() - a <= 10):
        if(mess != None):
            return
    clientSocket.send("-1".encode("utf-8"))
    print("You exceeded the time limit")


        
flag = False
while True:
    sockets_list = [sys.stdin, clientSocket]
    r,w,e = select.select(sockets_list,[],[])
    mess = None
    flag2 = False
    for s in r:
        if s == clientSocket:
            message = (s.recv(2048)).decode("utf-8","strict")
            if(message != ""):
                print (message)
            else:
                clientSocket.close()
                exit()
            if(message == "correct" or message == "Wrong"):
                flag2 = True
        else:
            mess = None
            mess = input()
            if(mess == "y"):
                flag = True
            else:
                flag = False
            if(flag):
                threading._start_new_thread(check,())
            clientSocket.send(mess.encode("utf-8"))
            mess = None
            sys.stdout.flush()
clientSocket.close()
sys.exit()