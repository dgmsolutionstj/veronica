# search.py
import webbrowser
from voice import speak

def google_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    speak(f"Searching Google for {query}")
    webbrowser.open(search_url)
