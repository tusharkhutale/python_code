# -*- coding: utf-8 -*-

import speech_recognition as sr
import pyttsx3 
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
#voices = engine.getProperty('voices')   // convert alexa voice to female voice
#engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
     try:
        
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)
     except:
        print('Error to listen')
        #talk('Error to listen')
      
     return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')  #%I:%M -> for 24 hour
        print(time)
        talk('Current time is '+ time)
    elif 'who is' in command:
        person = command.replace('who the heck is','')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'what is' in command:
        person = command.replace('who the heck is','')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')
        
while True:
 run_alexa()