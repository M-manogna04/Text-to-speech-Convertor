import tkinter as tk
from gtts import gTTS
import os

window=tk.Tk()
window.title("Python Text-Speech")
window.config(bg="lavender")
window.geometry('650x650')

message=tk.StringVar()

def play():
    language="en"
    myobj=gTTS(text=message.get(),lang=language,slow=False)
    myobj.save("speech.mp3")
    os.system("speech.mp3")


tk.Label(window,text="TEXT-TO-SPEECH",font='"Arial" 20 italic underline',bg="aquamarine2").pack()

tk.Label(window,text="Enter Text",font='"Arial" 14 italic').place(x=120,y=60)
tk.Entry(window,font='"Arial" 12',textvariable=message).place(x=300,y=60)

tk.Button(window,text="SUBMIT",font='"times new roman" 12 bold',command=play,width=10,bg="ghostwhite").place(x=230,y=150)

window.mainloop()
