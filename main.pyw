
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

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command(): 
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            print("pee")
            myVoice = listener.recognize_google(voice, language='en-IN', show_all=False)
            print('kee')
            myVoice = myVoice.lower()
            print('You said: '+myVoice)
                   
    except:
        talk("Sorry, I couldn't hear you. Come again please")
        ektara()
    return myVoice


def finish():
    talk("Time is up, Time is up")
  

def run_rose():
    command = take_command()
    print('Entered run_rose function')
    print('This is something I got: ' + command)
    if 'play' in command:
    
        meta = command.replace('play','')
        song = meta.replace('siri','')
        print('----------')
        print('playing'+ song)
        talk('playing'+ song)
        pywhatkit.playonyt(song)
        '''    
    elif 'set a timer for' in command:

        meta = [int(s) for s in command.split() if s.isdigit()]
        print(meta)
        time.sleep(3)
        if 'minutes' in command:
            talk('Setting a timer for ' +str(meta[0])+ 'and ' +str(meta[1])+ 'seconds' )
        else:
            talk('Setting a timer for '+str(meta[0])+'seconds')
        seconds = meta[0]*60 + meta[1]
        print(seconds)
        time.sleep(seconds)
        finish()
        print("Exit\n")
        '''

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

def ektara():
    while True:
        run_rose()
            

global interrupted

interrupted = False

print('Welcome to VoiceAssistance by Nidhi')

def WakeUpCall(): 
    while True:
        with sr.Microphone() as source:
            print('Waiting for you voice')
            wakeupword = listener.listen(source)
            WuW = listener.recognize_google(wakeupword)
            WuW = WuW.lower()
            print('aapne kaha '+ WuW)
            if 'julie' in WuW:
                talk('Hi I\'m Julie. How can I help?')
                print('How can I help?')
                ektara()

WakeUpCall()           

print('ending session')