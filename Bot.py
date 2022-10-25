import json
import keyboard
from time import sleep
import webbrowser
import selenium
import Wally_Google
import Wally_Tube
import files_system as fs
import Wally_database as wdb
import speech_recognition as sr
import pyttsx3
import Wally_Email
import Wally_Wpp
import Wally_Music


Sys = None

tts_engine = pyttsx3.init()


def speak(text):
  if tts_engine._inLoop:
    tts_engine.endLoop()
  tts_engine.say(text)
  tts_engine.runAndWait()


def inicialize():
    speak('Olá, o que você deseja fazer hoje?')
    print('''OPÇÕES
    - PESQUISAR ALGO
    - ASSISTIR ALGO
    - MODO SISTEMA
    - AGENDA
    - ESCUTAR MÚSICA
    - ENVIAR E-MAIL
    - ENCAMINHAR MENSAGEM
    - SAIR ''')

    microfone = sr.Recognizer()

    with sr.Microphone() as source:

        microfone.adjust_for_ambient_noise(source)
        print('pode falar...')
        audio = microfone.listen(source)
        frase = microfone.recognize_google(audio, language='pt-BR').split()

    for i in frase:
        print(i)
        if i in 'pesquisar' and 'algo':
            Wally_Google.search_google()
        elif i in 'assistir' and 'algo':
            Wally_Tube.search_youtube()
        elif i in 'modo' and 'sistema':
            fs.main()
        elif i in 'agenda':
            wdb.main()
        elif i in 'escutar' and 'música':
            Wally_Music.tocar_musica()
        elif i in 'enviar' and 'email':
            Wally_Email.enviar_email()
        elif i in 'encaminhar' and 'mensagem':
            Wally_Wpp.mensagem()
        elif i == 'sair' or i == 'fechar':
            result = False
            return result


# Main seria a função principal para iniciar o assistente
if __name__ == '__main__':
    print('Olá, eu sou o Wall-y, seu assistente virtual.')
    while True: # Esses laço garante o funcionamento do programa sempre que as teclas chaves foram pressionadas.
     if keyboard.is_pressed('ctrl+alt+m'):
        sleep(0.05)
        Sys = inicialize()
        sleep(0.05)
        if Sys == False:
            break
     elif keyboard.is_pressed('ctrl+alt+g'):
         exit()