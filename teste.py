import speech_recognition as sr


def testando():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:

        microfone.adjust_for_ambient_noise(source)
        print('Diga alguma coisa')

        audio = microfone.listen(source)
        frase = microfone.recognize_google(audio, language='pt-BR').split()
        print(frase)


testando()







