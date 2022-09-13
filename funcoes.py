import unidecode
from time import sleep
import os
import json
from selenium import webdriver

def tratamento_texto(user_text):
    text = user_text
    text_tratado = unidecode.unidecode(text).lower().replace(',','')
    return text_tratado


def acessando_sites(user_text):
    text = tratamento_texto(user_text)
    texto = text.split()
    with open("comando.json") as file:
        data = json.load(file)
    for i in texto:
        if i in data:
            driver = webdriver.Edge()
            url = f"{data[i]}"
            driver.get(url)


def acessar_caminho_do_sistema(user_text):
    text = tratamento_texto(user_text)
    caminho = text.split()
    with open(r"C:\Users\greyce.fumagali\PycharmProjects\pythonProject\BOT\conversa\funcoes\comando.json") as file:
        data = json.load(file)
    for i in caminho:
        if i in data:
            os.chdir(data[i])


def main():
    print("""
    1 - Acessar caminho no computador.
    2 - Criar uma nova pasta.
    3 - Abrir um site.
    4 - Fechar Assistente.
    """)
    while True:
        texto = input('Humano: ')
        if texto == "4":
            exit()
        elif texto == "3":
            user_text = input("Qual site deseja acessar? ")
            acessando_sites(user_text)
        elif texto == "2":
            pass
        elif texto == "1":
            user_text = input("Qual caminho no sistema deseja acessar? ")
            acessar_caminho_do_sistema(user_text)
        else:
            print("Comando desconhecido...")
            main()