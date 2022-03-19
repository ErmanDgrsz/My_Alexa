import googlesearch
import speech_recognition as sr
import pyaudio
import pyttsx3
import random
import datetime
import wikipedia as wikipedia
from googlesearch import search
import os
import urllib.request
import webbrowser


def speak():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Alexa: Listening...")
            audio = r.listen(source)
            try:
                query = r.recognize_google(audio)
                print(f"master:{query}")
                return query
            except:
                print("Try Again")


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def answer_byalexa(audio):
    engine.say(audio)
    engine.runAndWait()


while True:
    query = speak().lower()  # takes user command

    if 'name' in query:
        answer_byalexa("Hi boss! My  Name is Alexa")
    elif 'are you single' in query:
        answers = ['Ofcourse I am single what do you expect?', 'Dude I am a Robot'
            , 'Mind your own business casanova!']
        answer_byalexa(random.choice(answers))
    elif 'hate' in query:
        answer_byalexa("I hate when people call me machine")
    elif 'love' in query:
        answer_byalexa("I love raspberries, only")
    elif 'what time is it' in query:
        time = datetime.datetime.now().strftime('%I:%M %p')
        answer_byalexa(f"It's {time} master")
    elif 'wikipedia' in query:
        query = query.replace('wikipedia', '')
        answer_byalexa(wikipedia.summary(query, sentences=1))
    elif 'search' in query:
        query = query.replace('search', '')
        result = search(query, start=0, stop=5)
        for i in result:
            print(i)
    elif 'open' in query:
        query = query.replace('open', '')
        os.system(query)
    elif 'chrome' or 'browser' in query:
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk')
    elif 'youtube' in query:
        browser = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        webbrowser.get(browser).open_new_tab('https://www.youtube.com/')
