
import os
import speech_recognition as sr
import pyttsx3 as ts
import pywhatkit
import datetime
import wikipedia as w
import pyjokes as pj
import time
global interrupted
    
listener =  sr.Recognizer()
engine = ts.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)
interrupted = False   

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command(): 

    with sr.Microphone(sample_rate = 20000) as source:
        print("listening...")
        voice = listener.record(source,duration= 5)
        
        try:
            myVoice = listener.recognize_google(voice, language='en-IN')  # convert audio to text
        except sr.UnknownValueError:  # error: recognizer does not understand
            talk("I did not get that")
            run_rose()
        except sr.RequestError:
            # error: recognizer is not connected
            talk('Sorry, the service is down')
            run_rose()
        myVoice = myVoice.lower()
    return myVoice


def run_rose():
    command = take_command()
    print('Entered run_rose function')
    k = 'This is something I got: ' + command
    talk(k)

    if 'play' in command:
    
        meta = command.replace('play','')
        song = meta.replace('siri','')
        print('----------')
        print('playing'+ song)
        talk('playing'+ song)
        pywhatkit.playonyt(song)
    

    elif 'time' in command:
        __time__ = datetime.datetime.now().strftime('%H:%M')
        timeInAMPM = datetime.datetime.now().strftime('%I %M %p')
        talk('Its now '+  __time__)
        talk('or'+ timeInAMPM)
  
    elif 'joke' in command:
        joke = pj.get_joke()
        talk(joke)
        print(joke)

    elif 'quit' in command:
        talk('Tata Bye bye')
        return interrupted == True

    elif 'who is' in command:
        item0 = command.replace('who is','')
        info = w.summary(item0,1)
        print(info)
        talk(info)

    else :
        talk('Sorry? I didn\'t get you')

def WakeUpCall(): 
    talk("Hi I am Nidhi. How can I help?")
    print('How can I help?')

def main():
         
    WakeUpCall()
    while True:
        run_rose()


if __name__ == '__main__':
    main()
    