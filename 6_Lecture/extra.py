from tkinter import *
from tkinter.ttk import *
from time import strftime



root = Tk()
root.title('Programing Basics Clock')

def clock():
    tick = strftime('%H:%M:%S %p')
    label.config(text=tick)
    label.after(1000, clock)

label = Label(root, font =('sans',80), background = 'purple', foreground = 'yellow')
label.pack(anchor = 'center')
clock()
mainloop()

