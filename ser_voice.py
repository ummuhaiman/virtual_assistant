import speech_recognition as sr
from textblob import TextBlob
import random
import pyttsx3
import tkinter as tk

# Initialize the recognizer
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

# Create the GUI window
window = tk.Tk()
window.title("Speech Sentiment Analysis")
window.geometry("400x300")

# Create a label to display the output text
output_label = tk.Label(window, text="", wraplength=380)
output_label.pack(pady=50)

# Record audio from the microphone
def record_audio():
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)
    return audio

# Convert speech to text
def speech_to_text(audio):
    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

# Perform sentiment analysis on the text
def perform_sentiment_analysis(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

# Get a random motivational quote
def get_motivational_Positive():
    quotes = [
        
        "The only way to do great work is to love what you do. -Steve Jobs",
        "Don't watch the clock; do what it does. Keep going. -Sam Levenson",
        "The future belongs to those who believe in the beauty of their dreams. -Eleanor Roosevelt"
        
    ]
    return random.choice(quotes)

def get_motivational_Negative():
    quotes=[
        "Believe you can and you're halfway there. -Theodore Roosevelt",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. -Winston Churchill",
        "If there is no struggle, there is no progress.” —Frederick Douglass",
        "Someone will declare, “I am the leader!” and expect everyone to get in line and follow him or her to the gates of heaven or hell. My experience is that it doesnt happen that way. Others follow you based on the quality of your actions rather than the magnitude of your declarations.” ―Bill Walsh",
        "Develop success from failures. Discouragement and failure are two of the surest stepping stones to success.” —Dale Carnegie"
    ]
    return random.choice(quotes)
def get_motivational_Neutral():
    quotes=[
       "Success is peace of mind, which is a direct result of self-satisfaction in knowing you made the effort to become the best of which you are capable.” —John Wooden",
        "Never give up on a dream just because of the time it will take to accomplish it. The time will pass anyway.” —Earl Nightingale"
        "Good, better, best. Never let it rest. 'Til your good is better and your better is best."
    
    ]  

    return random.choice(quotes)

# Convert text to speech
def text_to_speech(text):
    engine.setProperty("rate",150)  # Adjust the speech rate as needed
    engine.say(text)
    engine.runAndWait()

# Process the audio and update the GUI
def process_audio():
    audio = record_audio()
    if audio:
        text = speech_to_text(audio)
        if text:
            sentiment = perform_sentiment_analysis(text)
            output_label.config(text="Sentiment: " + sentiment)
            if sentiment == "Positive":
                motivational_quote = get_motivational_Positive()
                output_label.config(text=output_label.cget("text") + "\nMotivational Quote: " + motivational_quote)
                text_to_speech(motivational_quote)
            elif sentiment == "Negative":
                motivational_quote = get_motivational_Negative()
                output_label.config(text=output_label.cget("text") + "\nMotivational Quote: " + motivational_quote)
                text_to_speech(motivational_quote)
            else:
                motivational_quote = get_motivational_Neutral()
                output_label.config(text=output_label.cget("text") + "\nMotivational Quote: " + motivational_quote)
                text_to_speech(motivational_quote)
               
# Create a button to trigger audio processing
process_button = tk.Button(window, text="Recording", command=process_audio)
process_button.pack()

# Run the GUI event loop
window.mainloop()