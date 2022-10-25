import pywhatkit as kit
import pyautogui as pi
import datetime
import sqlite3

conexao = sqlite3.connect('bdWally.db')
cursor = conexao.cursor()


def select_Num(x):
    sql = cursor.execute("SELECT Telefone FROM contatos WHERE Nome=?", [x])
    for i in sql.fetchone():
        return i
    conexao.commit()


def mensagem():
    cntt = input('Digite o nome do contato que você deseja enviar uma mensagem: ').title()

    msg = input('Mensagem que deseja enviar: ')

    time = datetime.datetime.now()

    time_hora = int(time.strftime("%H"))
    time_min = int(time.strftime("%M"))

    kit.sendwhatmsg(f"+55{select_Num(cntt)}", msg,  time_hora, time_min+1), pi.press('enter')



