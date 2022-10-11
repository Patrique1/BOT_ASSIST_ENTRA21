import sqlite3

class User():
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone





def update_user_data():
    nome = input('Nome: ')
    email = input('Email: ')
    telefone = input('Telefone: ')

    conn = sqlite3.connect('Agenda.db')
    cursor = conn.cursor()

    cursor.execute(f"""INSERT INTO Contatos (nome, email, telefone)
    VALUES ('{nome}', '{email}', '{telefone}')""")

    # gravando no bd
    conn.commit()

    print('Dados inseridos com sucesso.')

    conn.close()

def delete_user_data():
    pass

def charge_user_data():
    pass

def check_user_info():
    pass




