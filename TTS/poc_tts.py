import pyttsx3

def tekst_na_mowe(tekst, jezyk='polish'):
    engine = pyttsx3.init()
    
    voices = engine.getProperty('voices')
    for voice in voices:
        if jezyk in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    else:
        print(f"Nie znaleziono głosu dla języka: {jezyk}. Używam domyślnego głosu.")

    engine.setProperty('rate', 140)

    engine.say(tekst)

    engine.runAndWait()

tekst = "Witaj, jak się masz?"
tekst_na_mowe(tekst)
