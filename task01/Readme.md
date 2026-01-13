# Voice Automation Assistant
is a Python-based voice assistant designed to automate desktop tasks. Using speech recognition and GUI automation, it can send WhatsApp messages, take notes, play music on YouTube, and perform web searches.



## ✨ Features
* **WhatsApp Automation**: Search for a contact and send a message via the WhatsApp Desktop App.
* **Voice Notes**: Dictate notes and have them automatically saved as `.txt` files on your Desktop.
* **YouTube Integration**: Play any song or video instantly using voice commands.
* **Web Searching**: Perform hands-free Google searches.
* **System Speech**: Natural-sounding text-to-speech feedback.

## 🛠️ Requirements & Installation

### 1. Prerequisites
Ensure you have **Python 3.8+** installed on your system. You also need the **WhatsApp Desktop App** (Windows Store version) installed and logged in for the messaging feature to work.

### 2. Install Dependencies
Run the following command to install all necessary libraries:

```bash
pip install speechrecognition pyttsx3 pywhatkit pyautogui



🚀 How to Use
Run the script:

Bash

python voice_assistant.py
Wait for the "Systems online" prompt.

Example Commands:

"Play song Blinding Lights"

"Write a note" (will ask what to write)

"Send message" (will ask for the recipient and message)

"Search for the nearest coffee shop"

"Exit" or "Sleep" to turn off.
