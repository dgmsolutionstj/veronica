# ears.py
import speech_recognition as sr
from voice import speak

def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Adjusted energy_threshold:", r.energy_threshold)

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I did not understand your command.")
        return ""
    except sr.RequestError as e:
        print(f"Error with the speech recognition service; {e}")
        speak("I am sorry, but I am having trouble with the speech recognition service.")
        return ""

