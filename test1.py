#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *

def submit():
    print(u.get())
    p.set(u.get())

root = Tk()
root.title("测试")
frame = Frame()
frame.pack(padx=8, pady=8, ipadx=4, ipady=4)  # padx和pady,组件内部在x(y)方向上填充的空间大小;ipadx和ipady,组件外部在x(y)方向上填充的空间大小

lab1 = Label(frame, text="获取:")
lab1.grid(row=0, column=0, padx=5, pady=5, sticky=W)

u = StringVar()
ent1 = Entry(frame, textvariable=u)
ent1.grid(row=0, column=1, sticky='ew', columnspan=2)

lab2 = Label(frame, text="显示:")
lab2.grid(row=1, column=0, padx=5, pady=5, sticky=W)

p = StringVar()
ent2 = Entry(frame, textvariable=p)
ent2.grid(row=1, column=1, sticky='ew', columnspan=2)

button = Button(frame, text="登录", command=submit, default='active')
button.grid(row=2, column=1)

button2 = Button(frame, text="退出", command=quit)
button2.grid(row=2, column=2, padx=5, pady=5)

# root.update_idletasks()
# x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
# y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
# root.geometry("+%d+%d" % (x, y))

root.mainloop()