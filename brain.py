# brain.py
import datetime
import wikipedia as wiki
import random

from neurons import greet, speak, take_command, load_intents, get_response, wolfram_alpha_query, get_weather, google_search, add_task, save_tasks, delete_task, review_tasks

def main():
    intents = load_intents()
    random_responses = [response for intent in intents if intent['name'] == 'fallback' for response in intent['responses']]

    greet()

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

        elif "search google" in command:
            query = command.replace("search google", "").strip()
            google_search(query)

        else:
            for intent in intents:
                if any(pattern in command for pattern in intent['patterns']):
                    speak(get_response(intent['name'], intents, random_responses))
                    break
            else:
                speak(random.choice(random_responses))

if __name__ == '__main__':
    main()
