from threading import Lock
from time import sleep
import threading
import random

locker = Lock()

def critic_section(number, array):
    print()
    print('Pidiendo acceso a la sección critica')
    
    while locker:
        print(f'Proceso')
