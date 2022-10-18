import wikipedia
import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyttsx3

def entra21():
    # Informações de usuário
    user = input('Informe seu login: ').lower()
    user_password = input('Informe sua senha: ').lower()
    Comment_Class = input('Diga uma observação da aula de hoje: ')
    sleep(0.1)

    BOT = webdriver.Chrome(executable_path=r"C:\Users\patrique.pacheco\AppData\Local\Programs\Python\Python310\chromedriver.exe")
    BOT.maximize_window()

    BOT.get("https://externo.proway.com.br/login-aluno")
    sleep(2)
    BOT.find_element(By.XPATH, '//*[@id="formLoginSubscriber_username"]').send_keys(f'{user}')
    sleep(0.3)
    BOT.find_element(By.XPATH, '//*[@id="formLoginSubscriber_password"]').send_keys(f'{user_password}')
    sleep(0.3)
    BOT.find_element(By.XPATH, '//*[@id="formLoginSubscriber"]/div[3]/div/div/div/button').click()
    sleep(0.5)
    BOT.find_element(By.XPATH, '//*[@id="root"]/section/section/div[1]/div/div/div/ul/li[1]/ul/li/button').click()
    sleep(0.2)
    BOT.find_element(By.XPATH, '//*[@id="dailyEvaluationForm_hoje"]/div/label[5]').click()
    sleep(0.1)
    BOT.find_element(By.XPATH, '//*[@id="dailyEvaluationForm_instrutorMetodologia"]/div/label[5]').click()
    sleep(0.1)
    BOT.find_element(By.XPATH, '//*[@id="dailyEvaluationForm_instrutorPostura"]/div/label[5]').click()
    sleep(0.1)
    BOT.find_element(By.XPATH, '//*[@id="dailyEvaluationForm_instrutorDominio"]/div/label[5]').click()
    sleep(0.1)
    BOT.find_element(By.XPATH, '//*[@id="dailyEvaluationForm_empresaAmbiente"]/div/label[5]').click()
    sleep(0.1)
    BOT.find_element(By.XPATH, '//*[@id="dailyEvaluationForm_empresaMicro"]/div/label[5]').click()
    sleep(0.1)
    BOT.find_element(By.XPATH, '//*[@id="dailyEvaluationForm_empresaRecepcao"]/div/label[5]').click()
    sleep(0.1)
    BOT.find_element(By.XPATH, '//*[@id="dailyEvaluationForm_obs"]').send_keys(f'{Comment_Class}')
    sleep(0.1)
    BOT.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[2]').click()
    sleep(1)







