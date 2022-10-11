import json
import keyboard
from time import sleep
import webbrowser
import selenium
import Sites_WebScraping as SW
import teste_de_funcionalidades

global BROWSING_PERMISSION
global SCRAPING_PERMISSION

def validation(command):
    for i in command:
        if i in data:
            if i == "acessa" or i == "pesquisa" or i == "abra":
                BROWSING_PERMISSION = True
                SCRAPING_PERMISSION = False
            elif i == "logar":
                SCRAPING_PERMISSION = True
                BROWSING_PERMISSION = False
            for j in command:
                if j in data[i]:
                    for z in command:
                        if z in data[i][j]:
                            result = data[i][j][z]
                            SCRAPING_PERMISSION = False
                            BROWSING_PERMISSION = False
                    break
        break
    return result, SCRAPING_PERMISSION, BROWSING_PERMISSION


def inicialize():
    print('O que deseja fazer hoje?')
    x = input('>>> ').lower().split()
    value, SCRAPING_PERMISSION, BROWSING_PERMISSION = validation(x)
    if BROWSING_PERMISSION == True:
        SW.google_wiki_summary()
        BROWSING_PERMISSION = False
        return BROWSING_PERMISSION
    elif SCRAPING_PERMISSION == True:
        SW.entra21()
        SCRAPING_PERMISSION = False
        return SCRAPING_PERMISSION
    elif value == 'database' and SCRAPING_PERMISSION == False and BROWSING_PERMISSION == False:
        teste_de_funcionalidades.update_user_data()



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