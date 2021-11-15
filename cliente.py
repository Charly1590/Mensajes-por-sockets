import socket
print ("inicio del programa")
# Crear socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Establecer ip y puerto
host = socket.gethostname()
port = 3333
# Conectarse al servidor
mySocket.connect((host, port))
print ("Conectarse al servidor")

while True:
    # Recibir mensaje
    print ("---------------------- Read:", end = "") # Salida sin salto de línea
    msg = mySocket.recv(1024)
    print(msg)
    print ("Lectura completada")
    if msg == b"EOF":
        break
    if msg == b"quit":
        mySocket.close()
        print ("Fin del programa \ n")
        exit()
 
         #   Enviar un mensaje 
    msg = input ("---------------------- enviar:")
    mySocket.send(msg.encode())
    print ("Enviar completado")
    if msg == "EOF":
        break
    if msg == "quit":
        mySocket.close()
        print ("Fin del programa \ n")
        exit()
print ("Fin del programa \ n")