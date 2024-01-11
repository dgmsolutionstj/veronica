# neurons.py
from datetime import datetime
import pyttsx3 as tts
import speech_recognition as sr
import wikipedia as wiki
import wolframalpha
import random
import requests
import json
import webbrowser

OPENWEATHERMAP_API_KEY = 'f0c07340096e1c136205f769a53831f9'
WOLFRAM_ALPHA_APP_ID = '6YLR5Q-UYLY82PJ9T'

# Start the voice engine for Veronica.
engine = tts.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', 135)

def greet():
    current_hour = datetime.now().hour

    if 0 <= current_hour < 12:
        speak("Good Morning Sir")
    elif 12 <= current_hour < 17:
        speak("Good afternoon Sir")
    else:
        speak("Good Night Sir")

    speak("How can I help you today")

def speak(text):
    engine.say(text)
    engine.runAndWait()

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

def load_intents():
    try:
        with open('./intents.json', 'r') as file:
            intents = json.load(file)
        return intents['intents']
    except FileNotFoundError:
        print("Intents file not found.")
        speak("I am sorry, but there seems to be an issue with my configuration. Please contact support.")
        exit()
    except json.JSONDecodeError:
        print("Error decoding intents file.")
        speak("I am sorry, but there seems to be an issue with my configuration. Please contact support.")
        exit()

def get_response(intent_name, intents, random_responses):
    for intent in intents:
        if intent['name'] == intent_name:
            return random.choice(intent['responses'])
    return random.choice(random_responses)

def wolfram_alpha_query(query):
    client = wolframalpha.Client(WOLFRAM_ALPHA_APP_ID)
    try:
        res = client.query(query)
        pods = [pod.text for pod in res.pods if pod.text]
        if pods:
            answer = "\n".join(pods)
            return answer
        else:
            return "I'm sorry, I couldn't find an answer to that question."
    except Exception as e:
        print(f"Error during Wolfram Alpha query: {e}")
        return "An error occurred while processing the calculation. Please try again later."

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': OPENWEATHERMAP_API_KEY,
        'units': 'metric'  # You can change units to 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        print(f"API Status Code: {response.status_code}")
        print(f"API Response: {response.text}")

        if response.status_code == 200:
            weather_data = response.json()
            temperature = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            speak(f"The current weather in {city} is {temperature} degrees Celsius with {description}.")
        elif response.status_code == 404:
            speak(f"Sorry, I couldn't find weather information for {city}. Please check the city name and try again.")
        else:
            speak("Sorry, I couldn't retrieve the weather information. Please try again later.")

    except Exception as e:
        print(f"Error during weather query: {e}")
        speak("An error occurred while fetching weather information. Please try again later.")

def google_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    speak(f"Searching Google for {query}")
    webbrowser.open(search_url)

tasks = []

def add_task(task):
    tasks.append(task)
    speak(f"Note '{task}' has been added.")

def save_tasks():
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')
    speak("Note have been saved.")

def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        speak(f"Note '{task}' has been deleted.")
    else:
        speak(f"Note '{task}' not found.")

def review_tasks():
    if tasks:
        speak("Here are your current Notes:")
        for i, task in enumerate(tasks, start=1):
            speak(f"{i}. {task}")
    else:
        speak("You don't have any Notes at the moment.")
