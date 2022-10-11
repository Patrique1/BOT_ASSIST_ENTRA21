import os

lista_de_programas = ['chrome.exe', 'word.exe', 'excel.exe', 'calc.exe']

# Acessando todas as pastas no windows.
# sistema = os.environ


# Acessando a pasta atual com comando getcwd
# pasta = os.getcwd()
# print(pasta)

def list_files_dir():
    caminho = r'\\Server\python-matutino\patrique.pacheco\Desktop'
    os.chdir(caminho)
    print("""===============LISTANDO ARQUIVOS E DIRETORIOS NA PASTA ATUAL===============""")
    print("")
    for linha in os.listdir(caminho):
        print(linha)

    file_element = input("Diga o nome do arquivo: ")
    new_path = fr'\\Server\python-matutino\patrique.pacheco\Desktop\{file_element}'

    return new_path

def acessar_arquivo():
    new_path = list_files_dir()

    os.startfile(new_path)

def modificar_arquivo():
    new_path = list_files_dir()

    conteudo = input("Novo conteudo: ")
    with open(f"{new_path}", "a+") as file:
        file.writelines(f"{conteudo}\n")
        file.close()

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
    caminho = r'\\Server\python-matutino\patrique.pacheco\Desktop'
    os.chdir(caminho)

    new_file = input("Qual o nome desse novo arquivo: ")
    with open(f"{new_file}", "w") as file:
        file.close()


def criando_pasta():
    caminho = r'\\Server\python-matutino\patrique.pacheco\Desktop'
    os.chdir(caminho)

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






# Criando uma nova pasta dentro do caminho do windows
# os.mkdir("pastateste1")

#Listando as pastas dentro do caminho
# print(os.listdir())

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
        modificar_arquivo()
    elif op == "3":
        deletando_arquivo()
    elif op == "4":
        criando_arquivo()
    elif op == "5":
        criando_pasta()
    elif op == "6":
        executar_programa()
