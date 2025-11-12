from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from pynput import keyboard
from pynput.keyboard import Key
from pynput.keyboard import Controller as KeyboardController
import random
import time
import threading
import sys
import os

afkActive = {"flag": False}

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def afkBreaker():
    afkActive["flag"] = False

def antiFK():
    while afkActive["flag"] == True:
        kbController = KeyboardController()
        keyPicked = random.randint(1,3)

        if keyPicked == 1:
            for i in range(1, 101):

                kbController.tap("a")
                time.sleep(0.001)

        elif keyPicked == 2:
            for i in range(1, 101):

                kbController.tap("d")
                time.sleep(0.001)

        else:
            kbController.tap(Key.space)

        intervalPicker = random.randint(5,10)
        time.sleep(intervalPicker)

def startAntiFKthread():
    afkActive["flag"] = True
    thread = threading.Thread(target=antiFK)
    thread.daemon = True
    thread.start()

antiFKpanel = tk.Tk()
antiFKpanel.title("Anti-AFK Script")
antiFKpanel.wm_resizable(width=False, height=False)
antiFKpanel.geometry("430x250")
icoPath = resource_path("favicon.ico")
antiFKpanel.iconbitmap(icoPath)

antiAFKactivate = tk.Button(antiFKpanel, text="Activate Anti-AFK Measures", command = startAntiFKthread, cursor= "hand2", bg="lightgray", activebackground="gray")
antiAFKdeactivate = tk.Button(antiFKpanel, text="Deactivate Anti-AFK Measures", command = afkBreaker, cursor= "hand2", bg="lightgray", activebackground="gray")

antiAFKactivate.pack(pady=55)
antiAFKdeactivate.pack()

antiFKpanel.eval('tk::PlaceWindow . center')
antiFKpanel.mainloop()