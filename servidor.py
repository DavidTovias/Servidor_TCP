import socket

SERVIDOR = 'localhost'
PUERTO = 5000

mi_socket = socket.socket() # Genera un nuevo socket con los valores por default
mi_socket.bind( (SERVIDOR, PUERTO) ) # Se establece la conexión, Host y puerto 
mi_socket.listen(5) 

while True:
    conexion, direccion = mi_socket.accept() # El server va a estar aceptando peticiones
    print("Conexión establecida")
    
    while True:
        peticion = conexion.recv(1024).decode() # Se recibe mensaje del cliente
        print("Cliente envía: " + peticion)

        if peticion.upper() == 'DESCONEXION':
            conexion.close() # Cerrar la conexión
            print(f"Conexion cerrada: cliente: {direccion}")
            break
        else:
            conexion.send(peticion.upper().encode()) # Se envía al cliente el mensaje en Mayúsculas

    
    

