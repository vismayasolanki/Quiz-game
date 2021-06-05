from socket import *
import time
import threading
import random
import sys
import datetime
import select
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(3)
print("server is ready")
clients = []
bank = []
scores = [0,0,0]
answers = []
buzzers = [0,0,0]
i = 0
j = 0

Rules = ["This is a game.","Here questions will appear","you will have 10 seconds to think","If you know the answer press y","after pressing y you will have 10 secs to answer otherwise it will be considered as a wrong answer","for correct : +1 and for wrong : -0.5","Whoever reaches score 5 first wins","there are 50 questions","Good Luck"]

def send_all(message):
    for conn in clients:
        conn.send(message.encode("utf-8"))
    

def buzzer_not_pressed():
    for i in buzzers:
        if(i == 1):
            return False
    return True


def check():
    time.sleep(10)
    if message != None:
        return True
    return False



for i in range(50):
    q = str(i+1) + " + " +  str(i+1)
    a = str(2*i+2)
    t = (q,a)
    bank.append(t)
    random.shuffle(bank)


while(len(clients)<3):
    conn,addr = serverSocket.accept()
    clients.append(conn)
    print(str(addr) + " this user has joined")
 

    if(len(clients)<3):
        greeting = "welcome. waiting for others to join"
        conn.send(greeting.encode("utf-8"))
    else:
        greeting = "game about to start\n"
        conn.send(greeting.encode("utf-8"))
    print("")

for r in Rules:
    send_all(r) 
    send_all("\n")



while j<50:
    if(j>=49):
        send_all("Nodbody won")
        for c in range(len(clients)):
            clients[c].send(("Your score is " + str(scores[c])).encode("utf-8"))
        serverSocket.close()
    for i in range(len(scores)):
        if(scores[i]>=5):
            for c in clients:
                if(c == clients[i]):
                    c.send("You Won!!".encode("utf-8"))
                else:
                    c.send(("You lose. Your score is " + str(scores[clients.index(c)])).encode("utf-8"))
            serverSocket.close()
            sys.exit() 
   
    if(j<49):
        try:
            send_all(bank[j][0])
        except:
            continue
    else:
        for c in clients:
            c.close()
        exit()
    print("sending quetion " + str(j+1))

    r,w,e = select.select(clients,[],[],10)
    if(len(r)==0):
        j+=1

    if(len(r) != 0):
        conn = r[0]
    else:
        continue

    buzzer = None
    buzzer = (conn.recv(1)).decode("utf-8","strict")
    if buzzer:

        buzzers[clients.index(conn)] = 1
        print("player " + str(clients.index(conn) + 1)+ " pressed the buzzer")
        for c in clients:
            if(c==conn):
                c.send("type the answer".encode("utf-8"))
            else:
                c.send("some other player pressed buzzzer first. Please wait until next question".encode("utf-8"))

        a = time.time()
        ans = conn.recv(2048)
        if(ans.decode("utf-8","strict") == bank[j][1]):
            conn.send("correct".encode("utf-8"))
            scores[clients.index(conn)] += 1
        else:
            conn.send("Wrong".encode("utf-8"))
            scores[clients.index(conn)] -= 0.5
        buzzers[clients.index(conn)] = 0


    print(scores)
    buzzer = None
    j+=1