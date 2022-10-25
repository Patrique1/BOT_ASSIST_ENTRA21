import os

import keyboard

lista_de_programas = ['chrome.exe', 'word.exe', 'excel.exe', 'calc.exe']

# Acessando todas as pastas no windows.
# sistema = os.environ


# Acessando a pasta atual com comando getcwd
# pasta = os.getcwd()
# print(pasta)

def list_files_dir():

    print("""===============LISTANDO ARQUIVOS E DIRETORIOS NA PASTA ATUAL===============""")
    print("")
    for linha in os.listdir():
        print(linha)
    try:
        file_element = input("Diga o nome do arquivo: ")
    except FileNotFoundError:
        print("Esse arquivo não existe aqui...")

    return file_element

def acessar_arquivo():
    try:
        new_path = list_files_dir()
        os.startfile(new_path)
    except FileNotFoundError:
        print("Esse arquivo não existe aqui...")
def renomear_arquivo():
    new_path = list_files_dir()
    new_file_name = input("Diga o nome do novo arquivo: ")
    os.rename(f'{new_path}', f'{new_file_name}')

def deletando_arquivo():
    new_path = list_files_dir()
    if os.path.exists(f"{new_path}"):
        try:
            os.rmdir(new_path)
        except OSError:
            print('Não pode deletar uma pasta com arquivos dentro...')
    elif os.path.exists(f"{new_path}"):
        os.remove(f"{new_path}")
    else:
        print("The file does not exist")


def criando_arquivo():

    new_file = input("Qual o nome desse novo arquivo: ")
    with open(f"{new_file}", "w") as file:
        file.close()


def criando_pasta():

    new_dir = input("Qual o nome dessa nova pasta: ")
    if os.path.exists(new_dir):
        print("Existe uma pasta com esse nome...")
        return criando_pasta()
    else:
        os.mkdir(new_dir)

def executar_programa():
    program = input("Qual programar quer executar: ")
    for i in lista_de_programas:
        if program in i:
            os.startfile(i)

def menu_sys():
    caminho = input("""Qual caminho dentro do sistema você quer ter acesso: 
        [1] Documentos
        [2] Downloads
        [3] Área de trabalho
        [4] SAIR
        >>> """)
    try:
        if caminho == '1':
            path_sys = r'C:\Users\gabri\Documents'
            os.chdir(path_sys)
        elif caminho == '2':
            path_sys = r'C:\Users\gabri\Downloads'
            os.chdir(path_sys)
        elif caminho == '3':
            path_sys = r'C:\Users\gabri\Desktop'
            os.chdir(path_sys)
        elif caminho == '4' or keyboard.is_pressed('ctrl+alt+g'):
            exit()
    except Exception:
        print("Comando inválido, tente usar uma das opções disponíveis!")




def main():
    menu_sys()
    while True:
        op = input("""O que deseja fazer?
        [1] Executar um arquivo
        [2] Modificar um arquivo
        [3] Deletar um arquivo
        [4] Criar um novo arquivo
        [5] Criar uma nova pasta
        [6] Executar um programa
        [7] Sair
        >>> """)

        if op == "7":
            break
        elif op == "1":
            acessar_arquivo()
        elif op == "2":
            renomear_arquivo()
        elif op == "3":
            deletando_arquivo()
        elif op == "4":
            criando_arquivo()
        elif op == "5":
            criando_pasta()
        elif op == "6":
            executar_programa()
        menu = input("""Deseja retornar e modificar o caminho do sistema?
        [1] Permanecer e continuar
        [2] Retornar e modificar caminho
        [3] SAIR
        >>> """)
        if menu == '1':
            pass
        elif menu == '2':
            menu_sys()
        elif menu == '3' or keyboard.is_pressed('ctrl+alt+g'):
            break