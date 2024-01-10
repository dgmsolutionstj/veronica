# DGTech Solutions LLC
# Veronica v1.0.0
# requests@dgtech.com
# open-source project / Last Update: 1/09/2024
# Day 1 on development.
# ==================================================================================

#* Import Modules
#* Veronica's Skills List 
import pyttsx3 as tts
import datetime
import wikipedia as wiki
import speech_recognition as sr
import wolframalpha
import requests
import random
import json

#* Start the voice engine for Veronica.
engine = tts.init('sapi5')

#* Setting the rate of the voice of Veronica
rate = engine.getProperty('rate')
engine.setProperty('rate', 135)

#* OpenWeatherMap API Key - Replace 'YOUR_OPENWEATHERMAP_API_KEY' with your actual API key
OPENWEATHERMAP_API_KEY = 'f0c07340096e1c136205f769a53831f9'

#* Wolfram Alpha API Key - Replace 'YOUR_WOLFRAM_ALPHA_API_KEY' with your actual API key
WOLFRAM_ALPHA_APP_ID = '6YLR5Q-UYLY82PJ9T'

#& Creating the voice of Veronica.
def speak(text):
    engine.say(text)
    engine.runAndWait()

#& Function to recognize speech
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

tasks = []

def add_task(task):
    tasks.append(task)
    speak(f"Item '{task}' has been added.")

def save_tasks():
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')
    speak("Item have been saved.")

def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        speak(f"Item '{task}' has been deleted.")
    else:
        speak(f"Item '{task}' not found.")

def review_tasks():
    if tasks:
        speak("Here are your current Items:")
        for i, task in enumerate(tasks, start=1):
            speak(f"{i}. {task}")
    else:
        speak("You don't have any items at the moment.")

#& Veronica will greet the user depending on the time of the day.
def greeting():

    current_hour = datetime.datetime.now().hour

    if 0 <= current_hour < 12:
        speak("Good Morning Sir")
    elif 12 <= current_hour < 17:
        speak("Good afternoon Sir")
    else:
        speak("Good Night Sir")

    speak("How can I help you today")

if __name__ == '__main__':

    intents = load_intents()

    random_responses = [response for intent in intents if intent['name'] == 'fallback' for response in intent['responses']]

    greeting()

    #& Veronica now can response to human voice.
    while True:
        command = take_command()

        if any(exit_keyword in command for exit_keyword in ["quit", "exit"]):
            save_tasks()
            speak("Exiting the room. Goodbye Sir.")
            exit()

        if "add item" in command:
            task = command.replace("add item", "").strip()
            add_task(task)

        elif "save item" in command:
            save_tasks()

        elif "delete item" in command:
            task = command.replace("delete item", "").strip()
            delete_task(task)

        elif "review item" in command:
            review_tasks()

        if "time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The current time Sir is {current_time}")

        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f"Today Sir is {current_date}")

        elif "search" in command:
            search_query = command.replace("search", "").strip()
            try:
                result = wiki.summary(search_query, sentences=4)
                print(result)
                speak(result)
            except wiki.exceptions.DisambiguationError:
                speak("There are multiple matches. Please be more specific.")
            except wiki.exceptions.PageError:
                speak("I couldn't find any information on that topic.")
            except Exception as e:
                print(f"Error during Wikipedia search: {e}")
                speak("An error occurred while fetching information. Please try again later.")

        elif "calculate" in command:
            query = command.replace("calculate", "").strip()
            try:
                result = wolfram_alpha_query(query)
                print(result)
                speak(result)
            except Exception as e:
                print(f"Error during Wolfram Alpha query: {e}")
                speak("An error occurred while processing the calculation. Please try again later.")

        elif "weather" in command:
            city = command.replace("weather", "").strip()
            get_weather(city)

        else:
            for intent in intents:
                if any(pattern in command for pattern in intent['patterns']):
                    speak(get_response(intent['name'], intents, random_responses))
                    break
            else:
                speak(random.choice(random_responses)) 
     