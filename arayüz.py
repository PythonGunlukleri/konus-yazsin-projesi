from tkinter import *
import speech_recognition as sr
import keyboard

pencere = Tk()
pencere.geometry('200x70')



def clicked():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        ses = r.listen(source, timeout=5)
        keyboard.write(r.recognize_google(ses, language='tr-tr'))
        keyboard.press_and_release('enter')



buton1 = Button(pencere)
buton1.config(text="Ses İle konuş !", bg="green", fg="black", command=clicked)
buton1.pack()
mainloop()