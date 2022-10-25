import keyboard
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import speech_recognition as sr


def search_youtube():

    frase = input("O que deseja ver: ")

    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    navegador.maximize_window()

    navegador.get(f"https://www.youtube.com/results?search_query={frase}")
    sleep(4)
    navegador.find_element(By.ID, 'video-title').click()
    sleep(3)
    keyboard.press('f')
    while True:
        if keyboard.is_pressed('ctrl+w'):
            navegador.close()
            break