import keyboard
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep



def search_google():
        search = input("O que deseja pesquisar: ").lower()
        servico = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=servico)
        driver.maximize_window()
        driver.get(f"https://www.google.com/search?q={search}")
        try:
            driver.find_element(By.TAG_NAME, 'h3').click()
        except Exception:
            pass
        while True:
            if keyboard.is_pressed('ctrl+w'):
                driver.close()
                break