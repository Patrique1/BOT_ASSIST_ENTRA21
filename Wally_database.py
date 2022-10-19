import sqlite3
import requests as re
from time import sleep

conexao = sqlite3.connect('bdWally.db')
cursor = conexao.cursor()


# def createTable1():
#     cursor.execute('CREATE TABLE IF NOT EXISTS superuser ('
#                    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                    'Nome TEXT,'
#                    'Login TEXT,'
#                    'Senha TEXT,'
#                    'Email TEXT,'
#                    'Telefone TEXT,'
#                    'Cep TEXT,'
#                    'Bairro TEXT,'
#                    'Rua TEXT'
#                    ')')
#     conexao.commit()
#     cursor.close()
#     conexao.close()
#
# # createTable1()
#
#
# def createTable2():
#     cursor.execute('CREATE TABLE IF NOT EXISTS contatos('
#                    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                    'Nome TEXT,'
#                    'Email TEXT,'
#                    'Telefone TEXT'
#                    ')')
#     conexao.commit()
#     cursor.close()
#     conexao.close()

# createTable2()


# def insertTable1(nome, cpf, login, senha, email, telefone, cep):
#     cp = re.get(f'https://viacep.com.br/ws/{cep}/json/').json()
#
#     cursor.execute('INSERT INTO superuser (Nome, Cpf, Login, Senha, Email, Telefone, Cep, Estado, Cidade, Bairro, Rua) '
#                    'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
#                    (nome, cpf, login, senha, email, telefone, cep, cp['uf'], cp['localidade'], cp['bairro'], cp['logradouro']))
#     conexao.commit()
#     cursor.close()
#     conexao.close()


# nome = input('Nome: ').title()
# cpf = input('Cpf: ')
# login = input('Login: ')
# senha = input('Senha: ')
# email = input('Email: ')
# telefone = input('Telefone: ')
# cep = input('Cep: ')
#
# insertTable1(nome, cpf, login, senha, email, telefone, cep)


# nome = input('Nome: ').title()
# email = input('Email: ')
# telefone = input('Telefone: ')
#
# insertTable2(nome, email, telefone)




# def updateTable1(email, senha):
#     cursor.execute('SELECT * FROM superuser ')
#     for i in cursor.fetchall():
#         if email in i:
#             cursor.execute('UPDATE superuser SET Senha=? WHERE Email=?',
#                            (senha, email))
#             conexao.commit()
#             cursor.close()


# email = input('Email: ')
# senha = input('Digite sua nova senha: ')
#
# updateTable1(email, senha)


# def deleteTable1(cpf):
#     cursor.execute('SELECT * FROM superuser ')
#     for i in cursor.fetchall():
#         if cpf in i:
#             cursor.execute(f'DELETE FROM superuser WHERE Cpf={cpf}')
#             conexao.commit()
#             cursor.close()


# cpf = input('Para deletar a conta, preciso que digite o seu cpf \nCpf: ')
#
# deleteTable1(cpf)


# def selectTable1(cpf):
#     sql = cursor.execute(f'SELECT * FROM superuser WHERE Cpf={cpf}')
#     print(sql.fetchone())
#
#     conexao.commit()
#     cursor.close()


# telefone = input('Telefone: ')
# selectTable1(telefone)


def insertTable2(nome, email, telefone):
    cursor.execute('INSERT INTO contatos (nome, email, telefone) VALUES (?,?,?)',
                   (nome, email, telefone))
    conexao.commit()


def updateTable2(x, y, z):
    cursor.execute('SELECT * FROM contatos')
    for i in cursor.fetchall():
        if x in i:
            cursor.execute(f'UPDATE contatos SET {y}=? WHERE Nome=?',
                           (z, x))
            conexao.commit()


def deleteTable2(command):
    cursor.execute('SELECT * FROM contatos ')
    for i in cursor.fetchall():
        if command in i:
            cursor.execute(f'DELETE FROM contatos WHERE Nome=?', [command])
            conexao.commit()


def selectTable2(x):
    sql = cursor.execute(f'SELECT Nome, Email, Telefone FROM contatos WHERE Nome=?', [x])
    count = 1
    for info in sql.fetchone():
        if count == 1:
            print(f'Contato: {info}')
            count += 1
        elif count == 2:
            print(f'Email: {info}')
            count += 1
        elif count == 3:
            print(f'Telefone: {info}')
            break


    conexao.commit()


def main():
    print("Acessando sua agenda...")
    sleep(3)
    print()
    database = cursor.execute('SELECT Nome FROM contatos ')
    qnt = 0
    for i in database.fetchall():
        for j in i:
            print(f"Nome: {j}")
            qnt += 1
    print(f"Contatos totais: {qnt}")
    while True:
        print("\n", "="*55, "\n")
        user = input("""O que você deseja fazer?
        [1] - Inserir um novo contato na sua agenda.
        [2] - Alterar informação de algum contato.
        [3] - Excluir algum contato.
        [4] - Visualizar informações de algum contato.
        [5] - Sair
        >>> """)
        print()

        if user == '1':
            nome = input('Nome: ').title()
            email = input('Email: ')
            telefone = input('Telefone: ')

            insertTable2(nome, email, telefone)

        elif user == '2':
            nome = input('Diga o nome do contato que você deseja alterar alguma informação: ').title()

            opcaoUser = input("""Qual informação você deseja alterar?
                              [1] - Nome
                              [2] - Email
                              [3] - Telefone
                              >>> """).title()

            novaInfo = input('Nova informação: ').title()

            updateTable2(nome, opcaoUser, novaInfo)

        elif user == '3':
            nome = input('Diga o nome do contato que você deseja deletar  \nNome: ').title()
            deleteTable2(nome)

        elif user == '4':
            opcaoUser = input('Diga o número de telefone do contato que você deseja receber as informaões ').title()

            selectTable2(opcaoUser)

        elif user == '5':
            break


