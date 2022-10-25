import sqlite3
import Wally_database as WDT
import smtplib
import email.message


conexao = sqlite3.connect('bdWally.db')
cursor = conexao.cursor()


def select_Email(x):
    sql = cursor.execute("SELECT Email FROM contatos WHERE Nome=?", [x])
    for i in sql.fetchone():
        return i
    conexao.commit()


def enviar_email():
    nome = input('Nome do contato que você deseja enviar um e-mail: ').title()
    corpo_email = input('Mensagem: ')

    msg = email.message.Message()
    msg['Subject'] = "Email Automático"
    msg['From'] = "gabrieldsh2009@gmail.com"
    msg['To'] = select_Email(nome)
    password = "hruhrejjyyysnkrj"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


