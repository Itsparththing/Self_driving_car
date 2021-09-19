import speech_recognition as sr
import pyttsx3
import time
listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()
talk("Welcome to SDC")
talk("Have a comfortable ride")
talk("Please choose your destination")
