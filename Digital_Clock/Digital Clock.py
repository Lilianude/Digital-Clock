# from tkinter import Tk, Label
# from tkinter.ttk import *
# import time

# root = Tk()
# root.title("Digital Clock")
# root.resizable(1 ,1)

# def present_time():
#     currentTime = time.strftime('%I:%M:%S %p')
#     digi_clock.config(text = currentTime) # this displays it
#     digi_clock.after(200,present_time) # after ever 200 millisecond, it will run
    
# digi_clock = Label(root, font = ('arial', 48, 'bold'), bg = '#e5e6aa', fg = '#e8c815' )
# digi_clock.pack()

# present_time()
# root.mainloop()





import tkinter as tk
from datetime import datetime
import sys

# designing the outlook of the clock
digitalClock = tk.Tk()
digitalClock.title('Digital Clock')
digitalClock.geometry('650x250')
digitalClock.resizable(1,1)

# designing the font and background colo of the clock
textFont = ('Sans Serif', 48, 'bold')
background = '#e5e6aa'
foreground = '#e8c815'
borderWidth = 35

#let's define the label for the application

def digital_clock():
    current_timestamp = datetime.now()
    time = current_timestamp.strftime('%H:%M:%S')
    label.config(text = time)
    label.after(20, digital_clock)
    
label = tk.Label(digitalClock, font = textFont, bg = background, fg = foreground, bd = borderWidth)
label.grid(row =0, column =1)
label.pack()

    
    
digital_clock()
digitalClock.mainloop()

