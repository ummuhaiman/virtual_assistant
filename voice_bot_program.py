import tkinter as tk
import threading
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import random
import pyautogui


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


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
            if 'saga' in command:
                command = command.replace('saga', '')
                print(command)
    except sr.UnknownValueError:
        print("Could not understand audio")
    return command
def get_random_story():
    stories = [
        "Once upon a time, there was a brave knight who embarked on a quest to save the kingdom.",
        "In a faraway land, a young magician discovered an ancient spell that could grant unlimited power.",
        "In a small village, a humble farmer found a treasure map and set off on an exciting adventure.",
        "Long ago, a group of friends stumbled upon a hidden portal that led to a magical realm.",
        "In the depths of a mysterious forest, a lost traveler encountered a wise old hermit with a secret.",
        "Many years ago, a legendary pirate sailed the seas in search of a legendary treasure.",
    ]
    return random.choice(stories)

def run_saga():
    while True:
        command = take_command()
        if 'sleep' in command:
            break
        display_text("You: " + command)

        if 'play' in command:
            song = command.replace('play', '')
            sentence = 'Playing ' + song
            talk(sentence)
            pywhatkit.playonyt(song)
            display_text("Saga: " + sentence)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            sentence = 'Current time is ' + time
            talk(sentence)
            display_text("Saga: " + sentence)
        elif 'information about' in command:
            person = command.replace('information about', '')
            sentence = wikipedia.summary(person, 1)
            talk(sentence)
            display_text("Saga: " + sentence)
        elif 'your name' in command:
            sentence = 'I am Saga, how can I assist you?'
            talk(sentence)
            display_text("Saga: " + sentence)
        elif 'how are you' in command:
            sentence = 'I am fine, what about you?'
            talk(sentence)
            display_text("Saga: " + sentence)
        elif 'fine' in command:
            sentence = 'Alright'
            talk(sentence)
            display_text("Saga: " + sentence)
        elif 'which is your favourite subject' in command:
            sentence = 'History'
            talk(sentence)
            display_text("Saga: " + sentence)
        elif 'can i be your friend' in command:
            sentence = 'Yeah, of course'
            talk(sentence)
            display_text("Saga: " + sentence)
        elif 'about you' in command:
            sentence = "I am a conversational AI language model created by Gayathri, Darshini, Ummu, Albie"
            talk(sentence)
            display_text("Saga: " + sentence)
        elif 'Have you studied btech' in command:
            sentence = 'As an artificial intelligence language model, I have not "studied" in the traditional sense'
            talk(sentence)
            display_text("Saga: " + sentence)
        elif 'thank you' in command:
            sentence = 'You\'re welcome'
            talk(sentence)
            display_text("Saga: " + sentence)
        elif 'joke' in command:
            sentence = pyjokes.get_joke()
            talk(sentence)
            display_text("Saga: " + sentence)
        elif 'spotify' in command:
            sentence = 'Opening Spotify'
            talk(sentence)
            webbrowser.open('https://www.spotify.com/')
            display_text("Saga: " + sentence)
            sentence = 'do you have any other question,what can i do for you?'
            talk(sentence)
            display_text("Saga: " + sentence)
            
        elif 'open google' in command:
            sentence = 'Opening Google'
            talk(sentence)
            webbrowser.open('https://www.google.com/')
            display_text("Saga: " + sentence)
            search_query = take_command()
            sentence = f"Searching for {search_query} on Google"
            talk(sentence)
            search_url = 'https://www.google.com/search?q=' + search_query
            webbrowser.open(search_url)
            display_text("Saga: " + sentence)
            sentence = 'do you have any other question,what can i do for you?'
            talk(sentence)
            display_text("Saga: " + sentence)

        elif 'calculate' in command:
            calculation = command.replace('calculate', '')
            try:
                result = str(eval(calculation))
                sentence = f"The result of {calculation} is {result}"
                talk(sentence)
                display_text("Saga: " + sentence)
            except:
                sentence = "Sorry, I couldn't perform the calculation. Please try again."
                talk(sentence)
                display_text("Saga: " + sentence)    
        
         
            
          
           
        elif 'open amazon' in command:
            sentence = 'Opening Amazon'
            talk(sentence)
            webbrowser.open('https://www.amazon.com/')
            display_text("Saga: " + sentence)
            search_product = take_command()
            sentence = f"Searching for {search_product} on Amazon"
            talk(sentence)
            search_url = 'https://www.amazon.com/s?k=' + search_product.replace(' ', '+')
            webbrowser.open(search_url)
            display_text("Saga: " + sentence)
            sentence = 'do you have any other question,what can i do for you?'
            talk(sentence)
            display_text("Saga: " + sentence)

        elif 'open instagram' in command:
            sentence = 'Opening Instagram'
            talk(sentence)
            webbrowser.open('https://www.instagram.com/')
            display_text("Saga: " + sentence)
            sentence = 'do you have any other question,what can i do for you?'
            talk(sentence)
            display_text("Saga: " + sentence)

        elif 'close google' in command:
            sentence = 'Closing Google'
            talk(sentence)
            pyautogui.hotkey('ctrl', 'w')
            display_text("Saga: " + sentence)
            sentence = 'do you have any other question,what can i do for you?'
            talk(sentence)
            display_text("Saga: " + sentence)
           
    
        elif 'rock paper scissors' in command:
            sentence = 'Let\'s play Rock, Paper, Scissors!'
            talk(sentence)
            display_text("Saga: " + sentence)
            choices = ['rock', 'paper', 'scissors']
            user_choice = take_command().lower()
            saga_choice = random.choice(choices)
            result = None
            if user_choice in choices:
                if user_choice == saga_choice:
                    result = 'It\'s a tie!'
                elif (
                    (user_choice == 'rock' and saga_choice == 'scissors') or
                    (user_choice == 'paper' and saga_choice == 'rock') or
                    (user_choice == 'scissors' and saga_choice == 'paper')
                ):
                    result = 'You won!'
                else:
                    result = 'I won!'
            else:
                result = 'Invalid choice. Please try again.'
            talk(result)
            display_text("Saga: " + result)
        elif 'screenshot' in command:
            screenshot_path = 'screenshot.png'
            pyautogui.screenshot(screenshot_path)
            sentence = f'Screenshot taken and saved as {screenshot_path}'
            talk(sentence)
            display_text("Saga: " + sentence)

        elif 'tell me a story' in command:
            story = get_random_story()
            sentence = f"Once upon a time, {story}"
            talk(sentence)
            display_text("Saga: " + sentence)
        elif 'close google' in command:
            sentence = 'Closing Google'
            talk(sentence)
            pyautogui.hotkey('ctrl', 'w')
            display_text("Saga: " + sentence)
            sentence = 'do you have any other question,what can i do for you?'
            talk(sentence)
            display_text("Saga: " + sentence)

        else:
            sentence = 'Please say the command again.'
            talk(sentence)
            display_text("Saga: " + sentence)
       
def button_action():
    t = threading.Thread(target=run_saga)
    t.start()

def display_text(text):
    text_area.insert(tk.END, text + '\n')
    text_area.see(tk.END)

# Create the Tkinter window
window = tk.Tk()
window.title("Saga - Voice Assistant")

# Create a button
button = tk.Button(window, text='Start Voice Assistant', command=button_action)
button.pack()

# Create a text area for displaying the conversation
text_area = tk.Text(window, height=10, width=50)
text_area.pack()

# Start the Tkinter event loop
window.mainloop()