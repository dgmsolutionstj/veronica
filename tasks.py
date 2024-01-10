# tasks.py
import requests
import datetime
import random
import json
from voice import speak

tasks = []

def add_task(task):
    tasks.append(task)
    speak(f"Note '{task}' has been added.")

def save_tasks():
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')
    speak("Note has been saved.")

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

