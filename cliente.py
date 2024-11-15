import socket

SERVIDOR = 'localhost'
PUERTO = 5000

mi_socket = socket.socket()
mi_socket.connect( (SERVIDOR, PUERTO) )

while True:
    mensaje = input("Ingrese el mensaje para enviarlo al servidor: ")
    mi_socket.send(mensaje.encode('utf-8')) # Se envía información al servidor

    if mensaje.upper() == "DESCONEXION":
        mi_socket.close() # Se cierra conexión
        print("Se desconectó del servidor ...")
        break
    else:
        respuesta = mi_socket.recv(1024).decode() # Respuesta del servidor (mensaje enviado previamente por el cliente en Mayúsculas)
        print("Servidor responde: " + respuesta)

