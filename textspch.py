from tkinter import *
from gtts import gTTS
from playsound import playsound
import os


root = Tk()
root.geometry('420x200')
root.resizable(0,0)
root.title('Text to speech converter')

message_string = StringVar()
Label(root, text = 'Text:', font = 'arial 15 bold').place(x=32, y=50)
entry_field = Entry(root, textvariable = message_string, width = '60').place(x=32, y=80)

def TextSpeech():
	message = message_string.get()
	message_speech = gTTS(text = message, lang='en')
	message_speech.save('Saved.mp3')
	playsound('Saved.mp3')
	os.remove('Saved.mp3')

def Exit():
	root.destroy()

def Reset():
	message_string.set('')

Button(root, text = 'PLAY', font = 'arial 15 bold', bg = 'red', padx = 2, command = TextSpeech).place(x=32, y=110)
Button(root, text = 'RESET', font = 'arial 15 bold', bg = 'red', padx = 2, command = Reset).place(x=120, y=110)
Button(root, text = 'EXIT', font = 'arial 15 bold', bg = 'red', padx = 2, command = Exit).place(x=230, y=110)


root.mainloop()