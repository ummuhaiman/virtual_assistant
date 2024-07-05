import chat_bot_program

import subprocess
import tkinter as tk
import tkinter.messagebox as messagebox
import time





#create a window tkinter and setting up

window = tk.Tk()
window.title("SAGA")
window.geometry("1300x700")
window.resizable(False,False)
welcome_saga=tk.Label(text="SAGA")
welcome_saga.pack()
chat_here = tk.Label(window, text="CHAT HERE:")
chat_here.place(x=0,y=50)



conversation_text = tk.Text(window, width=89, height=21)
conversation_text.place(x=100, y=100)
    

def two_fun_for_chat():
    user_input = command_entry.get()
    conversation_text.insert(tk.END, "User: " + user_input + "\n")

    response = chat_bot_program.chat_system(user_input)
    conversation_text.insert(tk.END, "SAGA: " + response + "\n")

    command_entry.delete(0, tk.END)
def two_fun_for_voice():
    subprocess.call(['python',"voice_bot_program.py"]) 
def run_file():
    subprocess.call(['python',"test.py"]) 
    # Here you can add the code to open and process the selected file
def age_gender():
   subprocess.call(['python',"test1.py"]) 

def record_audio():
   subprocess.call(['python',"ser_voice.py"]) 

command_entry=tk.Entry(window,width=87)
command_entry.place(x=100,y=54)
submit_button=tk.Button(window,text="submit",command=two_fun_for_chat)
submit_button.place(x=1070,y=45)
start_button=tk.Button(window,text="voice",command=two_fun_for_voice)
start_button.place(x=1200,y=42)
or_option = tk.Label(window, text="OR")
or_option.place(x=1160,y=50)

open_file_button = tk.Button(window, text="face_emotion_prediction", command=run_file)
open_file_button.place(x=1070, y=100)

open_file_button = tk.Button(window, text="Age_gender_prediction", command=age_gender)
open_file_button.place(x=1070, y=150)

open_file_button = tk.Button(window, text="SER", command=record_audio)
open_file_button.place(x=1070, y=190)


def exit_message():

    result = messagebox.askokcancel("Are you sure ?")
    if result == True:
        window.destroy()
exit_button=tk.Button(window,text="CLICK HERE TO EXIT",command=exit_message)
exit_button.place(x=570,y=617)

window.mainloop()
