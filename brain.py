# veronica.py
import wikipedia as wiki
import wolframalpha
import datetime
import random
import requests
import json
from voice import speak
from ears import take_command
from tasks import add_task, save_tasks, delete_task, review_tasks

# Constants
OPENWEATHERMAP_API_KEY = 'f0c07340096e1c136205f769a53831f9'
WOLFRAM_ALPHA_APP_ID = '6YLR5Q-UYLY82PJ9T'

tasks = []

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
        'units': 'metric'
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

    while True:
        command = take_command()

        if any(exit_keyword in command for exit_keyword in ["quit", "exit"]):
            save_tasks()
            speak("Exiting the room. Goodbye Sir.")
            exit()

        if "add note" in command:
            task = command.replace("add note", "").strip()
            add_task(task)

        elif "save note" in command:
            save_tasks()

        elif "delete note" in command:
            task = command.replace("delete note", "").strip()
            delete_task(task)

        elif "review note" in command:
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

