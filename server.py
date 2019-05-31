import socket
from os import system

ip = '0.0.0.0' #pega o endereço ip da maquina que está rodando
port = 678 #numero de uma porta maior aleatoria
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #o server será do tipo tcp/ip

try:
    server.bind((ip,port))
    server.listen(5)

    print("Listening on %s %s" %(ip,port))

    obj, client = server.accept() #aguarda uma conexão no servidor local
    print ("Connection received from %s" %(client[0]))   #para retornar so o primeiro parametro
    while True:     #para sempre ficar aguardando um parametro passado e não fechar conexao apos a mensagem
        msg = obj.recv(1024)   #1024 num de bits (recebe uma mensagem)
        msg = msg[:-1]
        print(msg)
        #implementando funcoes do server
        if msg == bytes('ls','utf-8'):
            print (system(msg))
        else:
            print ("Invalid command")

    server.close()
except Exception as erro:
    print (erro)    #caso a porta ja esteja sendo usada
    server.close()
