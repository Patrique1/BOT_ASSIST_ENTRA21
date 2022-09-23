import json
import keyboard
from time import sleep
import webbrowser

def validation(command):
    for i in command:
        if i in data:
            for j in command:
                if j in data[i]:
                    for z in command:
                        if z in data[i][j]:
                            result = data[i][j][z]
                    break
        break
    return result


def navegador(command):
    x = command
    webbrowser.open_new_tab(x)




def inicialize():
    print('O que deseja fazer hoje?')
    x = input('>>> ').lower().split()
    value = validation(x)
    for i in x:
        if i == "site" or i == "pesquise":
            return navegador(value)



# Main seria a função principal para iniciar o assistente
if __name__ == '__main__':
    print('Olá, sou seu assistente virtual.')
    with open('command.json') as file:
        data = json.load(file)
        file.close()
    while True: # Esses laço garante o funcionamento do programa sempre que as teclas chaves foram pressionadas.
        if keyboard.is_pressed('ctrl+alt+m'):
            sleep(0.05)
            inicialize()
            sleep(0.05)