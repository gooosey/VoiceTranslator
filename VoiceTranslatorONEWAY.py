import speech_recognition as sr 
import pyttsx3 
from langdetect import detect
from googletrans import Translator
import keyboard

r = sr.Recognizer()
translator = Translator(service_urls=['translate.google.com'])
tts = pyttsx3.init()

# Logic
while True: 
    # micro phone
    with sr.Microphone() as source:
        print("Speak")
        # ambient
        r.adjust_for_ambient_noise(source)

        # Get voice
        audio = r.listen(source)
        
    try:
            # get recog
        text = r.recognize_google(audio)
        inputlan = detect(text)

        if inputlan == "jp":
            translation = translator.translate(text, dest='en')
            print(f"trnaslated to english: {translation.text}")
                # speak text
            tts.say(translation.text)
            tts.runAndWait()

        elif inputlan == "en":
            translation = translator.translate(text, dest='ja')
            print(translation.text)
            # speak text
            tts.say(translation.text)
            tts.runAndWait()
        
        

        else:
            print("Unable to detect language.")

    except sr.UnknownValueError:
        print("Could not understand audio.")

    except sr.RequestError as e:
        print("Error during request: {e}")





