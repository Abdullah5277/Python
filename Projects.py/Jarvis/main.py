import speech_recognition as sr
import webbrowser 
import pyttsx3  # MODULE TEXT TO SPEECH 
import Jarvis.musiclibrary as musiclibrary
import requests

recognizer = sr.Recognizer()  # RECOGNIZER() IS A CLASS
engine = pyttsx3.init()


def speak(text):  
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    c = c.lower().strip()
    
    if "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c:
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com")
    elif "open instagram" in c:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
    elif c.startswith("play"):
        try:
            # Extract song name and convert to lowercase
            song = c.split(" ", 1)[1].strip().lower()
            
            # Check if song exists (prevents crash)
            if song in musiclibrary.music:
                speak(f"Playing {song}")
                link = musiclibrary.music[song]
                webbrowser.open(link)
            else:
                speak(f"Song {song} not found")
                print(f"Available songs: {list(musiclibrary.music.keys())}")
                
        except IndexError:
            speak("Please say play followed by song name")
    elif c.lower().startswith("news"):
        r=requests.get("")

        #open Ai handle the request
        
        
    
if __name__ == "__main__":
    speak("Initializing Jarvis")  # LISTEN FOR THE WAKE WORD "JARVIS"

    while True:
        try:
            # LISTENING FOR WAKE WORD
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)

            print("Recognizing...")
            word = recognizer.recognize_google(audio)
            print("You said:", word)

            if "jarvis" in word.lower():
                speak("Yes, I am listening")

                # LISTENING FOR NEXT COMMAND
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

                word = recognizer.recognize_google(audio)
                print("Command:", word)
                processCommand(word)

        except sr.UnknownValueError:
            print("Could not understand audio")