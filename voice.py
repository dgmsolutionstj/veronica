# voice.py
import pyttsx3 as tts

engine = tts.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', 135)

def speak(text):
    engine.say(text)
    engine.runAndWait()

