import os
import speech_recognition as sr
import pyttsx3 as ts
import pywhatkit
import datetime
import wikipedia as w
import pyjokes as pj
import time

listener =  sr.Recognizer()
engine = ts.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)

def main() :
    def talk(text):
        engine.say(text)
        engine.runAndWait()

    def take_command(): 
        try:
            with sr.Microphone() as source:
                print("listening...")
                voice = listener.listen(source)
                myVoice = listener.recognize_google(voice, language='en-IN', show_all=False)
                print('kee')
                myVoice = myVoice.lower()
                print('You said: '+myVoice)
                    
        except:
            talk("Sorry, I couldn't hear you. Come again please")
            ektara()
        return myVoice
        
    def ektara():
        while True:
            command  = take_command()
                
    command  = take_command()