from socket import socket, AF_INET, SOCK_STREAM
from datetime import *

host = 'localhost'
port = 3000

def main():
    # Creamos un servidor con sockets
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    while True:
        # Establecemos la conexión
        connection, address = server.accept()

        print(f'Conexión establecida con el cliente: {address}')

        # Obtenemos la hora actual después de la petición
        hour = datetime.now()
        hour_string = hour.strftime('%Y%m%d %H:%M:%f')

        print(f'Enviando hora actual al cliente: {address}')
        print(hour)

        # Enviamos la hora actual al cliente
        connection.send(hour_string.encode())
        connection.close()

if __name__ == '__main__':
    main()
