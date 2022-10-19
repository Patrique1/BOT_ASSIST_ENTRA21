import json
import keyboard
from time import sleep
import webbrowser
import selenium
import Wally_Google
import Wally_Tube
import files_system as fs
import Wally_database as wdb

Sys = None


def inicialize():
    print('Wally - O que deseja fazer hoje?')
    print('''OPÇÕES
    [1] PESQUISAR ALGO
    [2] ASSISTIR ALGO
    [3] MODO SISTEMA
    [4] AGENDA
    [0] SAIR ''')

    op = input('>>> ').lower()

    if op == '1':
        Wally_Google.search_google()
    elif op == '2':
        Wally_Tube.search_youtube()
    elif op == '3':
        fs.main()
    elif op == '4':
        wdb.main()
    elif op == '5':
        pass
    elif op == '0' or op == 'sair' or op == 'pode fechar':
        result = False
        return result


# Main seria a função principal para iniciar o assistente
if __name__ == '__main__':
    print('Olá, sou seu assistente virtual.')
    with open('command.json') as file:
        data = json.load(file)
        file.close()
    while True: # Esses laço garante o funcionamento do programa sempre que as teclas chaves foram pressionadas.
     if keyboard.is_pressed('ctrl+alt+m'):
        sleep(0.05)
        Sys = inicialize()
        sleep(0.05)
        if Sys == False:
            break
     elif keyboard.is_pressed('ctrl+alt+g'):
         exit()