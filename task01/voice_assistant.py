
import speech_recognition as sr
import pyttsx3
import pywhatkit
import os
import webbrowser
import pyautogui
import time
from datetime import datetime

# --- CONFIGURATION ---
ASSISTANT_NAME = "Jarvis"
engine = pyttsx3.init()
engine.setProperty('rate', 180)
engine.setProperty('volume', 1.0)

def speak(text):
    print(f"[{ASSISTANT_NAME}]: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"User: {query}")
        return query.lower()
    except:
        return "none"

# --- CORE FUNCTIONS ---

def open_whatsapp_and_message(person_name, message):
    """Specific fix for WhatsApp Desktop App"""
    speak(f"Opening WhatsApp to message {person_name}")
    # Open WhatsApp Desktop (Works if installed from MS Store)
    os.system("start whatsapp:") 
    time.sleep(3) # Wait for app to load
    
    # Search for person
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(1)
    pyautogui.write(person_name)
    time.sleep(2)
    pyautogui.press('enter') # Select the first contact
    
    # Type and send
    pyautogui.write(message)
    pyautogui.press('enter')
    speak("Message sent.")

def save_note_to_desktop(content):
    speak("Saving your note to the desktop.")
    # Create file name with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"Note_{timestamp}.txt"
    desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop', file_name)
    
    with open(desktop_path, "w") as f:
        f.write(content)
    
    # Open it for the user to see
    os.startfile(desktop_path)
    speak("I have saved and opened the note for you.")

# --- MAIN ENGINE ---

def start_assistant():
    speak(f"Systems online. How can I help you?")
    
    while True:
        query = take_command()

        if "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
            speak("YouTube is now open.")

        elif "play song" in query:
            song = query.replace("play song", "").strip()
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)

        elif "send message" in query:
            # Example: "send message to Rahul hello how are you"
            speak("Who should I message on WhatsApp?")
            name = take_command()
            speak(f"What is the message for {name}?")
            msg = take_command()
            open_whatsapp_and_message(name, msg)

        elif "write note" in query:
            speak("What should the note say?")
            note_content = take_command()
            save_note_to_desktop(note_content)

        elif "search" in query:
            search_term = query.replace("search", "").strip()
            speak(f"Searching Google for {search_term}")
            pywhatkit.search(search_term)

        elif "exit" in query or "sleep" in query:
            speak("Powering down. Goodbye.")
            break

if __name__ == "__main__":
    start_assistant()