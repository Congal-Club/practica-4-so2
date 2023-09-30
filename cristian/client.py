from socket import socket, AF_INET, SOCK_STREAM
import datetime
import time

host = '192.168.0.106'
port = 3000

def convert_string_to_hour(string):
    hour = datetime.datetime.strptime(string, '%Y%m%d %H:%M:%f')
    return hour

def main():
    # Creamos el cliente de sockets y comenzamos a medir el tiempo
    client = socket(AF_INET, SOCK_STREAM)
    init = time.time()
    client.connect((host, port))

    # Recibimos la hora del servidor
    hour_string = client.recv(1024).decode()

    # Dejamos de medir el tiempo y sacamos el total
    end = time.time()
    total_time = end - init

    hour = convert_string_to_hour(hour_string)
    half_time = total_time / 2

    print(f'El tiempo total de la petición fue: {total_time} segundos')
    print(f'El tiempo de ida fue: {half_time} segundos')
    print(f'La hora recibida del servidor fue: {hour_string}')
    print('La hora exacta es:', hour + datetime.timedelta(seconds=half_time))

    client.close()

if __name__ == '__main__':
    main()
