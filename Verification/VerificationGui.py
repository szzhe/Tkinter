#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

class Verification(Tk):

    def __init__(self):
        super().__init__()
        self.title("身份信息录入")
        self.geometry("280x240+400+130")
        self.resizable(0, 0)
        self["bg"] = "lightgray"

        self.setup_UI()

    def setup_UI(self):

        self.style01 = Style()
        self.style01.configure("TLabel", font=("微软雅黑", 8, "bold"), foreground="navy", background="lightgray")
        self.style01.configure("TButton", font=("微软雅黑", 8, "bold"), foreground="navy", background="lightgray")

        # 学号
        self.stid_lable = Label(self, text="学号:", font=("微软雅黑", 8, "bold"), width=8)
        self.stid_lable.place(x=20, y=20)

        self.stid_entry = Entry(self, font=("微软雅黑", 8, "bold"), width=16)
        self.stid_entry.place(x=80, y=20)

        # 姓名
        self.name_lable = Label(self, text="姓名:", font=("微软雅黑", 8, "bold"), width=8)
        self.name_lable.place(x=20, y=50)

        self.name_entry = Entry(self, font=("微软雅黑", 8, "bold"), width=16)
        self.name_entry.place(x=80, y=50)

        # 性别
        self.sex_lable = Label(self, text="性别:", font=("微软雅黑", 8, "bold"), width=8)
        self.sex_lable.place(x=20, y=80)

        self.sex_entry = Entry(self, font=("微软雅黑", 8, "bold"), width=16)
        self.sex_entry.place(x=80, y=80)

        # 电话号码
        self.phone_lable = Label(self, text="电话号码:", font=("微软雅黑", 8, "bold"), width=8)
        self.phone_lable.place(x=20, y=110)

        self.phone_entry = Entry(self, font=("微软雅黑", 8, "bold"), width=16)
        self.phone_entry.place(x=80, y=110)

        # 电子邮件
        self.email_lable = Label(self, text="电子邮件:", font=("微软雅黑", 8, "bold"), width=8)
        self.email_lable.place(x=20, y=140)

        self.email_entry = Entry(self, font=("微软雅黑", 8, "bold"), width=16)
        self.email_entry.place(x=80, y=140)

        self.enter_button = Button(self, text="提交")
        self.enter_button.place(x=160, y=180)

if __name__ == "__main__":
    this_verification = Verification()
    this_verification.mainloop()