chat_command=''
import tkinter as tk
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

import tkinter.messagebox as messagebox




engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def chat_system(chat):

    chat_command=chat
     #print(chat_command)

    if 'play' in chat_command:
        song = chat_command.replace('play', '')
        sentance = 'playing ' + song
        talk(sentance)
        return sentance
        pywhatkit.playonyt(song)
    elif 'time' in chat_command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        sentance='Current time is' + time
        talk(sentance)
        return sentance
    elif 'information about' in chat_command:
        person = chat_command.replace('information about', '')
        sentance = wikipedia.summary(person, 1)
        talk(sentance)
        return sentance
    elif 'your name' in chat_command:
        sentance='Iam saga,how can i assist you'
        talk(sentance)
        return sentance
    elif 'how are you' in chat_command:
        sentance='fine what about you'
        talk(sentance)
        return sentance
    elif 'fine' in chat_command:
        sentance='Alright'
        talk(sentance)
        return sentance
    elif 'which is your favorite subject' in chat_command:
        sentance='history'
        talk(sentance)
        return sentance
    elif 'can i be your friend' in chat_command:
        sentance ='yeah ofcourse'
        talk(sentance)
        return sentance
    elif 'about you' in chat_command:
        sentance="I am a conversational AI language model created by Gayathri,darshini,ummu,Albie "
        talk(sentance)
        return sentance
    elif 'Have you study btech' in chat_command:
        sentance='As an artificial intelligence language model, I have not "studied" in the traditional sense'
        talk(sentance)
        return sentance
    elif 'thank you' in chat_command:
        sentance='youre welcome'
        talk(sentance)
        return sentance
    elif 'joke' in chat_command:
        sentance=pyjokes.get_joke()
        talk(sentance)
        return sentance
    elif 'god' in chat_command:
       sentance="As an artificial intelligence language model, I don't have personal beliefs or emotions"
       talk(sentance)
       return sentance
    else:
        talk('say the command again')
        return ''






#to print in the first window