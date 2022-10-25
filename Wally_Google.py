import keyboard
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import speech_recognition as sr
import pyttsx3


tts_engine = pyttsx3.init()


def speak(text):
  if tts_engine._inLoop:
    tts_engine.endLoop()
  tts_engine.say(text)
  tts_engine.runAndWait()


def search_google():
    frase = input('\nO que deseja pesquisar? ')

    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico)
    driver.maximize_window()
    driver.get(f"https://www.google.com/search?q={frase}")
    try:
        driver.find_element(By.TAG_NAME, 'h3').click()
    except Exception:
        pass

    while True:
        if keyboard.is_pressed('ctrl+w'):
            driver.close()
            break

