import socket
print ("Inicio del programa")
 # Crear socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 # Establecer IP y puerto
host = socket.gethostname()
port = 3333
 # bind vincula el puerto
mySocket.bind((host, port))
 # Monitor
mySocket.listen(1024)
 
while True:
         # Recibir conexión del cliente
    print ("Esperando conexión ...")
    client, address = mySocket.accept()
    print ("Nueva conexión")
    print("IP is %s" % address[0])
    print("port is %d\n" % address[1])
 
    while True:
                 #   Enviar un mensaje 
        msg = input ("---------------------- enviar:")
        client.send(msg.encode())
        print ("Enviar completado")
        if msg == "EOF":
            break
        if msg == "quit":
            client.close()
            mySocket.close()
            print ("Fin del programa \ n")
            exit()
                 # Leer el mensaje
        msg = client.recv(1024)
        print ("---------------------- Leer:", msg)
        print ("Lectura completada")
        if msg == b"EOF":
            break
        if msg == b"quit":
            client.close()
            mySocket.close()
            print ("Fin del programa \ n")
            exit()
 
 