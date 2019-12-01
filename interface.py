# import tkinter as tk
# from tkinter import *
# #import os

# root = tk.Tk()

# canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")

# root.mainloop()
import pyaudio
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
try:
    print("System predicts: " + r.recognize_google(audio))
except Exception:
    print("error")