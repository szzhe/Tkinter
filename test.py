#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.ttk import *

def changeItems():
    print(cnames.get())
    tnames = 'python', 'TCL', 'ruby', 'java'
    cnames.set(tnames)

root = Tk()
root.geometry('+400+200')
root.minsize(400, 200)
root.title("test")

tnames = 'python', 'TCL', 'ruby'
cnames = StringVar()
cnames.set(tnames)
l = Listbox(root, listvariable=cnames, height=10).grid()

Button(root, text="submit", command=changeItems).grid()

root.mainloop()