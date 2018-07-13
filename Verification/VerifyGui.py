#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import Verify

class VerifyGui(Tk):

    def __init__(self):
        super().__init__()
        self.title("身份信息录入")
        self.geometry("280x240+400+130")
        self.resizable(0, 0)
        self["bg"] = "lightgray"

        self.setup_UI()

    def setup_UI(self):

        self.style01 = Style()
        self.style01.configure("TLabel", font=("微软雅黑", 9, "bold"), foreground="navy", background="lightgray")
        self.style01.configure("TButton", font=("微软雅黑", 9, "bold"), foreground="navy", background="lightgray")

        # 学号
        self.stid_lable = Label(self, text="学号:", font=("微软雅黑", 9, "bold"), width=8)
        self.stid_lable.place(x=20, y=20)

        self.var_stid = StringVar()
        self.stid_entry = Entry(self, textvariable=self.var_stid, font=("微软雅黑", 9, "bold"), width=16)
        self.stid_entry.place(x=80, y=20)

        # 姓名
        self.name_lable = Label(self, text="姓名:", font=("微软雅黑", 9, "bold"), width=8)
        self.name_lable.place(x=20, y=50)

        self.var_name = StringVar()
        self.name_entry = Entry(self, textvariable=self.var_name, font=("微软雅黑", 9, "bold"), width=16)
        self.name_entry.place(x=80, y=50)

        # 性别
        self.sex_lable = Label(self, text="性别:", font=("微软雅黑", 9, "bold"), width=8)
        self.sex_lable.place(x=20, y=80)

        self.var_sex = StringVar()
        self.sex_entry = Entry(self, textvariable=self.var_sex, font=("微软雅黑", 9, "bold"), width=16)
        self.sex_entry.place(x=80, y=80)

        # 电话号码
        self.mobile_lable = Label(self, text="电话号码:", font=("微软雅黑", 9, "bold"), width=8)
        self.mobile_lable.place(x=20, y=110)

        self.var_mobile = StringVar()
        self.mobile_entry = Entry(self, textvariable=self.var_mobile, font=("微软雅黑", 9, "bold"), width=16)
        self.mobile_entry.place(x=80, y=110)

        # 电子邮件
        self.email_lable = Label(self, text="电子邮件:", font=("微软雅黑", 9, "bold"), width=8)
        self.email_lable.place(x=20, y=140)

        self.var_email = StringVar()
        self.email_entry = Entry(self, textvariable=self.var_email, font=("微软雅黑", 9, "bold"), width=16)
        self.email_entry.place(x=80, y=140)

        self.enter_button = Button(self, text="提交", command=self.check_info, width=8)
        self.enter_button.place(x=160, y=180)

    def check_info(self):
        stid = self.var_stid.get()
        name = self.var_name.get()
        sex = self.var_sex.get()
        mobile = self.var_mobile.get()
        email = self.var_email.get()

        # 实例方法调用
        # current = Verify.Verify(stid, name, sex, mobile, email)  # 实例化
        # check_result = current.check_all()  # 校验输入

        # 类方法调用
        current = Verify.Verify_cls(stid, name, sex, mobile, email)
        check_result = current.check_all()

        if check_result == 1:
            showinfo("系统消息", "学号不符合要求[要求：95开头的6位数字]")
        elif check_result == 2:
            showinfo("系统消息", "姓名不符合要求[要求：2-10个汉字]")
        elif check_result == 3:
            showinfo("系统消息", "性别不符合要求[要求：只能填男或者女]")
        elif check_result == 4:
            showinfo("系统消息", "手机号码不符合要求[要求：11位数字]")
        elif check_result == 5:
            showinfo("系统消息", "邮箱地址不符合要求")
        elif check_result == 0:
            showinfo("系统消息", "添加成功")

if __name__ == "__main__":
    this_VerifyGui = VerifyGui()
    this_VerifyGui.mainloop()