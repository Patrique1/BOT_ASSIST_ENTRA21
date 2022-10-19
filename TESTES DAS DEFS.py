

def tratamento_texto(comando):
    comando_tratado = comando.upper()
    texto(comando_tratado)

def texto():
    comando = tratamento_texto()
    if comando == 'PODE FECHAR':
        sys = False
        return sys

    for i in range(5):
        print(comando)


def main():
    while True:
        print("Testando funcionalidades...")

        user = input("Digite algo aqui: ")

        op = texto()


        if op == False:
            print("deu certo")
            break
        elif op == True:
            exit()

main()


