import sqlite3
import requests as re
from time import sleep

conexao = sqlite3.connect('bdWally.db')
cursor = conexao.cursor()


def createTable1():
    cursor.execute('CREATE TABLE IF NOT EXISTS superuser ('
                   'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                   'Nome TEXT,'
                   'Login TEXT,'
                   'Senha TEXT,'
                   'Email TEXT,'
                   'Telefone TEXT,'
                   'Cep TEXT,'
                   'Bairro TEXT,'
                   'Rua TEXT'
                   ')')
    conexao.commit()
    cursor.close()
    conexao.close()

# createTable1()


def createTable2():
    cursor.execute('CREATE TABLE IF NOT EXISTS contatos('
                   'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                   'Nome TEXT,'
                   'Email TEXT,'
                   'Telefone TEXT'
                   ')')
    conexao.commit()
    cursor.close()
    conexao.close()

# createTable2()


def insertTable1(nome, cpf, login, senha, email, telefone, cep):
    cp = re.get(f'https://viacep.com.br/ws/{cep}/json/').json()

    cursor.execute('INSERT INTO superuser (Nome, Cpf, Login, Senha, Email, Telefone, Cep, Estado, Cidade, Bairro, Rua) '
                   'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                   (nome, cpf, login, senha, email, telefone, cep, cp['uf'], cp['localidade'], cp['bairro'], cp['logradouro']))
    conexao.commit()
    cursor.close()
    conexao.close()


# nome = input('Nome: ').title()
# cpf = input('Cpf: ')
# login = input('Login: ')
# senha = input('Senha: ')
# email = input('Email: ')
# telefone = input('Telefone: ')
# cep = input('Cep: ')
#
# insertTable1(nome, cpf, login, senha, email, telefone, cep)


def insertTable2(nome, email, telefone):
    cursor.execute('INSERT INTO contatos (nome, email, telefone) VALUES (?,?,?)',
                   (nome, email, telefone))
    conexao.commit()
    cursor.close()
    conexao.close()


# nome = input('Nome: ').title()
# email = input('Email: ')
# telefone = input('Telefone: ')
#
# insertTable2(nome, email, telefone)




def updateTable1(email, senha):
    cursor.execute('SELECT * FROM superuser ')
    for i in cursor.fetchall():
        if email in i:
            cursor.execute('UPDATE superuser SET Senha=? WHERE Email=?',
                           (senha, email))
            conexao.commit()
            cursor.close()


# email = input('Email: ')
# senha = input('Digite sua nova senha: ')
#
# updateTable1(email, senha)

# cursor.execute('SELECT * FROM superuser ')
# for i in cursor.fetchall():
#     print(i)


def updateTable2(x, y, z):
    cursor.execute('SELECT * FROM contatos')
    for i in cursor.fetchall():
        if y in i:
            cursor.execute(f'UPDATE contatos SET {y}=? WHERE Nome=?',
                           (z, x))
            conexao.commit()
            cursor.close()


# nome = input('Diga o nome do contato que você deseja alterar alguma informação: ').title()
#
# opcaoUser = input("""Qual informação você deseja alterar?
#                   [1] - Nome
#                   [2] - Email
#                   [3] - Telefone
#                   >>> """).title()
#
# novaInfo = input('Nova informação: ').title()
#
# updateTable2(nome, opcaoUser, novaInfo)


def deleteTable1(cpf):
    cursor.execute('SELECT * FROM superuser ')
    for i in cursor.fetchall():
        if cpf in i:
            cursor.execute(f'DELETE FROM superuser WHERE Cpf={cpf}')
            conexao.commit()
            cursor.close()


# cpf = input('Para deletar a conta, preciso que digite o seu cpf \nCpf: ')
#
# deleteTable1(cpf)


def deleteTable2(telefone):
    cursor.execute('SELECT * FROM contatos ')
    for i in cursor.fetchall():
        if telefone in i:
            cursor.execute(f'DELETE FROM contatos WHERE Telefone={telefone}')
            conexao.commit()
            cursor.close()


# cpf = input('Para deletar a conta, preciso que digite o seu CPF \nCpf: ')
# deleteTable2(cpf)


def selectTable1(cpf):
    sql = cursor.execute(f'SELECT * FROM superuser WHERE Cpf={cpf}')
    print(sql.fetchone())

    conexao.commit()
    cursor.close()


# telefone = input('Telefone: ')
# selectTable1(telefone)


def selectTable2(telefone):
    sql = cursor.execute(f'SELECT * FROM contatos WHERE Telefone={telefone}')
    print(sql.fetchone())

    conexao.commit()
    cursor.close()


# telefone = input('Telefone: ')
#
# selectTable2(telefone)

def main():
    while True:
        print("Acessando sua agenda...")
        sleep(3)
        print("\n", "="*30, "\n")
        user = input("""O que você deseja fazer?
        [1] - Inserir um novo contato na sua agenda.
        [2] - Alterar informação de algum contato.
        [3] - Excluir algum contato.
        """)

        if user == '1':
            nome = input('Nome: ').title()
            email = input('Email: ')
            telefone = input('Telefone: ')

            insertTable2(nome, email, telefone)

        elif user == '2':
            pass

main()

